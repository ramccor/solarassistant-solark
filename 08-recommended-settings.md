# 08 — Recommended settings

[Index](README.md) · Prev: [07 — Worked example](07-worked-example.md)

Three optional changes that get more out of a working install. **None is required** —
the system in pages 00–06 is complete and correct without them. Skip this page until
verification passes.

## Where each change lives, and what it costs

| Change | Page | Requires Disconnect? |
|--------|------|----------------------|
| MQTT + Home Assistant | `Configuration → MQTT` | No |
| Battery capacity fallback | `Configuration → Advanced` | **Yes** |
| PV forecast inputs | `Configuration → Advanced` | **Yes** |

The Advanced page is read-only while the system is connected — it prints *"Disconnect
on Configuration page to make changes below"* and greys out every field. Disconnecting
stops data collection until you reconnect.

> **Batch the two Advanced-page changes into a single maintenance window.** They live on
> the same page, so doing them together costs one collection gap instead of two. The
> MQTT page stays editable while connected and needs no gap.

---

## 1. Enable MQTT and Home Assistant discovery

The single biggest gain if you run Home Assistant. SolarAssistant's MQTT broker is
**disabled by default**, and its built-in Home Assistant auto-discovery will publish
every metric it collects — per inverter and per battery pack — as HA entities with no
manual entity definitions.

That buys long-term history, alerting, and dashboards beyond what SolarAssistant
retains locally.

### Settings

| Field | Set to | Notes |
|-------|--------|-------|
| Topic prefix | leave at default (`solar_assistant`) | Every published example assumes it; changing it means rewriting topic paths for no gain |
| Allow setting changes | **Disabled** | See warning below |
| HomeAssistant → Unique ID | a short, stable site slug | Set once; treat as permanent |
| HomeAssistant → Auto discovery | **Enabled** | The reason to do any of this |
| Authentication → Username | set one | |
| Authentication → Password | set a long random one | |

Then start the broker: **`Configuration` → MQTT Broker → Start**. The MQTT page only
configures the broker; it does not start it.

### Two things to get right

> **`Allow setting changes` grants write control over your inverters.** Enabled, anything
> that can publish to the broker can change work mode, charge currents, and generator
> control. Leave it **Disabled** unless you specifically intend to automate the
> inverters — and if you do, enable it only after authentication is set, and never with
> the broker reachable from outside the LAN.

> **`Unique ID` is effectively permanent.** It namespaces entities so multiple
> SolarAssistant sites can share one Home Assistant. Changing it later re-creates every
> entity under new IDs, orphaning history and dashboards. Set it before first connection
> even on a single-site install — it costs nothing now and avoids a migration later.

The broker listens on port 1883 in plaintext, with no TLS. The password protects
against casual access on the LAN; it does not protect against traffic capture. Keep the
port on the LAN and do not forward it.

### Before you start — check your existing broker

SolarAssistant runs **its own** broker. There is no field to publish to an external
one, so Home Assistant connects *to* the Pi, not the other way round.

If Home Assistant already uses a broker such as Mosquitto, confirm your HA version
supports more than one MQTT connection before committing — historically it supported
only one, in which case you would either repoint HA at SolarAssistant's broker or
bridge the two brokers. Check this first; it is awkward to discover mid-setup.

---

## 2. Correct the battery capacity fallback

`Configuration → Advanced → Battery → Capacity kWh`

This field commonly holds a **single-pack** figure. In a multi-pack bank that is wrong
by the pack count — a twelve-pack bank left at a one-pack default reads twelve times
low.

### The value to enter

```
Capacity kWh = number of packs × per-pack kWh

per-pack kWh = nominal pack voltage × pack amp-hours ÷ 1000
```

A 51.2 V / 100 Ah pack is 5.12 kWh, so twelve of them are 61.4 kWh. Use your pack
datasheet; if it quotes a *usable* rather than nameplate figure, decide which convention
you want and apply it consistently.

### Why bother when it is dormant

The field's own hint says it is *"only used when not readable from battery or
inverter."* On a healthy install capacity **is** readable, so the value does nothing.

It goes live at exactly the wrong moment — when the console cable drops or the battery
driver disconnects. From then on every energy figure derived from state of charge is
computed against the wrong capacity. A full bank can read as nearly empty. The number
only ever surfaces while you are already troubleshooting, and when it does it actively
misleads.

> **Risk: none.** This is a display fallback, not a control parameter. Charge and
> discharge behaviour comes from the inverter settings and from the BMS over CAN.
> Nothing here reaches the battery.

---

## 3. Set the PV forecast inputs

`Configuration → Advanced → Solar PV`

