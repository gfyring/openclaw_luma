# TOOLS.md - My Home

This file is your map of the physical home. Read it whenever you need to translate natural language ("living room lights") into HA entity IDs or understand the home's layout.

Keep it up to date. When you discover new entity IDs, rename a device, or add something new — update this file.

---

## MCP Connection

Home Assistant is available via MCP through mcporter.

- **MCP server name:** `home-assistant`
- **Connection:** via mcporter (already configured in your OpenClaw setup)
- **Always use MCP tools** to read state before acting — never assume what's on or off
- **Always verify** after acting by reading state back. If state didn't change, report it — don't retry blindly.

---

## Rooms & Areas

| Room | HA Area ID | Notes |
|------|-----------|-------|
| Bedroom | `bedroom` | |
| Hallen | `hallen` | |
| Kitchen | `kitchen` | |
| Köket | `koket` | |
| Living Room | `living_room` | |
| Sams rum | `sams_rum` | |
| Vardagsrummet | `vardagsrummet` | Main area |

---

## Lights

### Living Room
| Friendly name | Entity ID | Type | Notes |
|--------------|-----------|------|-------|
| 55\" Philips 8008 Ambilight | `light.55_philips_8008_ambilight` | Hue | ? |
| Fåtöljen | `light.fatoljen` | Hue | ? |
| Fönstret | `light.fonstret` | Hue | ? |
| Gamla datorn | `light.gamla_datorn` | Hue | ? |
| Hemma | `light.hemma` | Hue | ? |
| Lampan över tv:n | `light.lampan_over_tv_n` | Hue | ? |
| Läslampa | `light.laslampa` | Hue | ? |
| Matbord | `light.matbord` | Hue | ? |
| Matbordet | `light.matbordet` | Hue | ? |
| Mattan | `light.mattan` | Hue | `light.mattan_2` and `light.mattan_3` also exist |
| Nya datorn | `light.nya_datorn` | Hue | ? |
| Soffan | `light.soffan` | Hue | ? |
| Soffbordet | `light.soffbordet` | Hue | `light.soffbordet_2`, `light.soffbordet_3` and `light.soffbordet_4` also exist |
| Vardagsrum | `light.vardagsrum` | Hue | ? |
| Vardagsrummet | `light.vardagsrummet` | Hue | ? |
| Home Assistant Voice 097249 LED Ring | `light.home_assistant_voice_097249_led_ring` | Hue | ? |

### Bedroom
| Friendly name | Entity ID | Type | Notes |
|--------------|-----------|------|-------|
| Sams lampa | `light.sams_lampa` | Hue | unavailable |
| Sams rum | `light.sams_rum` | Hue | ? |
| Sängen | `light.sangen` | Hue | ? |
| Sams skrivbord | `light.sams_skrivbord` | Hue | ? |

### Kitchen
| Friendly name | Entity ID | Type | Notes |
|--------------|-----------|------|-------|
| Diskbänk | `light.diskbank` | Hue | ? |
| Köket | `light.koket` | Hue | ? |
| Köksön | `light.kokson` | Hue | `light.kokson_2` and `light.kokson_3` also exist |
| Spisen | `light.spisen` | Hue | `light.spisen_2` and `light.spisen_3` also exist |

### Hall
| Friendly name | Entity ID | Type | Notes |
|--------------|-----------|------|-------|
| Hallen | `light.hallen` | Hue | `light.hallen_2`, `light.hallen_3`, `light.hallen_4`, `light.hallen_5`, `light.hallen_6` and `light.hallen_7` also exist |
| Hallen Entré | `light.hallen_entre` | Hue | `light.hallen_entre_2` and `light.hallen_entre_3` also exist |

### Light Groups (if any)
| Group name | Entity ID | Type | Members |
|-----------|-----------|---------|
| Hela | `light.hela` | Hue | All lights? | This could be an "all lights" group. |


---

## Media Players

| Friendly name | Entity ID | Type | Supports |
|--------------|-----------|------|---------|
| 55\" Philips 8008 | `media_player.55_philips_8008` | TV | on/off, volume, source, media_title: HBO Max |
| Home Assistant Voice 097249 Media Player | `media_player.home_assistant_voice_097249_media_player` | Speaker | volume |
| Spotify Gustav Fyring | `media_player.spotify_gustav_fyring` | Music Player | play, pause, volume, source |
| Vardagsrummet | `media_player.vardagsrummet` | Apple TV | on/off, volume, play, pause, source |

