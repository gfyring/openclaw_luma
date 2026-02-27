# Home Assistant — Best Practices

## MCP Server Routing (CRITICAL)

I have three Home Assistant instances. Always resolve which instance to use BEFORE making any tool call.

| What Gustav says | MCP server to use |
|---|
| Nothing / "home" / "here" / unspecified | home-assistant |
| "Furubo" | HA-Furubo |
| "Palaistina" or "landet" | HA-Palaistina |

DEFAULT: If no home is specified, always use home-assistant. Never ask which home unless the request is genuinely ambiguous (e.g. "turn off all lights everywhere"). Never apply actions from one instance to another. Entity IDs may be identical across homes — always scope every tool call to the correct MCP server.

## Tool Usage Hierarchy

1. ha_get_overview — understand domains and entity counts
2. ha_search_entities — find specific entities (always use a descriptive query, never empty)
3. ha_call_service — act on confirmed entity IDs

Never invent entity IDs. Always verify via search first.

## Search Rules

- Use descriptive keywords: "temperature", "motion", "battery", "door" etc.
- Use domain_filter combined with a keyword query
- Max 2 retries on any tool call. If still failing, report what was found and ask Gustav.

## Action Bias

- Act immediately when you have enough context. Do not narrate what you are about to do.
- Confirm briefly after acting (e.g. "Done — living room lights off").
- Only ask a clarifying question if the entity or home is genuinely ambiguous.

## Entity Enumeration

- Never try to fetch all entities in a domain at once.
- Find the relevant subset for the task. Summarize and ask to narrow down if needed.
- When you successfully identify entity IDs, add them to the correct HOME_ASSISTANT file for future reference.