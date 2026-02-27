# Home Assistant — Palaistina

MCP server: HA-Palaistina

Activated when Gustav says: "Palaistina" or "landet"

## Key Facts

- Total entities: 981
- Total domains: 29
- Location name: "Palaistina"

### Latest Motion Activity Check

To find the last time a motion sensor detected activity (state became "on"):
1. Identify the relevant motion sensor entity ID (e.g., `binary_sensor.signify_netherlands_b_v_sml003_occupancy` for living room, `binary_sensor.rorelsesensor_utekallaren_occupancy_2` for utekällaren).
2. Determine a suitable `start_time` (e.g., two weeks back from current date).
3. Use `mcporter call "HA-Palaistina.ha_get_history(entity_ids: [\"<ENTITY_ID>\"])"` with the calculated `start_time`.
4. Iterate through the `states` list in the tool's output to find the *most recent* entry where `"state": "on"`.
5. Extract the `last_changed` timestamp from that specific `"on"` state entry.
6. Adjust the timestamp to local timezone (GMT+1).

## Known Entity IDs (Populate this section as entities are discovered)

### Lights
- **Count:** 23
- **Examples:**
  - `Spot 1 loftet`
  - `Soffa 2`
  - `Hemma`
  - `Tak 2 hallen`
  - `Hall`
  - `Diskbänken`
  - `Trappan`

### Sensors
- **Count:** 592
- **Examples:**
  - `nordpool_mwh_se3_eur_0_10_0`
  - `VVM 310, 3x400V Add. heat (BT63)`
  - `activated`
  - `AP3-iPad-D2P29X799V SSID`
  - `Sam – iPhone Audio Output`
  - `motion_sensor_last_update`
  - **Rörelsesensor (vardagsrummet):** Fysisk enhet (Signify Netherlands B.V. SML003)
    - Rörelse: `binary_sensor.signify_netherlands_b_v_sml003_occupancy` (Senaste aktivitet: se `last_changed`)
    - Temperatur: `sensor.signify_netherlands_b_v_sml003_temperature`
    - Ljusstyrka: `sensor.signify_netherlands_b_v_sml003_illuminance`
    - Batteri: `sensor.signify_netherlands_b_v_sml003_battery`

### Switches
- **Count:** 24
- **Examples:**
  - `Palaistina Crossfade`
  - `Automation: Dimmer allt`
  - `Rörelsesensor utekällaren LED trigger indicator`
  - `Sjöstugan Aqara smart plug Power outage memory`
  - `Home Assistant Cloud Google Assistant state reporting`

### Automations
- **Count:** 8
- **Examples:**
  - `Meddelande rörelsesensor vardagsrummet`
  - `Meddelande rörelsesensor utekällaren`
  - `Temperature Control Holken Auto`
  - `Temperature Control Sjostugan Auto`
  - `Telegram - Respond to @Mention`
  - `Daily House Health Check`