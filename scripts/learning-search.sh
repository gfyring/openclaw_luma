#!/bin/bash
# Search learnings by keyword

LEARNINGS_DIR="$HOME/.openclaw/workspace/.learnings"

if [ -z "$1" ]; then
    echo "Usage: bash scripts/learning-search.sh <keyword>"
    echo ""
    echo "Examples:"
    echo "  bash scripts/learning-search.sh sonos"
    echo "  bash scripts/learning-search.sh 'exec timeout'"
    echo ""
    echo "Files available:"
    echo "  - LEARNINGS.md (corrections, discoveries, best practices)"
    echo "  - ERRORS.md (command failures, exceptions)"
    echo "  - FEATURE_REQUESTS.md (missing capabilities)"
    exit 1
fi

QUERY="$1"
RESULT_COUNT=0

echo "=== Searching .learnings/ for: $QUERY ==="
echo ""

for file in "$LEARNINGS_DIR"/{LEARNINGS,ERRORS,FEATURE_REQUESTS}.md; do
    if [ -f "$file" ]; then
        FILE_BASENAME=$(basename "$file")
        MATCHES=$(grep -n -i "$QUERY" "$file" || true)
        if [ -n "$MATCHES" ]; then
            echo "📄 $FILE_BASENAME:"
            echo "$MATCHES" | head -10 | sed 's/^/  /'
            if [ "$(echo "$MATCHES" | wc -l)" -gt 10 ]; then
                echo "  ... and more"
            fi
            echo ""
            RESULT_COUNT=$((RESULT_COUNT + $(echo "$MATCHES" | wc -l)))
        fi
    fi
done

if [ "$RESULT_COUNT" -eq 0 ]; then
    echo "❌ No matches found for: $QUERY"
    exit 1
else
    echo "✅ Found $RESULT_COUNT matches"
fi
