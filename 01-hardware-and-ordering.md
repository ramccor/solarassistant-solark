# 01 — Hardware and ordering

[Index](README.md) · Prev: [00 — Overview](00-overview.md) · Next: [02 — Wiring the Sol-Ark](02-wiring-solark.md)

## The purchase rules

Three rules determine everything you order:

### Per SolarAssistant site — 1 ×

| Item | Price | Order page |
|------|-------|------------|
| **Device with software** (Raspberry Pi 5) | $229 | [solar-assistant.io/shop/products/device_rpi5](https://solar-assistant.io/shop/products/device_rpi5) |

One device per monitoring site. Ships fully assembled: Raspberry Pi 5 (2 GB), SanDisk
High Endurance SD card, aluminium enclosure with cooling, ML-2020 rechargeable cell for
the real-time clock, and a power supply — either a 9–60 V DC USB supply on a 2.5 m
cable, or the official Pi 3 A mains supply. The **software licence is included and
perpetual**; there is no monthly fee, and the unit runs without internet.

**No comms cables are included.** Every cable below is ordered separately.

### Per Sol-Ark 15K inverter — 1 × each

| Item | Price | Order page |
|------|-------|------------|
| **Deye/SunSynk/Sol-Ark RJ45 splitter** | $14 | [solar-assistant.io/shop/products/deye_rj45_split](https://solar-assistant.io/shop/products/deye_rj45_split) |
| **Sol-Ark RS485 USB cable** | $29 | [solar-assistant.io/shop/products/sunsynk_rs485](https://solar-assistant.io/shop/products/sunsynk_rs485) |

$43 per inverter. This pair repeats for every Sol-Ark on site regardless of how many
you parallel — SolarAssistant's Sol-Ark 15K-2P documentation states that *"for parallel
inverters and 3 phase installations each inverter requires its own cable."*

The splitter is needed on any inverter whose CAN pins are already carrying a battery
BMS link — which is the normal case for a Sol-Ark paired with Pytes. See
[00 — Overview](00-overview.md) for why.

### Per Pytes V5 stack — 1 ×

| Item | Price | Order page |
|------|-------|------------|
| **Pytes console USB cable** | $29 | [solar-assistant.io/shop/products/pytes_rs232](https://solar-assistant.io/shop/products/pytes_rs232) |

One cable per **stack**, not per pack. The product page is explicit: *"A single cable
can read all batteries in the battery bank."* A twelve-pack stack needs exactly one
cable, the same as a two-pack stack.

Order a second cable only if you have a second, electrically separate stack with its
own master.

Shop index: [solar-assistant.io/shop](https://solar-assistant.io/shop) · Custom lengths:
[Create a custom RS485 or RS232 cable](https://solar-assistant.io/help/shop/create-custom-cable)

## Working out your order

```
Total = $229 + ($43 × inverters) + ($29 × battery stacks)
```

| Site | Device | Inverter kit | Console | Total |
|------|--------|--------------|---------|-------|
| 1 inverter, 1 stack | $229 | $43 | $29 | **$301** |
| 2 inverters, 1 stack | $229 | $86 | $29 | **$344** |
| 3 inverters, 1 stack | $229 | $129 | $29 | **$387** |
| 4 inverters, 1 stack | $229 | $172 | $29 | **$430** |
| 4 inverters, 2 stacks | $229 | $172 | $58 | **$459** |

Prices as listed at time of writing; confirm on the order pages.

## The USB port budget

> ### More than 3 inverters on a site requires a separate powered USB hub
>
> The supplied Pi 5 has **four** USB ports. Three inverters plus one battery stack
> fills all four. A fourth inverter has nowhere to go, so any site with **4 or more
> Sol-Arks must budget for a powered USB hub** in addition to the items above.

This is the constraint that decides whether your site needs anything beyond the list
above.

```
USB ports required = inverters + battery stacks
```

The supplied Pi 5 has **four** USB ports (2 × USB 2.0, 2 × USB 3.0).

| Site | Ports used | Fits directly? |
|------|-----------|----------------|
| 1 inverter, 1 stack | 2 | Yes, 2 spare |
| 2 inverters, 1 stack | 3 | Yes, 1 spare |
| 3 inverters, 1 stack | 4 | Yes, none spare |
| **4 inverters, 1 stack** | 5 | **No — powered hub required** |
| **5 inverters, 1 stack** | 6 | **No — powered hub required** |
| 3 inverters, 2 stacks | 5 | **No — powered hub required** |

The hub must be **powered** (its own mains supply). Do not use a bus-powered hub:
several FTDI adapters sharing an unpowered bus is a classic source of the intermittent
dropouts described in [06 — Troubleshooting](06-troubleshooting.md), and those failures
present as flaky data rather than a clean disconnect.

At exactly three inverters you fit with zero spare ports. Consider a hub anyway — it
leaves headroom for a fourth inverter without re-planning the install, and it keeps a
port free for a keyboard during on-site diagnostics.

## Why not a generic Amazon adapter

SolarAssistant's own Sol-Ark 15K-2P page warns that a random USB-RS485 RJ45 cable
*"will most likely not work"* unless it specifically states support for Deye inverters.
The pin assignment inside the RJ45 shell is not standardised across vendors, and a
cable wired for a different inverter family will present RS485 A/B on the wrong pins.

The supplied cables are 1.5 m, shielded, and use a genuine FTDI chip. That last detail
is verifiable after installation — see [05 — Verification](05-verification.md), where
every adapter should appear as a genuine FTDI part. Counterfeit FTDI chips are common
in cheap adapters and produce intermittent dropouts rather than clean failures, which
is far harder to diagnose.

The same applies to the splitter — see the warning in
[02 — Wiring the Sol-Ark](02-wiring-solark.md#step-2--fit-the-splitter) about passive
Y-adapters, which are **not** substitutes.

## Cable routing notes

- RS485 and console runs are shielded. Keep them out of the same conduit as battery
  cabling and AC output where practical.
- The splitter is 50 cm and lives inside or immediately adjacent to the inverter
  enclosure, so the 1.5 m RS485 cable is measured **from the splitter**, not from the
  inverter's port.
- If 1.5 m does not reach, order a custom length rather than adding an RJ45 coupler and
  patch cable. Every extra junction on an RS485 run is a candidate for intermittent
  faults.
- Plan cable runs before ordering: on a large site the distance from the furthest
  inverter to the Pi is what determines whether stock lengths work.

---

Next: [02 — Wiring the Sol-Ark 15K inverters](02-wiring-solark.md)
