# Cheat sheet — Sol-Ark 15K-2P parallel inverter failure

Standalone reference; not part of the guide sequence or the slide decks. Source: Sol-Ark
*15K Installation Manual* MA-00007 **Rev. 13** (July 2026), §2.12 Power Cycle Sequence,
§5 Parallel Systems, §8.1 Error Codes. Section references below are to that document.
Applies to 120/240 V split-phase parallel systems on a shared battery bank.

## What the master does that a slave doesn't

| Responsibility | Manual reference |
|---|---|
| Holds **Modbus SN 1**; its GRID and Battery settings are copied to every slave | §5.2 step 3; §4 power-on step C |
| Controls the **generator two-wire start** (relay on pins 7 & 8) | §5.2 note: *"The inverter assigned as Master will control the two-wire start feature"* |
| Carries the **CT pair** (grid-tied sites only) | §2.9: *"Only one pair of CT sensors must be wired to the designated Master inverter"* |
| Is the only unit whose **Battery CANBus** jack is cabled to the BMS on a typical build — slaves take battery state over the parallel link | Site wiring convention; see page 00 |

Everything else — LOAD, GRID, GEN AC connections, the battery bank — is shared by every
unit (§5.1 C: *"All INPUTS/OUTPUTS must be shared among ALL parallel inverters, except
for DC solar inputs"*). PV strings are **not** shared: a dead inverter takes its own
strings with it.

## Fault codes you will see (§8.1)

| Code | Name | Meaning in a parallel system |
|---|---|---|
| **F29** | Parallel_Canbus_Fault | Lost parallel comms. *"Check cables, and Modbus addresses."* Normal for a moment during power-up until all units are on. |
| **F41** | Parallel_System_Stop_Fault | *"If one system faults in parallel, this normal fault will register on the other units as they disconnect from the grid."* The healthy units are reporting a neighbour's failure. |
| **F46** | Battery_Backup_Fault | *"Cannot communicate with other parallel systems. Verify that the Master is set to 1, the Slaves are set to 2–9, and the Ethernet cables are connected."* |
| **F61** | Button_Manual_OFF | *"The parallel Slave system turned off without turning off the Master."* Someone pressed a slave's power button. |
| **F58** | BMS_Communication Fault | Unit is in lithium BMS mode but has no BMS link — expect this on slaves if the master (which holds the CAN cable) goes down. |

## Common ground rules

- **Power-cycle order (§2.12, parallel):** OFF — AC breakers (GRID, GEN, LOAD), then PV DC
  disconnect, then power button, **master first, then slaves**; battery breakers last, any
  order; wait ~1 min. ON — reverse it: **slaves first, master last**. *"Inverters will
  likely fault momentarily with F29 and F41 codes until all inverters are ON."* (§5.2 step 6)
- **DIP switches (§5.1):** termination on the two ends of the parallel daisy-chain. Two
  units: **both ON**. Three or more: first and last ON, middle units OFF. Any change to
  the chain means re-checking these.
- **Firmware:** all units in parallel must show the same COMM and MCU version
  (§5.1 A). A replacement unit must be updated to match *before* it joins the chain.
- **Five strikes.** Self-clearing alarms auto-restart up to 5 times; the fifth stop on the
  same alarm locks the unit out until it is manually reset and the cause is cleared
  (installer's deck). A unit that is "dead" may just be locked out — read its alarm list
  before condemning it.
- **Never run parallel mode without a battery bank** (§5.1) — irrelevant during a failure
  but the reason you don't "just" pull the battery to isolate a unit.

---

## A. Slave inverter failure

**Symptoms.** Slave shows red Alarm LED or is dark; other units log **F41** (and may
briefly drop AC output), then carry on. In SolarAssistant the failed unit's column on
`/inverter/status` goes stale; total PV and load capacity fall by one unit's share.

**What still works.** Generator auto-start (master), BMS communication (master), all
shared AC paths, battery charge/discharge through the remaining units. What is lost:
15 kW continuous / 12 kW on battery per unit, and that unit's PV strings.

**Steps**

1. **Read the alarm** on the failed unit: Home → *System Alarms*. Note the code(s). If it
   is F29/F46, check the yellow parallel RJ45 cable and the Modbus SN before assuming
   hardware failure.
2. **Try one power cycle** of the whole system per §2.12 (master off first, slaves on
   first). Many faults clear. If the unit comes back with the Normal LED, stop here and
   watch it.
3. **If it does not recover, isolate it:** on the failed unit only — AC breakers OFF
   (GRID, GEN, LOAD), PV DC disconnect OFF, power button OFF, its battery breaker OFF.
   Leave the others running.
4. **Repair the parallel chain.** If the dead unit was at the *end* of the daisy-chain
   (always true in a two-inverter system), nothing to re-cable; set the new end unit's DIP
   switch ON. If it was in the *middle*, cable around it (Parallel_1/Parallel_2 ports) and
   re-terminate the two new ends.
5. **Power-cycle the survivors** (§2.12) so they re-establish parallel comms. Expect
   momentary F29/F41, then Normal LEDs.
6. **Shed load** to the reduced capacity (§5.1 table: 15 kW with PV / 12 kW on battery,
   × remaining units). Peak 10 s is 24 kVA per unit.
7. **Charge current:** Gen/Grid "A" on the Battery Setup page is **per inverter** — the
   total into the bank drops automatically with one unit gone. Raise the per-unit value
   only if the generator can carry it.
8. **SolarAssistant:** no reconfiguration needed. The stale column is expected; reconnect
   the RS485 lead when the replacement arrives.

**Replacement unit:** match firmware (§5.1 A) → set Parallel ✓, Modbus SN to the vacated
number, DIP switch per position → cable into the chain → full power cycle, slaves first,
master last → verify GRID and Battery settings copied from the master (§4 step E).

---

## B. Master inverter failure

**Symptoms.** Master dark or in alarm; slaves log **F41**, then **F29/F46** (no comms) and,
if in lithium BMS mode, **F58** (the BMS cable lands on the master). Generator will not
auto-start. In SolarAssistant inverter 1's column goes stale; battery data from the Pytes
console port keeps flowing because that path does not go through the inverter.

**Why this is urgent.** With no generator control and no BMS link, the bank can discharge
to *Shutdown* with nothing to stop it. Treat this as a same-day job, not a "watch it"
situation.

**Immediate stopgap (minutes):**

- The generator is wired to the GRID input of **every** unit (§5.1 C), so the surviving
  slaves are physically fed the moment it runs. Start it manually from its own controls
  and watch for the AC LED on a slave: if it lights, the slave is accepting the input and
  you have passthrough and charging while you work. If it does not light within a couple
  of minutes, the slave's logic is not qualifying the input without a master — shed to
  essential loads and go straight to promotion. (The manual does not state which
  happens; confirm with Sol-Ark support before you need it.)
- Note `Shutdown`/`Restart` and current SOC so you know your runway.

**Promote a slave to master (the fix):**

1. **Power down everything** per §2.12 — failed master's AC breakers, PV disconnect and
   power button first (if it is alive at all), then each slave, then battery breakers.
2. **Move the master-only wiring to the chosen slave:**
   - **Battery CAN** lead → the new master's *Battery CANBus* jack (right-hand RJ45). If
     every unit already has a splitter fitted, this is just moving one leg.
   - **Generator two-wire start** → new master's pins **7 & 8** (Gen Start Relay).
   - **CT pair** → new master (grid-tied sites only; off-grid has none).
   - **SolarAssistant RS485** leads stay where they are.
3. **Re-address.** On the promoted unit: *Basic Setup → Parallel → Modbus SN = 1* (it is
   already Parallel ✓). Leave the remaining slaves at 2…n; the vacated SN can stay empty.
4. **Repair the chain and terminations** exactly as in A.4 — the dead master is almost
   always an end unit, so the promoted unit becomes a chain end with its DIP switch ON.
5. **Power up: slaves first, new master last** (§5.2 step 6). Wait for Normal LEDs on all.
6. **Verify the new master's settings** — they were copied from the old master when it
   was a slave, but confirm each page before trusting it: *Grid type 120/240 V split-phase;
   Battery Setup (capacity, Shutdown/Restart, Gen/Grid charge A, BMS lithium mode);
   Gen start V/%, Gen down time, Gen max run time; Time of Use — every interval where
   the generator must be able to auto-start needs `Charge` ticked.* Then confirm the
   slaves report the same values (§4 step E).
7. **Prove generator control:** *Force gen* from the new master → *Gen Signal* should show
   within ~2 minutes (Sol-Ark training notes) → generator starts → charge current appears
   on `/inverter/status` → clear *Force gen*.
8. **Prove BMS comms:** battery SOC, voltage and limits on the new master's battery page
   match the BMS; no F58.
9. **Shed load** to remaining capacity as in A.6.
10. **SolarAssistant:** no change. `/inverter/settings` will now show the promoted unit as
    master; the old master's column stays stale until the replacement is connected. If
    low-SOC automations key off a specific inverter's values, re-point them.

**Replacement unit:** as in A, but decide whether it joins as a slave (simplest — leave
the promoted unit as master) or is made master again, which means repeating steps 2–8 in
reverse. Do not leave two units at SN 1.

---

## Two-inverter quick card

| | Slave (SN 2) dies | Master (SN 1) dies |
|---|---|---|
| Capacity left | 15 kW PV / 12 kW battery | 15 kW PV / 12 kW battery |
| Gen auto-start | still works | **lost** until promotion |
| BMS comms | still works | **lost** until CAN lead moved |
| Chain work | none; survivor's DIP stays ON | set SN 2 → 1; move CAN lead + gen start wires; DIP stays ON |
| Power-up order | just the survivor | just the survivor (it is now the master) |
| Expect | F41 logged on survivor | F41, F29/F46, F58 logged on survivor |
