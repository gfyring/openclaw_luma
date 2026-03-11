# Home Assistant — Palaistina (Landet)

MCP server: `HA-Palaistina`

This file contains specific knowledge for the home "Landet" or "Palaistina".

## Common Task Workflows
- **Status Check:** Use `ha_get_overview` to fetch current domain stats (temperature, motion, light status).
- **Lights:** Use the `light` domain; target by area ID or specific entity (e.g., `light.hallen`, `light.kok`).
- **Motion Sensors:** Check `binary_sensor` entities (e.g., `binary_sensor.rorelsesensor_occupancy`). Last trigger time is stored in `input_datetime` helpers.

## Key Facts
- Location: Palaistina/Landet
- Features: Temperature control (Holken, Sjostugan, Vardagsrummet), motion sensing, router monitoring.

## Motion Sensors (Last Update)
- `input_datetime.motion_sensor_vardagsrummet_last_update`
- `input_datetime.motion_sensor_utekallaren_last_update`

## Temperature Control (Input Booleans/Numbers)
- **Holken:** `input_boolean.holken_element_auto`, `input_number.holken_min_temp`, `input_number.holken_max_temp`
- **Sjostugan:** `input_boolean.sjostugan_element_auto`, `input_number.sjostugan_min_temp`, `input_number.sjostugan_max_temp`
- **Vardagsrummet:** `input_boolean.vardagsrummet_element_auto`, `input_number.vardagsrummet_min_temp`, `input_number.vardagsrummet_max_temp`

## Lights (Examples)
| Friendly name | Entity ID |
|--------------|-----------|
| Spot 3 loftet | `light.spot_3_loftet` |
| Tak 1 köket | `light.tak_1_koket` |
| Tak 2 köket | `light.tak_2_koket` |
| Matplats | `light.matplats` |
| Vardagsrum | `light.vardagsrum` |
| Kök | `light.kok` |
| Hallen | `light.hallen` |
| Kotten | `light.kotten` |

## Automations
- `Meddelande rörelsesensor vardagsrummet`
- `Meddelande rörelsesensor utekällaren`
- `Temperature Control Holken Auto`
- `Temperature Control Sjostugan Auto`
- `Temperature control vardagsrummet auto`
- `Daily House Health Check`
