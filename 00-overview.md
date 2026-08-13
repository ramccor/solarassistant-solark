# 00 — Overview and topology

[Index](README.md) · Next: [01 — Hardware and ordering](01-hardware-and-ordering.md)

## The problem this wiring solves

Sol-Ark 15K inverters expose a single RJ45 **2-in-1 BMS port** that carries two
independent buses on different pins:

| Pins | Bus | Used by |
|------|-----|---------|
| 1, 2, 3 | RS485 (B, A, GND) | **SolarAssistant** reading the inverter |
| 4, 5 | CAN (High, Low) | The **inverter reading the battery BMS** |
| 6, 7, 8 | unused | — |

Because the two buses occupy different pins in the same connector, they can run
simultaneously — but only one RJ45 plug fits the socket. That is what the splitter is
for: it breaks the one physical port into two sockets, one carrying pins 1–3 and the
other carrying pins 4–5.

In a Sol-Ark + Pytes system the battery link normally runs on **CAN**, which you
confirm on the inverter as `Lithium protocol: CAN (protocol 0)`. The CAN pins are
therefore occupied and the RS485 pins are free for SolarAssistant.

Source: [SolarAssistant — 1 in 2 BMS port](https://solar-assistant.io/help/inverters/deye/SG01LP1/2-in-1-bms-port).

## The two scaling rules

Everything about this install follows from an asymmetry between the two device types:

### Inverters do not share a cable

Paralleled inverters are linked to each other by their own CAN bus for load sharing and
master/slave arbitration. That link carries **no Modbus data to SolarAssistant**.

SolarAssistant's Sol-Ark 15K-2P documentation is explicit: *"For parallel inverters and
3 phase installations each inverter requires its own cable."* You cannot daisy-chain
the RS485 side. **N inverters means N RS485 cables, N splitters, and N USB ports.**

### Battery packs do share a cable

The packs in a stack are already chained to one another, and the master pack aggregates
the whole stack. **One console cable reads every pack**, whether the stack holds two
packs or twelve.

A second console cable is needed only for a second, electrically separate stack with
its own master.

## Topology

```
                        ┌────────────────────────────┐
                        │  SolarAssistant device     │
                        │  (Raspberry Pi 5, 4x USB)  │
                        └──┬────────┬────────┬───┬───┘
                           │        │        │   │
                    RS485 ─┘  RS485 ┘        │   └─ spare
                      │         │            │
                      │         │      RS232 console
                      │         │            │
        ┌─────────────┴──┐  ┌───┴───────────┐│
        │ Sol-Ark 15K #1 │  │ Sol-Ark 15K #N││
        │ 2-in-1 BMS port│  │ 2-in-1 BMS port││
        │  └─ splitter   │  │  └─ splitter  ││
        │     ├ pins 1-3 ┘  │     ├ pins 1-3┘│
        │     └ pins 4-5 ┐  │     └ pins 4-5┐│
        └────────────────│──┘───────────────││
                     CAN │                CAN││
                         ▼                  ▼▼
              ┌──────────────────────────────────────┐
              │  Pytes V5 stack                      │
              │  master pack (console port)          │
              │  + chained packs                     │
              └──────────────────────────────────────┘

  The inverter-to-inverter parallel CAN link runs separately between the
  Sol-Arks for load sharing. It carries no SolarAssistant data — leave it alone.
```

Each inverter contributes one RS485 leg to the Pi. Each battery stack contributes one
console leg. The CAN legs go to the battery and never to the Pi.

> **Port limit.** The Pi 5 has four USB ports, and three inverters plus one battery
> stack fills all four. Any site with **more than 3 inverters requires a separate
> powered USB hub** — see the
> [USB port budget](01-hardware-and-ordering.md#the-usb-port-budget).

## What SolarAssistant gives you

Once wired and configured:

| Source | Data |
|--------|------|
| Each inverter, individually | Load, PV per MPPT, battery, grid, temperatures, serial, parallel role |
| Inverter cluster | Site totals across all inverters |
| Each battery pack | Serial, firmware, SOC, cell voltages, cell imbalance, temperatures, cycles |
| Battery bank | Total capacity, SOC, recommended charge/discharge limits |

## Numbering gotcha

**SolarAssistant numbers inverters by USB port enumeration order — not by Modbus
address and not by parallel role.**

SolarAssistant's "Inverter 1" may well be the Sol-Ark configured as the parallel
*slave*. Do not assume its number matches the number on the inverter's own display, and
do not use it to decide which physical unit you are looking at.

Match on the **serial number** instead. It is the only unambiguous key, it appears in
both the inverter settings page and the cluster status page, and it does not move when
someone re-seats a USB cable.

[07 — Worked example](07-worked-example.md) shows a real site where SolarAssistant's
"Inverter 1" is Modbus 2 and the slave.

## Prerequisites before you start

- Inverters already paralleled, commissioned, and reporting a single master
- Battery stack already addressed, chained, and communicating with the inverters over
  CAN
- `Lithium protocol: CAN (protocol 0)` set on every inverter
- Network available to the Pi (WiFi or Ethernet)

This guide adds monitoring to a working system. It is not a commissioning procedure for
the inverters or the battery bank.

---

Next: [01 — Hardware and ordering](01-hardware-and-ordering.md)
