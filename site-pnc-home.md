# Site notes — `pnc-home`

> **Site-specific — not for distribution.** This page records the as-built values and
> analysis for one installation. It contains the site's coordinates and hostname and is
> deliberately excluded from the generic guide and from both slide decks. Hand out pages
> 00–09 and the decks; keep this one.

## Site summary

| Item | Value |
|------|-------|
| SolarAssistant | `https://pnc-home.us.solar-assistant.io` (renamed from `farmhome`, 2026-08-22) |
| Location | ~35.65° N, 88.13° W (west Tennessee) |
| Site type | Off-grid; **Wildcat Patriot 40 kW** (Hyundai, EPA Tier 4F, DSE 6110 MKIII controller) prime-power towable diesel — **36 kW / 150 A at 120/240 V single-phase**, which is the installer's "35 kW" — on the GRID inputs via a colour-coded wall box; two-wire start on the master's pins 7 & 8. 50 A outdoor receptacle for a portable 240 V generator (≤12 kW) on the **GEN** inputs |
| Inverters | 2 × Sol-Ark 15K-2P in parallel |
| Battery | 12 × Pytes V5 = 61.4 kWh |
| Array | 84 × Trina TSM-NE09RC.05 **410 W** bifacial, black-on-black = **34.44 kW DC** |
| Strings | 42 panels per inverter; 14 per MPPT across 3 MPPTs (2 strings × 7 in series) |
| Racking | 3 × **Sinclair Designs adjustable-tilt** ground mounts, currently **32.1°**, azimuth **0°** (due south); clamp torque 20 ft-lb |
| PV disconnects | Midnite combiner at the end of each array (one 600 V breaker per 14 panels) → wall disconnect → inverter PV switch |
| Installer | Mainstream Green Solutions, Lexington TN |
| DC:AC | 1.15 |

## Module datasheet — 410 W column

Source: `Trina-NE09RC-05-Datasheet-DS.pdf` (TSM_NA_2023_BV3). The sheet covers the
400–425 W range; these are the **410 W** values.

| Parameter | STC | NOCT (800 W/m², 20 °C) |
|-----------|-----|------------------------|
| Pmax | 410 W (0 / +5 W) | 312 W |
| Vmpp / Impp | 42.1 V / 9.73 A | 39.3 V / 7.93 A |
| Voc / Isc | 50.1 V / 10.37 A | 47.5 V / 8.36 A |
| With 10 % rear irradiance | 437 W, Impp 10.36 A, Isc 11.04 A | — |

Common to all bins: Pmax coefficient **−0.30 %/°C**, Voc −0.25 %/°C, Isc +0.04 %/°C,
NOCT **43 ±2 °C**, bifaciality 65 ±10 %, 1762 × 1134 × 30 mm, 21.8 kg, 6000 Pa front /
4000 Pa rear, 20 A max series fuse, 1500 V max system.

**Cold-weather string check.** Voc at −20 °C ≈ 50.1 × (1 + 0.0025 × 45) = **55.7 V**.
7 in series = 390 V; 8 = 446 V; 9 = 502 V — over the Sol-Ark's 500 V limit. The as-built
7-series strings are fine. Per-MPPT current at bifacial Impp: 2 × 10.36 = 20.7 A, within
the 26 A/MPPT rating.

## Inverter / generator setpoints (installer's training deck, as delivered)

| Setting | Value |
|---|---|
| Generator auto-start | **35 % SOC** |
| Sol-Ark Shutdown | **15 %** |
| Emergency floor for Start % | 11 % — only if the generator will not start |
| Max Gen Runtime | **150 min** (firmware 7228+) |
| Generator stop | 95 % SOC or Max Gen Runtime, whichever first; charge tapers above 90 % |
| Battery warranty | no routine discharge below 10 % |
| Pytes sleep point | below ~5 %, with reserve for a 51.2 V force charge |
| Initial diesel fill | 115 gal, anti-gel treated; add anti-gel to every fill before winter |
| Sump heater + built-in starting-battery charger | Both fed from the generator's 120 V NEMA 5-15 inlet; heater 1000–1500 W, runs near freezing. That inlet must stay powered in winter. |
| Starting-battery maintainer | **Battery Tender Plus 12 V / 1.25 A** (Deltran 022-0185G-DL-WH) on the generator battery; green steady = floated. ~20 W. |
| Fuel burn (manual) | 3.6 gal/h full load, 2.0 gal/h at 50 % — a 150 min charge run is roughly 5–9 gal |
| Firmware | updated by Sol-Ark; auto-gen-start programmed, tested and working (deck dated 6/18/26) |

These are what the installer set; cross-check against MySolArk before relying on them.

## SolarAssistant settings as applied

