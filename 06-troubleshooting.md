# 06 — Troubleshooting

[Index](README.md) · Prev: [05 — Verification](05-verification.md) · Next: [07 — Worked example](07-worked-example.md)

SSH is disabled by default, so every check below is done from the web UI.

## Symptom table

| Symptom | Most likely cause | Fix |
|---------|-------------------|-----|
| Fewer inverter columns than inverters on site | Not every USB port selected in Connections | Disconnect, multi-select **one entry per inverter**, reconnect — [page 04, step 3](04-solarassistant-config.md#step-3--configure-the-inverters) |
| Two columns, identical serials | Two RS485 cables on the same inverter | Trace and re-land one cable on the other inverter's splitter |
| An inverter shows Disconnected | Wrong pins, wrong port, or a non-Deye cable | Confirm the cable is in the splitter's **RS485 (pins 1–3)** socket, and that it is the purpose-built Sol-Ark cable |
| Inverter connects, battery drops out | RS485 pins carried through to the battery | You are using a passive Y-splitter, not the purpose-built one — [page 02, step 2](02-wiring-solark.md#step-2--fit-the-splitter) |
| Battery Disconnected | Console cable in the RS485 or CAN socket | Move it to the master pack's **RS232C / console** port |
| Battery connects, packs missing | Pack addressing, or a break in the inter-pack chain | Check for duplicate addresses; a pack whose address collides will not enumerate |
| Capacity reads low | Same as above — packs missing from the chain | Compare pack count against [page 05, check 4](05-verification.md#check-4--every-battery-pack-enumerates) |
| An adapter vanished from `lsusb` | Cable, port, or power | Try **Cycle USB power** on the USB devices page before touching hardware |
| Adapters drop out intermittently on a large site | Too many devices for the Pi's ports, or a bus-powered hub | Sites with more than 3 inverters need a **powered** hub — [USB port budget](01-hardware-and-ordering.md#the-usb-port-budget) |
| Intermittent dropouts, no clean failure | Counterfeit FTDI chip, or a marginal RS485 run | Confirm every adapter still shows as *Future Technology Devices International*; check for added couplers or extensions |
| Two inverters report Master, or none do | Parallel configuration fault on the inverters | Resolve on the inverters themselves — not a SolarAssistant issue |

## Diagnostic order

Work outward from the host. Each step rules out everything before it:

1. **`Configuration → System → USB devices → view detail`.** One `0403:6001` per
   inverter, one `0403:6015` per battery stack, all reporting as FTDI. If one is
   missing, it is physical. Try **Cycle USB power** first.
2. **`Configuration` → Devices panel.** Correct drivers, correct port count, both rows
   showing Connected.
3. **`/inverter/status`.** One column per inverter, all serials distinct, plausible
   independent values.
4. **`/battery/status`.** Full pack count and expected total capacity.

## The failure this wiring is most prone to

The single most likely long-term fault is someone replacing the purpose-built splitter
with a generic RJ45 Y-adapter — they look interchangeable and the generic one is
cheaper and easier to source locally.

A passive Y-adapter passes all eight pins to both sockets, which puts the RS485 pins on
the battery leg. The result is the confusing failure in row four of the table: the
inverter still reads fine, the battery intermittently drops, and nothing looks wrong at
the connector. If battery comms degrade after any maintenance visit, check what is
physically plugged into the BMS port before anything else.

## Things that are *not* faults

- **SolarAssistant's "Inverter 1" being the parallel slave.** Expected. Numbering
  follows USB enumeration order, not Modbus address. See
  [00 — Overview](00-overview.md).
- **Grid reading 0 W, 0 Hz and near-zero volts.** On an **off-grid site this is the
  normal steady state** — the grid input is simply absent and the inverters run from PV
  and battery. It is not a comms fault and not an alarm. On a grid-tied site the same
  reading would indicate a genuine outage or an open grid disconnect.
- **Small differences between inverters' readings.** Desirable — see
  [page 05, check 2](05-verification.md#check-2--per-inverter-values-are-independent-and-plausible).

## Escalation

If a fault survives the diagnostic order above, gather before contacting support:

- Screenshot of `Configuration → System → USB devices`
- Screenshot of the Devices panel showing drivers and port assignments
- Screenshot of `/inverter/status` including the serial number row
- Software version and board model from the System panel
- Site scale: number of inverters, number of battery stacks, whether a USB hub is in use
- Which of the four diagnostic steps first showed something unexpected

SolarAssistant support: [solar-assistant.io](https://solar-assistant.io) · Reference
pages used throughout this guide are linked from
[01 — Hardware and ordering](01-hardware-and-ordering.md).

---

Next: [07 — Worked example](07-worked-example.md)
