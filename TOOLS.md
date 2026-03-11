# TOOLS.md - My Home

This file is your map of the physical home layout, media devices, and non-Home Assistant tools (like Email).

---

## Himalaya Mail

Himalaya is configured to manage mail for `luma@fyring.se`. It can read and send emails, although the CLI may sometimes report errors for sending operations even when successful.

### Account Details
- **Email Address:** `luma@fyring.se`
- **Default Account:** Yes
- **CLI Tool:** `himalaya`

### Email Folders
| Folder Name | Purpose |
|-------------|---------|
| Handled     | Emails already processed or completed. |
| Archive     | Emails for future reference, no action needed. |
| Action      | Emails requiring action, but not immediately. |
| Waiting     | Emails where a response or information is pending. |
| References  | Emails with useful information, links, or documents. |

### Web Search
The standard `web_search` tool is currently missing an API key. Instead, use the **Tavily Search** skill, which is fully configured and optimized for AI-clean results.

**Usage:**
```bash
node /home/gfyring/.openclaw/workspace/skills/tavily-search/scripts/search.mjs "your query"
```
- `-n <count>`: Number of results (default: 5)
- `--deep`: For comprehensive research
- `--topic news`: For current events

---

## Himalaya Mail
