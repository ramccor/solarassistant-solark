# 07 — Worked example: two inverters, one twelve-pack stack

[Index](README.md) · Prev: [06 — Troubleshooting](06-troubleshooting.md) · Next: [08 — Recommended settings](08-recommended-settings.md)

A complete as-built record for a real installation, showing how the generic rules
resolve into concrete quantities and settings. Use it as a template for your own
baseline ([page 05](05-verification.md#recording-a-baseline)).

The screenshots throughout this guide were captured from this installation. Identifying
values — hostname, site owner, serial numbers, IP addresses, WiFi SSID, site location —
are shown as `[REDACTED]` in both the images and the tables below, so the whole guide
can be distributed as-is.

Fill the redacted fields in from your own site when you use this as a baseline template.

## Site scale

| Quantity | Count |
|----------|-------|
| SolarAssistant sites | 1 |
| Sol-Ark 15K inverters | 2 |
| Pytes V5 stacks | 1 (12 packs) |

## Resulting order

| Scope | Item | Qty | Line total |
|-------|------|-----|-----------|
| Per site | [Device with software (Pi 5)](https://solar-assistant.io/shop/products/device_rpi5) | 1 | $229 |
| Per inverter | [RJ45 splitter](https://solar-assistant.io/shop/products/deye_rj45_split) | 2 | $28 |
| Per inverter | [Sol-Ark RS485 cable](https://solar-assistant.io/shop/products/sunsynk_rs485) | 2 | $58 |
| Per stack | [Pytes console cable](https://solar-assistant.io/shop/products/pytes_rs232) | 1 | $29 |
| | | | **$344** |

USB ports required: 2 inverters + 1 stack = **3 of 4**. Fits the Pi directly with one
port spare — no hub needed. A third inverter would still fit; a fourth would require a
powered USB hub.

## Host

| Item | Value |
|------|-------|
| Site ID | `[REDACTED]` |
| Location | `[REDACTED]` |
| Local URL | `[REDACTED]` (wlan0; eth0 down) |
| Board | Raspberry Pi 5 Model B Rev 1.0 (`rpi64`) |
| Software version | 2026-07-27 |
| Storage | 28% of 16 GB |
| Localization | English, America/Chicago |
| Temperature unit | °Fahrenheit |
| Energy totals reset | Weekly |
| Scheduled reboot | Never |
| SSH | Disabled |
| Remote proxy | North America |
| MQTT broker | **Enabled** (port 1883), Home Assistant auto-discovery on, `Allow setting changes` Disabled |

## Adapters

| USB ID | Part | Assigned to |
|--------|------|-------------|
| `0403:6001` | FT232R | Inverter RS485 (USB0) |
| `0403:6001` | FT232R | Inverter RS485 (USB2) |
| `0403:6015` | FT231X | Pytes console (USB1) |

SolarAssistant Devices panel: Inverter `Deye, SunSynk, Sol-Ark` on **USB0 + USB2**;
Battery `USB PylonTech/Pytes console` on **USB1**. Solar PV rated power 34 440 W.

**Solar array:** 84 × Trina 410 W bifacial (black-on-black) = **34.44 kW DC** — 42 per
inverter, 14 per MPPT across 3 MPPTs, DC:AC ratio 1.15. Rated power is entered as the
front-side STC nameplate; bifacial rear-side gain is not modelled by the forecast.

## Inverters

| SolarAssistant name | Serial | Parallel role | Modbus № | Max AC | MPPTs |
|---------------------|--------|---------------|----------|--------|-------|
| Inverter 1 | `[REDACTED]` | Slave | 2 | 15.0 kW | 3 |
| Inverter 2 | `[REDACTED]` | **Master** | 1 | 15.0 kW | 3 |

Both report protocol version 2.1, MCU 7228, COMM 1452.

> This site is the concrete case of the numbering gotcha from
> [00 — Overview](00-overview.md): SolarAssistant's "Inverter 1" is the Sol-Ark
> **slave** on Modbus 2, and "Inverter 2" is the **master** on Modbus 1.

### Inverter-side settings (identical on both units)

| Group | Setting | Value |
|-------|---------|-------|
| Battery | Type | Lithium |
| Battery | Lithium protocol | **CAN (protocol 0)** |
| Battery | Operation | State of charge |
| Battery | Capacity | 1200 Ah |
| *Advanced* | Battery capacity fallback | 61.4 kWh |
| *Advanced* | PV temperature coefficient / NMOT | −0.29 %/°C / 43.0 °C |
| *Advanced* | PV tilt / azimuth | 32.1° / 0° (due south) |
| Charging | Max charge current | 225 A |
| Charging | Max discharge current | 275 A |
| Charging | Max grid charge current | 150 A |
| Charging | Max generator charge current | 71 A |
| Charging | Float / absorption / equalization | 56.8 V |
| Grid | Type | 120/240 V two phase |
| Grid | Frequency | 60 Hz (limits 55.0–65.0 Hz) |
| Grid | Voltage limits | 185–265 V |
| Grid | Peak shaving | Disabled (8.00 kW) |
| Auxiliary | Aux port | Generator input |
| Auxiliary | Generator connected to grid input | Enabled |
| Auxiliary | Generator start / stop capacity | 50% / 90% |
| Work mode | Mode | Zero export to load |
| Work mode | Energy pattern | Battery first |
| Work mode | Max sell power | 9.00 kW |
| Work mode | Max solar power | 16.5 kW |
| Work mode | Grid charge | Enabled |
| Work mode | Output shutdown capacity | 15% |
| Work mode | Stop / start battery discharge | 20% / 25% |
| Work mode | Start grid charge capacity | 35% |

> These are commissioning values for one particular site, not recommendations. Charge
> voltages, current limits, and SOC thresholds must match your own battery
> specification and site design.

## Battery stack

| Property | Value |
|----------|-------|
| Packs | 12 × `E-BOX-48100V-D` |
| Total capacity | 1200 Ah |
| BMS firmware | `SPBMS16SRPV1.10.24.C16 (24-11-27)` — uniform across all packs |
| Protocol reported | `V2P` |
| Per-pack serial numbers | `[REDACTED]` × 12, all distinct |
| Per-pack max current | 101 A charge / −101 A discharge |
| Observed bank voltage at 100% SOC | ~54.9 V |
| Observed cell imbalance at 100% SOC | 0.008–0.013 V |

## Snapshot at capture time

Conditions when the screenshots were taken, for context when reading them:

| Reading | Value |
|---------|-------|
| Device mode | Discharge above 50% |
| Load | 2.28 kW (1.13 + 1.15 kW) |
| Solar PV | 2.40 kW (1.19 + 1.20 kW), across 3 MPPTs per inverter |
| Battery | 100% SOC, 54.9 V, −198 W |
| Grid | Absent — 0 W, 0 Hz |

**This site runs off-grid**, so grid-absent is the normal steady state rather than a
fault or an outage. The grid-related inverter settings recorded above (voltage and
frequency limits, grid charge, peak shaving) are still present in the inverter's
configuration, but the grid input is not normally energised. See
[06 — Troubleshooting](06-troubleshooting.md#things-that-are-not-faults).

---

Next: [08 — Recommended settings](08-recommended-settings.md)
