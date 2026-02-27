#!/bin/bash
# Helper for auto-logging errors
# Called by error-detector hook or used manually
# Usage: auto-log-error.sh "command" exit_code "output"

LEARNINGS_DIR="$HOME/.openclaw/workspace/.learnings"
ERRORS_FILE="$LEARNINGS_DIR/ERRORS.md"

if [ $# -lt 2 ]; then
    echo "Usage: $0 <command> <exit_code> [output]"
    exit 1
fi

COMMAND="$1"
EXIT_CODE="$2"
OUTPUT="${3:-}"

# Generate entry ID
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
DATE=$(date +%Y%m%d)
RAND_ID=$(od -An -N3 -tx1 /dev/urandom | tr -d ' ')
ID="${DATE}-${RAND_ID}"

# Extract command name
CMD_NAME=$(echo "$COMMAND" | awk '{print $1}' | xargs basename)

# Build entry
ENTRY="## [ERR-$ID] $CMD_NAME (exit $EXIT_CODE)

**Logged**: $TIMESTAMP
**Priority**: medium
**Status**: pending
**Area**: infra

### Summary
Command failed with exit code $EXIT_CODE

### Command
\`\`\`
$COMMAND
\`\`\`

### Error Output
\`\`\`
${OUTPUT:-(no output captured)}
\`\`\`

### Context
Exit code: $EXIT_CODE
Timestamp: $TIMESTAMP

### Suggested Fix
(User should fill in after reviewing error)

### Metadata
- Reproducible: (unknown)
- Related Files: (none yet)

---
"

# Append to file
{
    flock -x 9
    echo "$ENTRY" >> "$ERRORS_FILE"
} 9>"$ERRORS_FILE.lock" 2>/dev/null

echo "✅ Error logged to ERRORS.md"
echo "   ID: ERR-$ID"
echo ""
echo "Review with:"
echo "  bash scripts/learning-search.sh '$CMD_NAME'"
