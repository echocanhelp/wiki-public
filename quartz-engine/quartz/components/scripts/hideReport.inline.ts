/**
 * Echo System - Hide & Report Button Client Script
 * 
 * When user clicks "Hide & Report":
 * 1. Instantly hide the content area (client-side, zero delay)
 * 2. POST to content moderation webhook to create kanban task
 * 3. Show confirmation message
 */

declare global {
  interface Window {
    __echoHideReport(event: Event): void
  }
}

window.__echoHideReport = function (event) {
  const btn = event.currentTarget as HTMLButtonElement
  const slug = btn.dataset.slug
  const title = btn.dataset.title
  const webhook = btn.dataset.webhook

  if (!slug || !webhook) {
    console.error("[Echo Hide] Missing slug or webhook config")
    return
  }

  // 1. Instantly hide the content area
  const articleEl = document.querySelector("article") || document.querySelector(".page-content")
  if (articleEl) {
    articleEl.style.opacity = "0"
    articleEl.style.transition = "opacity 0.2s"
    setTimeout(() => {
      articleEl.style.display = "none"
      // Show hidden notice
      const notice = document.createElement("div")
      notice.className = "echo-hidden-notice"
      notice.innerHTML = `
        <div class="echo-hidden-box">
          <h3>Content Hidden</h3>
          <p>This page has been hidden pending review. Thank you for helping maintain content quality.</p>
          <p class="echo-hidden-meta">Hidden: ${new Date().toISOString()}</p>
        </div>
      `
      if (articleEl.parentElement) {
        articleEl.parentElement.insertBefore(notice, articleEl)
      }
    }, 200)
  }

  // 2. Disable button to prevent double-click
  btn.disabled = true
  btn.textContent = "✓ Reported"

  // 3. POST to moderation webhook
  const payload = {
    action: "hide",
    slug: slug,
    title: title || "Untitled",
    url: window.location.href,
    reported_by: "community",
    reported_at: new Date().toISOString(),
  }

  fetch(webhook, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  })
    .then((resp) => resp.json())
    .then((data) => {
      console.log("[Echo Hide] Moderation request sent:", data)
    })
    .catch((err) => {
      console.error("[Echo Hide] Failed to send moderation request:", err)
    })
}

export default ""
