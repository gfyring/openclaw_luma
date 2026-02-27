# HEARTBEAT.md

# Keep this file empty (or with only comments) to skip heartbeat API calls.

# Add tasks below when you want the agent to check something periodically.

# Check for new emails
himalaya envelope list --account luma --folder INBOX --output json --page-size 5 "flag unseen"
