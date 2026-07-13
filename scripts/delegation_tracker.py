#!/usr/bin/env python3
"""
Delegation Tracker - Log and measure delegation efficiency.

Usage:
    python3 delegation_tracker.py log <task> <iterations> <duration> <tokens>
    python3 delegation_tracker.py report
    python3 delegation_tracker.py summary
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime

LOG_FILE = Path("/home/leedt/echo-system/knowledge/operational/delegation-log.jsonl")

def log_delegation(task, iterations, duration_seconds, tokens_input, tokens_output, tool_calls):
    """Log a delegation event."""
    entry = {
        "timestamp": datetime.now().isoformat(),
        "task": task,
        "iterations": iterations,
        "duration_seconds": duration_seconds,
        "tokens_input": tokens_input,
        "tokens_output": tokens_output,
        "tool_calls": tool_calls,
    }
    
    # Append to JSONL log
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")
    
    print(f"✅ Logged: {task}")
    print(f"   {iterations} iterations, {duration_seconds:.0f}s, {tokens_input:,} input tokens, {tokens_output:,} output tokens")

def show_report():
    """Show delegation report."""
    if not LOG_FILE.exists():
        print("No delegation log found.")
        return
    
    entries = []
    with open(LOG_FILE) as f:
        for line in f:
            if line.strip():
                entries.append(json.loads(line))
    
    if not entries:
        print("No delegation entries found.")
        return
    
    print("=== DELEGATION REPORT ===\n")
    print(f"Total delegations: {len(entries)}\n")
    
    total_iterations = sum(e["iterations"] for e in entries)
    total_duration = sum(e["duration_seconds"] for e in entries)
    total_tokens_input = sum(e["tokens_input"] for e in entries)
    total_tokens_output = sum(e["tokens_output"] for e in entries)
    total_tool_calls = sum(e["tool_calls"] for e in entries)
    
    print(f"Total iterations: {total_iterations}")
    print(f"Total duration: {total_duration:.0f}s ({total_duration/60:.1f} min)")
    print(f"Total tokens in: {total_tokens_input:,}")
    print(f"Total tokens out: {total_tokens_output:,}")
    print(f"Total tool calls: {total_tool_calls}")
    print(f"Average duration: {total_duration/len(entries):.0f}s per delegation")
    print(f"Average iterations: {total_iterations/len(entries):.1f} per delegation")
    
    print("\n--- Details ---\n")
    for i, entry in enumerate(entries, 1):
        print(f"{i}. {entry['task']}")
        print(f"   {entry['iterations']} iterations, {entry['duration_seconds']:.0f}s, {entry['tokens_input']:,} in, {entry['tokens_output']:,} out, {entry['tool_calls']} tool calls")
        print()

def show_summary():
    """Show efficiency summary."""
    if not LOG_FILE.exists():
        print("No delegation log found.")
        return
    
    entries = []
    with open(LOG_FILE) as f:
        for line in f:
            if line.strip():
                entries.append(json.loads(line))
    
    if not entries:
        print("No delegation entries found.")
        return
    
    # Calculate efficiency metrics
    total_tool_calls = sum(e["tool_calls"] for e in entries)
    total_iterations = sum(e["iterations"] for e in entries)
    avg_tool_calls_per_iter = total_tool_calls / total_iterations if total_iterations > 0 else 0
    
    print("=== DELEGATION EFFICIENCY SUMMARY ===\n")
    print(f"Delegations completed: {len(entries)}")
    print(f"Total tool calls handled: {total_tool_calls}")
    print(f"Average tool calls per iteration: {avg_tool_calls_per_iter:.1f}")
    print(f"\nToken savings estimate:")
    print(f"  Without delegation: ~{total_tool_calls * 100:,} tokens (main context)")
    print(f"  With delegation: ~{sum(e['tokens_input'] for e in entries):,} tokens (isolated)")
    print(f"  Saved: ~{total_tool_calls * 100 - sum(e['tokens_input'] for e in entries):,} tokens in main context")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 delegation_tracker.py <log|report|summary>")
        print("  log <task> <iterations> <duration> <tokens_in> <tokens_out> <tool_calls>")
        print("  report - Show full delegation report")
        print("  summary - Show efficiency summary")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "log":
        if len(sys.argv) != 8:
            print("Usage: python3 delegation_tracker.py log <task> <iterations> <duration> <tokens_in> <tokens_out> <tool_calls>")
            sys.exit(1)
        task = sys.argv[2]
        iterations = int(sys.argv[3])
        duration = float(sys.argv[4])
        tokens_in = int(sys.argv[5])
        tokens_out = int(sys.argv[6])
        tool_calls = int(sys.argv[7])
        log_delegation(task, iterations, duration, tokens_in, tokens_out, tool_calls)
    
    elif command == "report":
        show_report()
    
    elif command == "summary":
        show_summary()
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)