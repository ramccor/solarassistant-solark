# SolarAssistant — Sol-Ark 15K + Pytes V5 Configuration Guide

How to configure SolarAssistant to monitor any number of parallel **Sol-Ark 15K**
inverters over RS485 and one or more **Pytes V5** battery stacks over the RS232
console port.

The guide is written for any site. Quantities scale from the three rules below;
[07 — Worked example](07-worked-example.md) shows a real two-inverter, twelve-pack
build end to end.

Read the pages in order. Pages 02 and 03 involve working inside a live inverter
enclosure — read [00-overview](00-overview.md) first.

| # | Page | What it covers |
|---|------|----------------|
| 00 | [Overview and topology](00-overview.md) | What talks to what, and why the wiring is shaped this way |
| 01 | [Hardware and ordering](01-hardware-and-ordering.md) | The purchase rules, with solar-assistant.io order links |
| 02 | [Wiring the Sol-Ark 15K inverters](02-wiring-solark.md) | 2-in-1 BMS port, RJ45 splitter, one RS485 cable per inverter |
| 03 | [Wiring the Pytes V5 stack](03-wiring-pytes.md) | Console cable to the master pack |
| 04 | [SolarAssistant configuration](04-solarassistant-config.md) | Driver selection and port assignment |
| 05 | [Verification](05-verification.md) | How to prove every device is actually being read |
| 06 | [Troubleshooting](06-troubleshooting.md) | Symptom-to-cause table |
| 07 | [Worked example](07-worked-example.md) | A complete as-built two-inverter, twelve-pack site, plus a three-inverter order |
| 08 | [Recommended settings](08-recommended-settings.md) | Optional post-install changes: MQTT/Home Assistant, battery capacity fallback, PV forecast |
| 09 | [Sol-Ark ↔ SolarAssistant terminology](09-terminology-mapping.md) | What each MySolArk field is called in SolarAssistant, and where the two disagree |

## End-user runbook (standalone)

Not part of the page sequence or the decks. Written for someone with no electrical
background: each page opens with the hard safety rules, a "what you see → what to do"
table, and numbered procedures with "if not →" branches; technician detail is split out into
a separate appendix, with a pointer at the end of each page. Lights and buttons are named by printed label
and behaviour, never by color alone. Each page has a US-letter PDF alongside it
(`cheatsheet-<name>.pdf`), built with `python3 build-cheatsheets.py` (python-markdown +
headless Chrome). Figures clipped from the source manuals live in `images/cheat-*.png`.

| Page | What it covers |
|------|----------------|
| [Start here](cheatsheet-00-runbook-index.md) | Symptom index across all pages, who to call, where things are |
| [Batteries](cheatsheet-low-battery.md) | Reading pack lights, low battery, power out, a pack that shut itself off, safe power-up order |
| [Generator](cheatsheet-generator.md) | Forcing a run, won't start, overload, stopping, portable generator on the GEN inlet, cold-weather checks, service parts |
| [Inverter failed](cheatsheet-inverter-failure.md) | Which one failed, ordered restart, running on one inverter, master failure and promotion (installer-gated) |
| [Solar panels](cheatsheet-array-maintenance.md) | Wash, snow/ice, seasonal tilt, MPPT at 0 V, panel replacement, storm check |
| [Maintenance calendar](cheatsheet-maintenance-calendar.md) | Month-by-month tasks with parts lists, the mid-October generator inlet check, stock to keep on hand |
| [Technician appendix](cheatsheet-99-technician-appendix.md) | The reference material behind each page — setpoints, fault codes, specs, service parts, technician-only procedures — split out so the end-user binder stays thin |

## Site-specific notes (not for distribution)

[site-pnc-home.md](site-pnc-home.md) holds the as-built values, datasheet figures, applied
SolarAssistant settings and the PVGIS tilt analysis for one particular site. It contains
that site's coordinates and hostname, is not part of the guide proper, and is not
referenced from either slide deck. Leave it out when handing the guide to an installer.

## Presentation deck

There are two [Marp](https://marp.app) decks, both 49 slides, for briefing an installer on
a screen rather than having them read the reference pages. Both close with an *After the
install* section mirroring [page 08](08-recommended-settings.md) and the key naming pairs
from [page 09](09-terminology-mapping.md).

| Deck | Use it when |
|------|-------------|
| [`slides.md`](slides.md) | The installer may source their own cables, or you want the electrical detail |
| [`slides-simple.md`](slides-simple.md) | **Every cable and the splitter are ordered from the solar-assistant.io shop** |

The simplified deck drops the RJ45 pinout table, the pin-level splitter diagram, and the
cable-substitution material, on the assumption that buying the shop parts removes that
entire class of problem. Nothing in it asks the installer to identify a pin or verify a
conductor. It is not a subset of the full deck — several slides are rewritten rather than
removed, so **edits to shared content must be made in both files.**

| File | Use |
|------|-----|
| `slides.md` / `slides-simple.md` | Source; edit these |
| `slides.pdf` / `slides-simple.pdf` | Hand out or present |
| `slides.html` / `slides-simple.html` | Present in a browser |

Rebuild after editing either source:

```bash
marp slides.md --pdf  -o slides.pdf  --allow-local-files
marp slides.md --html -o slides.html --allow-local-files

marp slides-simple.md --pdf  -o slides-simple.pdf  --allow-local-files
marp slides-simple.md --html -o slides-simple.html --allow-local-files
```

The deck is a *walkthrough*; the numbered pages remain the reference. Pinout tables and
the troubleshooting matrix are easier to scan on a page than on a slide.

## Purchase rules

Everything you need follows from three rules:

| Scope | Item | Quantity | Unit |
|-------|------|----------|------|
| **Per site** | [Device with software (Raspberry Pi 5)](https://solar-assistant.io/shop/products/device_rpi5) | 1 | $229 |
| **Per Sol-Ark 15K** | [Deye/SunSynk/Sol-Ark RJ45 splitter](https://solar-assistant.io/shop/products/deye_rj45_split) | 1 each | $14 |
| **Per Sol-Ark 15K** | [Sol-Ark RS485 USB cable](https://solar-assistant.io/shop/products/sunsynk_rs485) | 1 each | $29 |
| **Per Pytes V5 stack** | [Pytes console USB cable](https://solar-assistant.io/shop/products/pytes_rs232) | 1 each | $29 |

```
Total = $229 + ($43 × inverters) + ($29 × battery stacks)
```

> **Sites with more than 3 inverters also need a separate powered USB hub.** The Pi 5
> has four USB ports; three inverters plus one battery stack fills all four. See the
> [USB port budget](01-hardware-and-ordering.md#the-usb-port-budget).

Full breakdown, worked totals, and the USB port budget:
[01 — Hardware and ordering](01-hardware-and-ordering.md).

## The two rules that catch people out

- **Inverters do not share a cable.** Each Sol-Ark needs its own RS485 cable into its
  own USB port. Parallel inverters are not daisy-chained on the RS485 side.
- **Battery packs do share a cable.** One console cable reads an entire stack,
  whether that stack is two packs or twelve.

---

Screenshots throughout are from a live installation and show what each screen should
look like. Identifying values — hostname, site owner, serial numbers, IP addresses,
WiFi SSID, site location — appear as `[REDACTED]` in every image and on
[page 07](07-worked-example.md).

**The complete guide, pages 00–09, is safe to distribute as-is.**