### Media Notes
- Spotify is controlled via `media_player` entities — use `media_player.play_media` service
- Volume is 0.0–1.0 scale in HA
- The `media_player.55_philips_8008` currently playing \"HBO Max\".

---

## Home Assistant Instances

Three instances are configured. See HOME_ASSISTANT_BEST_PRACTICES.md for routing rules. See HOME_ASSISTANT.md, HOME_ASSISTANT_FURUBO.md, HOME_ASSISTANT_PALAISTINA.md for entity references. Never use a Home Assistant tool without first confirming which MCP server to target.

---

## Himalaya Mail

Himalaya is configured to manage mail for `luma@fyring.se`. It can read and send emails, although the CLI may sometimes report errors for sending operations even when successful.

### Account Details
- **Email Address:** `luma@fyring.se`
- **Default Account:** Yes
- **CLI Tool:** `himalaya`

### Reading Mail

**List all folders:**
```bash
himalaya folder list --account luma --output json
```

**List latest 5 emails in INBOX (including read):**
```bash
himalaya envelope list --account luma --folder INBOX --output json --page-size 5 "order by date desc"
```

**List latest 5 unread emails in INBOX:**
```bash
himalaya envelope list --account luma --folder INBOX --output json --page-size 5 "flag unseen"
```

**Read a specific email by ID (e.g., ID 2):**
```bash
himalaya message read 2 --account luma --output json
```

### Sending Mail

To send an email, construct the full raw message (including headers and body) and pipe it to `himalaya message send`.

**Example:**
```bash
himalaya message send --account luma <<< "From: Luma <luma@fyring.se>
To: recipient@example.com
Cc: cc@example.com
Subject: Your Subject Here

Your message body goes here."
```

**Quirk:** The `himalaya message send` command may report an error even if the email is successfully sent.

---

## Automations (important ones)

| Friendly name | Automation ID | Purpose |
|--------------|--------------|---------|
| Notify on poor network quality | `automation.notify_on_poor_network_quality` | Notifies when network quality is poor |
| Increment TV watch seconds every minute while Apple TV is playing | `automation.increment_tv_watch_seconds_every_minute_while_apple_tv_is_playing` | Tracks TV watching time |
| Notify on long TV session | `automation.notify_on_long_tv_session` | Notifies for extended TV sessions |
| Create repair notification on sensor anomaly | `automation.create_repair_notification_on_sensor_anomaly` | Creates repair notification for sensor issues |
| Restart router on sustained poor network | `automation.restart_router_on_sustained_poor_network` | Restarts router if network is poor |
| Sync AI Dashboard Every 10 Minutes | `automation.sync_ai_dashboard_every_10_minutes` | Syncs AI Dashboard periodically |

---

## Home Assistant Overview

| Tool Name | Description | Use Case |
|---|---|---|
| `ha_get_overview()` | Get a comprehensive overview of all entities, organized by domain and area, with current state and attributes. | General "status at home" queries, health checks, finding all entities. |

## Quirks & Known Issues

- Example: \"The bedroom Zigbee bulb sometimes doesn\'t respond on first command — retry once before reporting failure\"\n- Example: \"TV entity goes `unavailable` when on standby — check with `ha_get_state` first\"\n- **Observation:** The \'Passive BLE monitor integration update\' entity is still present in `update` domain, despite BLE sensors being removed. This indicates the integration might still be installed.\n- **Observation:** A sensor state reads: "Network score: 0 • Apple TV: HBO Max (off) • TV today: unknown • Sensor health: degraded". This suggests a potential network or TV-related issue.\n\n---\n\n## How to Update This File\n\nWhen you add a new device or rename something:\n1. Ask the agent: \"Update TOOLS.md with the new entity ID for [device]\"\n2. Or edit directly and tell the agent: \"TOOLS.md has been updated, re-read it\"\n\nThe agent should proactively update this file when it discovers new entity IDs during tasks.\n