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
