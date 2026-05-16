/**
 * Echo System - Content Moderation Webhook Server
 *
 * Receives hide requests from the wiki frontend and creates
 * kanban tasks for the moderation queue.
 *
 * Architecture:
 *   Wiki (GitHub Pages) --POST--> [This Server:8891] --CLI--> hermes kanban create
 */

const express = require("express");
const { execSync } = require("child_process");
const crypto = require("crypto");
const fs = require("fs");
const path = require("path");

const app = express();
const PORT = process.env.PORT || 8891;
const LOG_DIR = process.env.LOG_DIR || "/root/wiki-public/moderation-webhook/logs";
const SECRET = process.env.WEBHOOK_SECRET || "echo-moderation-secret";

// Ensure log directory exists
if (!fs.existsSync(LOG_DIR)) {
  fs.mkdirSync(LOG_DIR, { recursive: true });
}

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Request logging
app.use((req, res, next) => {
  const ts = new Date().toISOString();
  console.log(`[${ts}] ${req.method} ${req.path}`);
  next();
});

// Health check
app.get("/health", (req, res) => {
  res.json({
    status: "ok",
    service: "echo-moderation-webhook",
    timestamp: new Date().toISOString(),
    uptime: process.uptime(),
  });
});

// GET /api/content-hide/status - list recent hide requests
app.get("/api/content-hide/status", (req, res) => {
  const recent = readRecentLogs();
  res.json({
    total: recent.length,
    requests: recent,
  });
});

// POST /api/content-hide - main endpoint
app.post("/api/content-hide", (req, res) => {
  const { action, slug, title, url, reported_by, reported_at } = req.body;

  // Validate required fields
  if (!slug || !action || action !== "hide") {
    return res.status(400).json({
      error: "Missing required fields: action='hide' and slug",
    });
  }

  const request_id = crypto.randomBytes(8).toString("hex");
  const timestamp = reported_at || new Date().toISOString();

  // Build kanban task
  const taskTitle = `[Moderation] Review hidden content: ${title || slug}`;
  const taskBody = JSON.stringify(
    {
      action: "content_moderation_review",
      request_id: request_id,
      slug: slug,
      title: title || "Untitled",
      url: url || "N/A",
      reported_by: reported_by || "anonymous",
      reported_at: timestamp,
      status: "pending_review",
      notes:
        "Content was hidden by a community member via the Hide & Report button. " +
        "Review the content and either: (1) restore if appropriate, " +
        "(2) permanently remove if inappropriate, (3) edit if it needs corrections.",
    },
    null,
    2
  );

  // Log the request immediately (before kanban create, so we don't lose it)
  const logEntry = {
    request_id,
    slug,
    title,
    url,
    reported_by,
    timestamp,
    task_title: taskTitle,
    status: "processing",
  };
  appendLog(logEntry);

  // Create kanban task via CLI
  let kanbanResult = null;
  try {
    const cliOutput = execSync(
      `hermes kanban create '${taskTitle.replace(/'/g, "\\'")}' ` +
        `--assignee archivist ` +
        `--priority high ` +
        `--body '${taskBody.replace(/'/g, "\\'")}'`,
      {
        encoding: "utf-8",
        timeout: 15000,
        env: { ...process.env, PATH: "/root/.hermos/bin:" + process.env.PATH },
      }
    );
    kanbanResult = JSON.parse(cliOutput);
    logEntry.status = "kanban_task_created";
    logEntry.kanban_task_id = kanbanResult?.task_id || "unknown";
  } catch (err) {
    console.error("[ERROR] Failed to create kanban task:", err.message);
    logEntry.status = "kanban_create_failed";
    logEntry.error = err.message;
    // Still return success - the hide already happened client-side
  }

  // Update log with final status
  updateLog(request_id, logEntry);

  res.json({
    success: true,
    request_id,
    slug,
    status: logEntry.status,
    kanban_task_id: logEntry.kanban_task_id || null,
    message: `Content hide request processed. ${
      logEntry.status === "kanban_task_created"
        ? "Moderation task created."
        : "Moderation task creation failed - logged for manual review."
    }`,
  });
});

