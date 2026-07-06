---
name: hermes-profile-configuration
category: autonomous-ai-agents
description: Safely apply configuration changes, MCP servers, and skills across multiple Hermes Agent profiles with explicit inclusion/exclusion rules.
---

# Hermes Profile Configuration Management

Handles system-wide configuration of external tools (MCP servers, skills, environment settings) across multiple Hermes profiles while respecting explicit exclusions.

## Core Principle
When making changes that should affect "all agents except X":
- Discover all profiles in `~/.hermes/profiles/`
- Apply changes to every profile **except** those explicitly listed for exclusion
- Use safe YAML merging to avoid breaking existing configuration
- Never modify excluded profiles

## Recommended Workflow
1. List profiles: `ls ~/.hermes/profiles/`
2. Identify exclusion list
3. Use Python + PyYAML (or equivalent) to safely merge new sections into `config.yaml`
4. Verify changes with targeted reads
5. Report exactly which profiles were updated vs skipped

## References
- `references/multi-profile-yaml-merge.md` — safe merging pattern used in production
- `references/gbrain-hermes-integration.md` — example of GBrain MCP server rollout

## When to Use
- Adding MCP servers (GBrain, external tools)
- Enabling/disabling skills across the fleet
- Applying environment variables or feature flags
- Any configuration that must be consistent except for named exceptions