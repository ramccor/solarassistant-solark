# 02 — Wiring the Sol-Ark 15K inverters

[Index](README.md) · Prev: [01 — Hardware and ordering](01-hardware-and-ordering.md) · Next: [03 — Wiring the Pytes stack](03-wiring-pytes.md)

> **Before opening anything.** The RS485 port on a Sol-Ark 15K is behind the wiring
> compartment cover, alongside conductors at battery and AC potential. Shut down the
> inverter, open the DC and AC disconnects, and confirm de-energised before removing
> the cover. A comms cable is not worth working a live 15 kW enclosure. Follow
> Sol-Ark's own shutdown sequence for your model and firmware.

**Repeat this entire page once per inverter.** Every Sol-Ark on site gets its own
splitter, its own RS485 cable, and its own USB port on the Pi. Only the **master's**
splitter carries a battery CAN cable — see [step 2](#step-2--fit-the-splitter).

## Finding the right socket

A Sol-Ark 15K-2P has **four RJ45 jacks** in the wiring compartment, and three of them are
wrong. Identify the socket before you touch anything:

| Silkscreen label | Count | What it is |
|------------------|-------|------------|
| `Parallel` | 2 | Inverter-to-inverter parallel link. Leave alone |
| `Modbus RS485` | 1 | External Modbus devices such as meters. **Not this one** |
| **`Battery CANBus`** | 1 | **The 2-in-1 port. This is the one.** Right-hand jack of the group |

> **The `Modbus RS485` jack is a decoy.** You are running an RS485 cable, there is a jack
> labelled `Modbus RS485`, and it is the wrong one. SolarAssistant reads the inverter over
> the RS485 pins of the **`Battery CANBus`** jack — the port Sol-Ark's manual lists under
> "BMS RJ45 ports (RS485 / CAN)" and instructs you to use for battery communications.

Source: Sol-Ark 15K-2P-N manual, §1.1 General Description, component **E**.

## The 2-in-1 BMS port

The `Battery CANBus` jack is one RJ45 socket carrying two buses:

| Pin | Signal | Bus |
|-----|--------|-----|
| 1 | RS485 **B** | RS485 → SolarAssistant |
| 2 | RS485 **A** | RS485 → SolarAssistant |
| 3 | GND | RS485 → SolarAssistant |
| 4 | CAN High | CAN → battery BMS |
| 5 | CAN Low | CAN → battery BMS |
| 6, 7, 8 | unused | — |

RS485 needs three pins and CAN needs two, which is exactly why both fit one connector.
The inverter reads the battery over CAN while SolarAssistant reads the inverter over
RS485, in the same port, at the same time.

Source: [SolarAssistant — 1 in 2 BMS port](https://solar-assistant.io/help/inverters/deye/SG01LP1/2-in-1-bms-port).

## Step 1 — Confirm the CAN pins are in use

On the inverter's own display, check the battery protocol:

```
Battery type      : Lithium
Lithium protocol  : CAN (protocol 0)
```

- **CAN (protocol 0)** — the battery link uses pins 4–5, leaving RS485 free. You need
  the splitter. This is the normal case for Sol-Ark paired with Pytes.
- **An RS485 battery protocol** — pins 1–3 are already occupied by the battery and this
  approach does not apply. Changing an inverter's battery protocol is a commissioning
  decision with consequences for charge control; it is out of scope here.

Check this on **every** inverter, not just the master. A unit that has been swapped or
re-flashed may not match its siblings.

## Step 2 — Fit the splitter

Plug the splitter's single male RJ45 into the inverter's `Battery CANBus` jack.

**What goes on the CAN leg depends on which inverter you are at:**

| Inverter | CAN leg |
|----------|---------|
| **Master** | The existing battery CAN cable. Unplug it from the jack, move it to the splitter's **CAN (pins 4–5)** socket |
| **Slave** | **Nothing. Leave it empty.** |

Only the master talks to the battery stack over CAN; the slaves receive battery state
across the inverter-to-inverter parallel link instead. A slave's `Battery CANBus` jack is
therefore empty before you start, and its splitter's CAN leg stays empty afterwards.

> **A slave still gets its own splitter.** One splitter per inverter is what
> SolarAssistant's own documentation specifies, and it is the configuration verified
> working on a live two-inverter site — see [07 — Worked example](07-worked-example.md).
> It also means every inverter is wired identically and the RS485 cable can never end up
> sharing a socket with CAN. Do not economise here: an untested variation on a comms
> topology is a poor trade for the price of one adapter.

```
  Battery CANBus jack
   (pins 1-5 in)
        │
   ┌────┴─────┐
   │ splitter │
   └──┬────┬──┘
      │    │
 pins │    │ pins
  1-3 │    │ 4-5
      │    │
   RS485  CAN
      │    │
      │    └──► MASTER: existing cable to battery BMS
      │         SLAVE:  empty
      │
      └──► new USB-RS485 cable to the Pi
```

> **Do not hand-roll this with a passive Y-splitter.** SolarAssistant's documentation
> is specific: when making a custom splitter, do not carry the RS485 pins through to
> the battery alongside the CAN pins. Doing so puts the battery on the RS485 bus and
> breaks SolarAssistant's ability to read the inverter. A generic RJ45 Y-adapter passes
> all eight pins straight through to both sockets and will do exactly this. Use the
> [purpose-built splitter](https://solar-assistant.io/shop/products/deye_rj45_split).

## Step 3 — Connect the RS485 cable

Plug the [Sol-Ark RS485 USB cable](https://solar-assistant.io/shop/products/sunsynk_rs485)
into the splitter's RS485 socket and run it to the Raspberry Pi.

**Each inverter gets its own cable into its own USB port.** Do not bridge two
inverters' RS485 lines onto one adapter — SolarAssistant's Sol-Ark 15K-2P documentation
requires one cable per inverter in parallel installations.

The inverter-to-inverter parallel CAN link is a separate cable between the Sol-Arks and
is not touched by any of this. Leave it exactly as it is.

## Step 4 — Label both ends by serial number

You now have several identical black cables arriving at one Pi. Label each at both ends
with the inverter's **serial number** — not "1" and "2".

Record a table like this as you go; you will need it for
[05 — Verification](05-verification.md):

| Cable label (serial) | Parallel role | Modbus № | Pi USB port |
|----------------------|---------------|----------|-------------|
| _serial of inverter A_ | Master / Slave | | |
| _serial of inverter B_ | Master / Slave | | |

Serial number is the only key that stays stable. As covered in
[00 — Overview](00-overview.md), SolarAssistant's own "Inverter 1"/"Inverter 2" labels
follow USB enumeration order and need not match Modbus addresses or parallel roles.

## Step 5 — Restore power

Close the enclosure, restore AC and DC, and bring the inverters up. Confirm the
parallel group still reports exactly one master on the inverters' own displays
**before** moving to SolarAssistant — if the parallel link was disturbed while the
cover was off, you want to know now, not while debugging comms.

---

Next: [03 — Wiring the Pytes V5 stack](03-wiring-pytes.md)
