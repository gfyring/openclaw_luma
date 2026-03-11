# Home Assistant — Furubo

MCP server: `HA-Furubo`

This file contains specific knowledge for the home "Furubo".

## Common Task Workflows
- **Status Check:** Use `ha_get_overview` to fetch current domain stats (temperature, motion, connectivity).
- **Control:** The controllable devices are primarily `media_player` (TVs) and `switch` (Smart Plugs).
- **Monitoring:** Heavily reliant on BLE sensors (temperature, motion, toothbrush) and network/router status.

## Key Facts
- Location: Furubo
- Features: Router monitoring, BLE sensors, TV media players, smart plugs.

## Motion & BLE Sensors
- Motion sensor active status: `automation.motion_sensor_active`
- Motion sensor last update (datetime): `input_datetime.motion_sensor_last_update`
- BLE Sensors: Temperature, Humidity, RSSI, Battery, Motion (IDs start with `ble_`)

## Media Players
| Friendly name | Entity ID |
|--------------|-----------|
| Samsung AU9075 43 TV | `media_player.samsung_au9075_43_tv` |
| Telia TV | `media_player.telia_tv` |

## Switches (Smart Plugs)
| Friendly name | Entity ID |
|--------------|-----------|
| Plug Vardagsrum | `switch.plug_vardagsrum` |
| Plug 3 | `switch.plug_3` |

## Automations
- `motion sensor active`
