#!/bin/bash
# Quick overview of learning status

LEARNINGS_DIR="$HOME/.openclaw/workspace/.learnings"

echo "=== Learning Management Status ==="
echo ""

# Count by file
echo "📊 By File Type:"
for file in "$LEARNINGS_DIR"/{LEARNINGS,ERRORS,FEATURE_REQUESTS}.md; do
    if [ -f "$file" ]; then
        BASENAME=$(basename "$file")
        COUNT=$(grep -c "^## \[" "$file" || echo "0")
        printf "  %-20s %3d entries\n" "$BASENAME" "$COUNT"
    fi
done

echo ""
echo "📊 By Status:"
PENDING=$(grep -h "Status.*: pending" "$LEARNINGS_DIR"/*.md 2>/dev/null | wc -l)
PROMOTED=$(grep -h "Status.*: promoted" "$LEARNINGS_DIR"/*.md 2>/dev/null | wc -l)
RESOLVED=$(grep -h "Status.*: resolved" "$LEARNINGS_DIR"/*.md 2>/dev/null | wc -l)
printf "  %-20s %3d\n" "Pending" "$PENDING"
printf "  %-20s %3d\n" "Promoted" "$PROMOTED"
printf "  %-20s %3d\n" "Resolved" "$RESOLVED"

echo ""
echo "📊 By Priority:"
grep -h "Priority.*:" "$LEARNINGS_DIR"/*.md 2>/dev/null | sort | uniq -c | while read -r count priority; do
    printf "  %-20s %3d\n" "$priority" "$count"
done

echo ""
echo "⚠️  High-Priority Pending (Action Needed):"
CRITICAL=$(grep -B 1 "Status.*: pending" "$LEARNINGS_DIR"/*.md 2>/dev/null | grep "Priority.*: critical" | wc -l)
HIGH=$(grep -B 1 "Status.*: pending" "$LEARNINGS_DIR"/*.md 2>/dev/null | grep "Priority.*: high" | wc -l)
if [ "$CRITICAL" -gt 0 ] || [ "$HIGH" -gt 0 ]; then
    printf "  Critical: %d\n" "$CRITICAL"
    printf "  High:     %d\n" "$HIGH"
    echo ""
    echo "  Review with: bash scripts/learning-stats.sh --pending"
else
    echo "  ✅ None (all clear!)"
fi

# Show pending details if --pending flag
if [ "$1" == "--pending" ]; then
    echo ""
    echo "=== Pending High-Priority Items ==="
    grep -B 5 "Status.*: pending" "$LEARNINGS_DIR"/*.md 2>/dev/null | grep -E "^##|Priority.*(critical|high)" | head -20
fi
