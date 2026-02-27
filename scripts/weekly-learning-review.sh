#!/bin/bash
# Weekly Learning Review & Promotion
# Runs every Sunday at 20:00 (part of existing cron)
# Reviews pending learnings and suggests promotions

LEARNINGS_DIR="$HOME/.openclaw/workspace/.learnings"
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

echo "🧠 [Learning Review] $TIMESTAMP"
echo ""

# Check if learnings exist
if [ ! -d "$LEARNINGS_DIR" ]; then
    echo "No learnings directory found. Skipping."
    exit 0
fi

# Count pending items
PENDING=$(grep -h "Status.*: pending" "$LEARNINGS_DIR"/*.md 2>/dev/null | wc -l)
PROMOTED=$(grep -h "Status.*: promoted" "$LEARNINGS_DIR"/*.md 2>/dev/null | wc -l)
RESOLVED=$(grep -h "Status.*: resolved" "$LEARNINGS_DIR"/*.md 2>/dev/null | wc -l)

echo "📊 Status:"
echo "  Pending:  $PENDING"
echo "  Promoted: $PROMOTED"
echo "  Resolved: $RESOLVED"
echo ""

# Find high-priority pending
HIGH_PRIORITY=$(grep -B 5 "Status.*: pending" "$LEARNINGS_DIR"/*.md 2>/dev/null | grep -c "Priority.*: high\|critical")

if [ "$HIGH_PRIORITY" -gt 0 ]; then
    echo "⚠️  High-Priority Pending: $HIGH_PRIORITY items"
    echo ""
    echo "Review and promote with:"
    echo "  bash scripts/learning-stats.sh --pending"
    echo ""
    echo "Then update status in .learnings/ files:"
    echo "  **Status**: promoted (and add destination link)"
    echo ""
fi

# Find recurring patterns (3+ See Also links)
echo "🔄 Recurring Patterns (candidates for skills):"
PATTERNS=$(grep -c "See Also:" "$LEARNINGS_DIR"/*.md 2>/dev/null | grep -v ":0$" | wc -l)
if [ "$PATTERNS" -gt 0 ]; then
    echo "  Found $PATTERNS entries with related issues"
    grep -h "Pattern-Key:" "$LEARNINGS_DIR"/*.md 2>/dev/null | sort | uniq -c | awk '$1 >= 2 {print "  - " $2 " (seen " $1 " times)"}' || true
else
    echo "  None detected (keep learning!)"
fi
echo ""

# Summary
if [ "$PENDING" -eq 0 ]; then
    echo "✅ All caught up! No pending learnings."
else
    echo "📝 Next action: Review pending items above and promote high-value ones"
    echo ""
fi
