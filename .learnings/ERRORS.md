## [ERR-20260226-003] Himalaya attachment download --dir flag error

**Logged**: 2026-02-26T18:16:00Z
**Priority**: high
**Status**: pending
**Area**: tools

### Summary
Attempted to use `--dir` flag with `himalaya attachment download` but it was not recognized, resulting in an error.

### Error
```
error: unexpected argument '--dir' found

  tip: to pass '--dir' as a value, use '-- --dir'

Usage: himalaya attachment download --account <NAME> <ID>...

For more information, try '--help'.
```

### Context
- Command/operation attempted: `himalaya attachment download 13 --account luma --dir ~/.openclaw/workspace/services/`
- Issue: The `--dir` flag was not a valid argument for `himalaya attachment download`.

### Suggested Fix
Consult `himalaya attachment download --help` for correct usage of flags and parameters for specifying output directory, or assume it downloads to current working directory.

### Resolution
- **Status**: pending

---

## [ERR-20260310-001] Missing Perplexity API Key for web_search

**Logged**: 2026-03-10T18:45:00Z
**Priority**: medium
**Status**: promoted
**Area**: config

### Summary
The standard `web_search` tool failed because it defaulted to Perplexity and no API key was configured.

### Error
```
{
  "error": "missing_perplexity_api_key",
  "message": "web_search (perplexity) needs an API key. Set PERPLEXITY_API_KEY in the Gateway environment, or configure tools.web.search.perplexity.apiKey.",
  "docs": "https://docs.openclaw.ai/tools/web"
}
```

### Context
Attempted to use `web_search` for a routine query. The tool is enabled but has no valid provider key.

### Suggested Fix
Use the `tavily-search` skill instead, as it is already configured and working. Update workspace files to prefer Tavily.

### Resolution
- **Resolved**: 2026-03-10T18:45:00Z
- **Promoted**: TOOLS.md, AGENTS.md
- **Notes**: Added explicit rules to TOOLS.md and AGENTS.md to use Tavily CLI instead of `web_search`.

---

## [ERR-20260310-002] SOUL.md edit failure

**Logged**: 2026-03-10T18:55:00Z
**Priority**: low
**Status**: resolved
**Area**: tools

### Summary
Failed to edit `SOUL.md` on the first attempt due to incorrect white space matching.

### Error
```
{
  "status": "error",
  "tool": "edit",
  "error": "Could not find the exact text in SOUL.md. The old text must match exactly including all whitespace and newlines."
}
```

### Context
Attempted to insert a self-improvement rule into the Boundaries section of `SOUL.md`.

### Suggested Fix
Always read the file content fully before attempting an `edit` to ensure an exact match for the `oldText` parameter.

### Resolution
- **Resolved**: 2026-03-10T18:55:00Z
- **Notes**: Re-read the file and successfully performed the edit on the second attempt.

---
