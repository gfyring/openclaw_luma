# Home Assistant — Furubo

MCP server: HA-Furubo

Activated when Gustav says: "Furubo"

## Key Facts

- Total entities: 380
- Total domains: 19
- Location name: "Furubo"

### Latest Motion Activity Check

To find the last time a motion sensor detected activity (state became "on"):
1. Identify the relevant motion sensor entity ID (e.g., `binary_sensor.motion_sensor_occupancy`).
2. Determine a suitable `start_time` (e.g., two weeks back from current date).
3. Use `mcporter call "HA-Furubo.ha_get_history(entity_ids: [\"<ENTITY_ID>\"])"` with the calculated `start_time`.
4. Iterate through the `states` list in the output to find the *most recent* entry where `"state": "on"`.
5. Extract the `last_changed` timestamp from that specific `"on"` state entry.
6. Adjust the timestamp to local timezone (GMT+1).

## Known Entity IDs (Populate this section as entities are discovered)

### Lights
(No traditional light entities found in this instance's domain overview.)

### Sensors
- **Count:** 281
- **Examples:**
  - `ble temperature E4D32C0EF02F`
  - `ble steps CB6919D57BEB`
  - `Zigbee2MQTT Bridge Version`
  - `AP3-iPhone-D76Q377LC7 Average Active Pace`
  - `ble humidity 48872D800B19`
  - `motion sensor Occupancy`
  - **Rörelsesensor:** (Fysisk enhet märkt som "motion sensor")
    - Rörelse: `binary_sensor.motion_sensor_occupancy` (Senaste aktivitet: se `last_changed`)
    - Temperatur: `sensor.motion_sensor_temperature`
    - Ljusstyrka: `sensor.motion_sensor_illuminance`
    - Batteri: `sensor.motion_sensor_battery`
    - Spänning: `sensor.motion_sensor_voltage`

### Switches
- **Count:** 14
- **Examples:**
  - `shellyplugsg3-8cbfea939e00 Switch 0`
  - `plug_vardagsrum LED disabled night`
  - `Zigbee2MQTT Bridge Permit join`

### Automations
- **Count:** 1
- **Entities:**
  - `motion sensor active`