// POST /api/content-hide/bulk - bulk hide (for admin tools)
app.post("/api/content-hide/bulk", (req, res) => {
  const { items } = req.body;

  if (!Array.isArray(items) || items.length === 0) {
    return res.status(400).json({ error: "Expected items array" });
  }

  const results = [];
  for (const item of items) {
    // Reuse the single-item handler logic
    const { slug, title, url, reported_by } = item;
    if (!slug) continue;

    const request_id = crypto.randomBytes(8).toString("hex");
    const timestamp = new Date().toISOString();

    const taskTitle = `[Moderation] Review hidden content: ${title || slug}`;
    const taskBody = JSON.stringify(
      {
        action: "content_moderation_review",
        request_id,
        slug,
        title: title || "Untitled",
        url: url || "N/A",
        reported_by: reported_by || "bulk_admin",
        reported_at: timestamp,
      },
      null,
      2
    );

    let kanbanResult = null;
    try {
      const cliOutput = execSync(
        `hermes kanban create '${taskTitle.replace(/'/g, "\\'")}' ` +
          `--assignee archivist --priority high --body '${taskBody.replace(/'/g, "\\'")}'`,
        { encoding: "utf-8", timeout: 15000 }
      );
      kanbanResult = JSON.parse(cliOutput);
    } catch (err) {
      console.error(`[BULK] Failed for ${slug}:`, err.message);
    }

    results.push({
      slug,
      request_id,
      status: kanbanResult ? "created" : "failed",
      kanban_task_id: kanbanResult?.task_id || null,
    });
  }

  res.json({ success: true, processed: results.length, results });
});

// ============================================================
// Utility functions
// ============================================================

function logFilePath() {
  const date = new Date().toISOString().split("T")[0];
  return path.join(LOG_DIR, `hide-${date}.jsonl`);
}

function appendLog(entry) {
  const fp = logFilePath();
  fs.appendFileSync(fp, JSON.stringify(entry) + "\n");
}

function updateLog(requestId, updatedEntry) {
  const fp = logFilePath();
  if (!fs.existsSync(fp)) return;
  const lines = fs
    .readFileSync(fp, "utf-8")
    .split("\n")
    .filter(Boolean);
  const updated = lines.map((line) => {
    try {
      const entry = JSON.parse(line);
      if (entry.request_id === requestId) return JSON.stringify(updatedEntry);
      return line;
    } catch {
      return line;
    }
  });
  fs.writeFileSync(fp, updated.join("\n") + "\n");
}

function readRecentLogs() {
  const results = [];
  if (!fs.existsSync(LOG_DIR)) return results;
  const files = fs
    .readdirSync(LOG_DIR)
    .filter((f) => f.startsWith("hide-") && f.endsWith(".jsonl"))
    .sort()
    .reverse()
    .slice(0, 3); // last 3 days
  for (const file of files) {
    const lines = fs
      .readFileSync(path.join(LOG_DIR, file), "utf-8")
      .split("\n")
      .filter(Boolean);
    for (const line of lines) {
      try {
        results.push(JSON.parse(line));
      } catch {}
    }
  }
  return results;
}

// ============================================================
// Start server
// ============================================================

app.listen(PORT, "0.0.0.0", () => {
  console.log(`[Echo Moderation Webhook] Listening on port ${PORT}`);
  console.log(`[Echo Moderation Webhook] Health: http://localhost:${PORT}/health`);
  console.log(`[Echo Moderation Webhook] Endpoint: POST http://localhost:${PORT}/api/content-hide`);
});

// Graceful shutdown
process.on("SIGTERM", () => {
  console.log("[SIGTERM] Shutting down...");
  process.exit(0);
});
process.on("SIGINT", () => {
  console.log("[SIGINT] Shutting down...");
  process.exit(0);
});