| Setting | Value | Changed |
|---------|-------|---------|
| `Configuration → Solar PV → Rated power` | 34 440 W | 2026-08-12 (was 24 000) |
| `Advanced → Battery → Capacity kWh` | 61.4 | 2026-08-12 (was 4.8) |
| `Advanced → PV → Latitude / Longitude` | 35.64979 / −88.1267 | unchanged |
| `Advanced → PV → Tilt / Azimuth` | 32.1° / 0.0° | unchanged |
| `Advanced → PV → Temperature Coefficient (Pmax)` | **−0.30 %/°C** | 2026-08-22 (−0.29 set 2026-08-12; corrected to datasheet) |
| `Advanced → PV → NMOT` | 43.0 °C | 2026-08-12 (was 41) |
| MQTT broker / HA discovery | Enabled, port 1883, ID `farmhome`; setting changes **disabled** | 2026-08-12 |

Editing `Advanced` fields requires **Disconnect** on the Devices panel first; a **Save**
button appears under the Solar PV block only after a value changes. Reconnect afterwards
and confirm `/inverter/status` is showing live watts. The 2026-08-22 edit paused
monitoring for about 2½ minutes.

## Tilt analysis (PVGIS v5.2, 2026-08-22)

Inputs: 34.44 kW DC, 14 % system loss, due south, site coordinates above. PVGIS models
the **front side only**; the bifacial rear gain is extra and favours the steeper tilts.

### Fixed tilt

PVGIS's own optimiser lands on **32°** — the existing 32.1° racking is already the
annual optimum.

| Tilt | kWh/yr | vs 32.1° | Dec | Jan | Jun | Jul |
|------|--------|----------|-----|-----|-----|-----|
| 20° | 47 330 | −1.8 % | 2 439 | 2 819 | 4 993 | 4 936 |
| **32.1°** | **48 189** | — | 2 784 | 3 181 | 4 689 | 4 677 |
| 36° | 48 131 | −0.1 % | 2 871 | 3 270 | 4 563 | 4 570 |
| 42° | 47 714 | −1.0 % | 2 981 | 3 382 | 4 344 | 4 376 |
| 50° | 46 517 | −3.5 % | 3 085 | 3 482 | 3 992 | 4 056 |

Winter-biasing a *fixed* array to 42° buys ~200 kWh in each of Dec/Jan for ~300 kWh
lost in each of Jun/Jul — net −1 %/yr.

### Seasonal adjustment

| Schedule | Positions | kWh/yr | vs fixed 32.1° |
|----------|-----------|--------|----------------|
| 2 switches | 10° Apr–Aug, 50° Sep–Mar | 50 392 | +2 204 (+4.6 %) |
| 2 switches, winter-biased | 10° Apr–Sep, 55° Oct–Mar | 50 324 | +2 136 (+4.4 %) |
| 4 switches | 10° May–Aug, 30° Mar–Apr, 56° Oct–Feb, 32° Sep | 50 684 | +2 496 (+5.2 %) |
| Monthly (upper bound) | 12 adjustments | 50 830 | +2 642 (+5.5 %) |

Two switches capture ~88 % of what four do; the extra two adjustments are worth
~290 kWh/yr (0.6 %) — noise against weather.

10°/50° vs 10°/55°, month by month (kWh):

| | Fixed 32.1° | 10°/50° | 10°/55° |
|---|---|---|---|
| Jan | 3 178 | 3 482 | **3 516** |
| Feb | 3 227 | 3 376 | 3 371 |
| Mar | 3 995 | 3 943 | 3 876 |
| Apr–Aug | 23 215 | 24 416 | 24 416 |
| Sep | 4 090 | 3 944 | 3 850 |
| Oct | 4 163 | 4 292 | 4 268 |
| Nov | 3 539 | 3 853 | **3 884** |
| Dec | 2 781 | 3 085 | **3 124** |

55° gives up ~90 kWh/yr overall but moves ~35–40 kWh/month from the shoulder months into
Nov–Jan, which is where generator hours come from on this site.

### Recommendation

| | Angle | Switch |
|---|---|---|
| Summer | **15°** (10° is the front-side optimum, but 15° keeps some rear-side gain and sheds rain; the yield difference is negligible) | early **April** |
| Winter | **55°**, or the rack's maximum if lower | early **October** |

Expected: ~+4.5 % front-side annually vs fixed 32°, with Nov–Jan each up ~10–12 %, and
more once rear-side gain is counted. Checks before committing: the racking's stated tilt
range and wind-load rating at 55° (the modules themselves are rated 6000/4000 Pa — the
rack is the limit, not the panels).

**Every time the racking is adjusted, update `Advanced → PV → Tilt` in SolarAssistant to
match.** The forecast has no seasonal model; left at 32.1° it will be wrong for half the
year. Requires Disconnect → edit → Save → Connect as described above.
