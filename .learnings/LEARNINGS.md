## [LRN-20260226-005] User explicitly manages telegram-logger service

**Logged**: 2026-02-26T22:18:00Z
**Priority**: high
**Status**: resolved
**Area**: workflow

### Summary
I repeatedly attempted to manage and verify the `telegram-logger` service (stop, extract, install dependencies, restart, check status/logs) despite the user stating that the installation was complete and configured. The user explicitly directed me to remove these steps from my workflow.

### Details
My previous workflow assumed I needed to verify all aspects of a new service installation. However, the user clarified that they are managing the `telegram-logger` service directly and that I should not interfere with or verify those steps. My continued attempts to manage the service were unnecessary and frustrating for the user.

### Suggested Action
When a user explicitly states that a service or configuration is "done" or "configured," trust their statement and proceed with subsequent steps without attempting to re-verify or re-manage components of that service. If a problem arises that *requires* service management, inform the user and await their explicit instruction before acting.

### Resolution
- **Resolved**: 2026-02-26T22:18:00Z
- **Notes**: Updated internal workflow to respect user's explicit control over external service management. Will no longer attempt to verify or restart `telegram-logger` unless specifically instructed by the user.

---

## [LRN-20260310-001] Preference for Tavily Search over standard web_search

**Logged**: 2026-03-10T18:48:00Z
**Priority**: high
**Status**: promoted
**Area**: tools

### Summary
The standard `web_search` tool is currently unconfigured. The custom `tavily-search` skill is the preferred way to perform web searches in this workspace.

### Details
The `web_search` tool in OpenClaw requires a Perplexity or Brave API key, which is currently missing. However, the `tavily-search` skill is installed and fully functional via its CLI scripts. This was discovered when a test query for Stockholm weather failed with a missing key error.

### Suggested Action
Always use `node ~/.openclaw/workspace/skills/tavily-search/scripts/search.mjs "query"` for searching. This provides cleaner, AI-optimized results.

### Resolution
- **Resolved**: 2026-03-10T18:48:00Z
- **Promoted**: TOOLS.md, AGENTS.md
- **Notes**: Added explicit usage instructions to TOOLS.md and a mandatory recall/usage rule to AGENTS.md.

---

## [LRN-20260310-002] Multi-step tool use for status checking

**Logged**: 2026-03-10T18:57:00Z
**Priority**: low
**Status**: resolved
**Area**: tools

### Summary
`openclaw status` command did not complete instantly and required `process` tool to poll for output.

### Details
When running `openclaw status` via `exec`, the command may not return immediately on some systems (like a Raspberry Pi). Instead of failing or hanging, I successfully used `process(action="poll")` with a session ID to retrieve the results.

### Suggested Action
When a command via `exec` returns a "still running" message, use the `process` tool with `action="poll"` to fetch the output rather than assuming an error.

### Resolution
- **Resolved**: 2026-03-10T18:57:00Z
- **Notes**: Successfully retrieved the gateway status using this two-step process.

---