These determine forecast accuracy. On a grid-tied site the forecast is decoration; **on
an off-grid site it is operational** — it is the input to "do I run the generator
tonight" and "can I defer that load to tomorrow." A forecast of the wrong shape gives
confidently wrong planning information.

| Field | Source |
|-------|--------|
| Latitude / Longitude | Site coordinates — usually already correct |
| Tilt | The array's actual angle: racking angle for ground mounts, roof pitch for roof mounts |
| Azimuth | The array's actual bearing |
| Temperature Coefficient (Pmax) | Module datasheet |
| NMOT | Module datasheet |

**Azimuth convention:** `0` is **due south**, with negative values east of south and
positive values west; `180`/`−180` is north. Tilt runs `0`–`90`, where `0` is pointing
straight up and `90` is pointing at the horizon. Both are per
[SolarAssistant's PV forecast help page](https://solar-assistant.io/help/dashboard/pv_forecast).

A stored `0` is therefore a legitimate value for a south-facing array, not a
placeholder — verify it against the physical array rather than assuming it needs
changing.

> **Do not carry an azimuth over from other solar software without converting it.**
> Compass-bearing tools — pvlib's `surface_azimuth`, PVWatts, Home Assistant's sun
> integration — put `0` at **north** and south at `180`. SolarAssistant follows the
> forecast.solar convention instead. Applying a compass bearing here points a
> south-facing array due north and inverts the forecast curve.

**Typical datasheet ranges,** useful for spotting a value that was never updated:
temperature coefficient −0.29 to −0.40 %/°C (newer N-type modules sit at the low end,
older mono PERC nearer −0.34 to −0.40); NMOT 41–45 °C.

**One field lives elsewhere.** `Configuration → Solar PV → Rated power (W)` must be the
**DC nameplate sum** of installed panels, not an AC figure. The forecast scales linearly
from it.

### Validating rather than guessing

Compare predicted against actual over two or three clear-sky days. The error pattern
identifies the field:

| Symptom | Likely culprit |
|---------|----------------|
| Consistently over- or under-predicts by a fixed ratio | Rated power |
| Peak arrives earlier or later than predicted | Azimuth |
| Accurate in one season, poor in the other | Tilt |
| Accurate in the morning, drifts high in afternoon heat | Temperature coefficient |

> **Multi-orientation arrays.** SolarAssistant accepts one tilt and one azimuth, and
> [does not support strings facing different directions](https://solar-assistant.io/help/dashboard/pv_forecast).
> Where they do, enter the **average facing direction**, weighted by each group's rated
> power if the split is uneven. No single pair can describe such an array, so accept
> that the curve shape will never be exact.

> **Seasonally adjusted racking.** If the array is tilted twice a year, the stored tilt
> must change with it — the forecast has no seasonal model and will be wrong for half the
> year otherwise. For a mid-latitude site (roughly 30–40° N) the usual schedule is
> **latitude − 15° to −20° from spring to early autumn** and **latitude + 15° to +20°
> for the rest of the year**; PVGIS modelling puts the annual gain at around **4–5 %**
> over a fixed latitude tilt, concentrated in the winter months that drive generator
> runtime on an off-grid site. Four adjustments a year add well under 1 % more and are
> rarely worth the labour. Bifacial modules on an open ground mount gain a little extra
> from the steeper winter angle. Put the two tilt values and switch dates on the site
> record so whoever adjusts the racking also updates this field.

> **Risk: none.** These inputs feed prediction only. They do not affect MPPT behaviour,
> charge control, or anything the inverters or BMS act on.

---

## Leave these alone

Settings on the same pages that look adjustable but are already correct on a working
install:

| Setting | Correct value | Why |
|---------|---------------|-----|
| Battery → Read current from | `Battery` | The `Inverter` option is for banks where **only the master pack** is readable. If every pack enumerates, `Battery` is right |
| Inverter → MPPT connections | `Auto detect` | Correctly finds the inverter's actual MPPT count |
| Inverter → Grid connection / Grid multiplier | `Auto detect` | |
| Inverter → Allow passive reading | `Yes` | Harmless on a dedicated RS485 line; it matters only where the monitoring port is shared with a WiFi dongle |
| Grid → Provider | `Default` | Tariff providers are irrelevant off-grid, and on-grid only if you want price data |

---

## Order of work

1. Verify the install first — [05 — Verification](05-verification.md)
2. MQTT and Home Assistant (no Disconnect needed)
3. Open a maintenance window: **Disconnect**
4. Battery capacity fallback
5. PV forecast inputs
6. **Connect**, then confirm both devices return to Connected
7. Re-check [page 05](05-verification.md) — column count, pack count, capacity

---

Next: [09 — Sol-Ark ↔ SolarAssistant terminology](09-terminology-mapping.md)
