# Cheat sheet — low battery, shutdown and recovery

Standalone reference; not part of the guide sequence or the slide decks. Sources: Sol-Ark
*15K Installation Manual* MA-00007 Rev. 13 (§3.4 Battery Setup, §8.1 Error Codes) and the
installer's customer-training deck. For an LFP bank (Pytes V5) on parallel Sol-Ark 15K-2P
inverters.

## Two safeties, in the order they trip

| Layer | What it does | Where set |
|---|---|---|
| **1. Sol-Ark `Shutdown` V/%** | Inverter stops AC output *"to protect the battery from an over discharge situation"*; battery icon turns red. Output resumes at **`Restart` V/%**. If grid or generator is available the inverter passes it through instead. | Battery Setup → Discharge |
| **2. BMS low-voltage cutoff** | The pack itself disconnects, typically in the **3–10 % SOC** band. Pytes V5 enters **sleep below ~5 %** but keeps a small reserve so it can be **force-charged back** if it is not left flat for long. Left drained for an extended period, it needs service. | Fixed in the BMS |

Layer 1 is meant to fire first and leave headroom above layer 2. Between them sits
**`Low Batt`** (icon turns yellow): on an off-grid site TOU may discharge down to
*Shutdown*, on a grid-tied site only down to *Low Batt* (§4).

**The goal is never to reach layer 2.** A pack that has tripped its own BMS is the one
failure on this sheet that can turn into a service call.

## Recommended usable window (training deck)

- LFP: use down to **10–20 % SOC** in normal operation (80–90 % usable). The battery warranty excludes **routine discharge below 10 %**.
- Installer's off-grid setpoints: generator auto-start **35 %**, Sol-Ark Shutdown **15 %** (Sol-Ark's own default is 20 %), emergency floor **11 %**.
- During an outage the bank may go lower before Shutdown — acceptable occasionally, not routinely.
- Bring the bank to **100 % SOC at least once a week** for BMS balancing. Off-grid, that means a clear day with solar — the generator stops at ~95 % and will not do it.

## When the battery icon goes yellow (Low Batt)

1. Note SOC and time. Work out hours of runway at the current load.
2. Shed discretionary loads (water heating, HVAC setback, EV charging, pumps that can wait).
3. Off-grid: confirm the generator *will* auto-start — the Start % setpoint is above Shutdown, no TOU interval without ☑ Charge covers the next few hours, Gen Down Time is not still counting. If in doubt, **force it now** (see the generator sheet) rather than finding out at 3 a.m.
4. Check SolarAssistant for a reason: a string down, an inverter column stale, an unexpectedly large load.

## When the inverter has shut down (red icon, no AC output)

1. **Do not reset the inverter or pull the battery breaker.** It is waiting for `Restart` V/% — it will resume on its own once the bank is charged above that point by solar, grid or generator (deck: *"system should restart automatically once batteries are sufficiently recharged or grid (or generator) power becomes available"*). Self-clearing alarms (overload, under-voltage, low battery) auto-restart **up to 5 times**; after the fifth stop on the same alarm the inverter **locks out until manually reset** and the cause is fixed — so if it is dark and silent, read the alarm list before anything else.
2. **Get charge into the bank:**
   - Daylight: the MPPTs still charge with AC output off. Wait.
   - Off-grid, night: start the generator — Gen Force from the master if the screen is alive; otherwise from the generator's own controls (it feeds every inverter's GRID input).
   - Grid-tied: confirm grid is present; the inverter should already be in passthrough.
3. **Watch for F56** DC_VoltLow_Fault: *"Batteries are overly discharged, the inverter is Off-Grid and exceeded the programmed batt discharge current by 20 %, or Lithium BMS has shut down."* F56 together with F58 (BMS comms lost) means the BMS has likely gone to sleep — move to the next section.
4. Once SOC is above `Restart`, AC output returns. Reconnect loads gradually.
5. Afterwards, find out why. Usual causes: generator did not start (TOU/Down Time/loop), a string or inverter was down, or a load ran all night.

## When a pack has gone to sleep (BMS cutoff)

Symptoms: pack LEDs dark or in fault, no voltage at its terminals, inverter shows F56/F58,
SolarAssistant's `/battery/status` card for that pack stale or missing.

1. Do not attempt to charge a sleeping LFP pack with anything other than the inverter or a **51.2 V LFP force charger**. Do not parallel it to live packs hoping it "catches up".
2. **Act promptly.** Pytes keeps a reserve below the sleep point precisely so a force charge can recover it — but only if it has not sat flat for an extended period.
3. **Follow the Pytes V5 wake procedure** — *confirm the exact steps with the installer and write them here; the Sol-Ark documents do not cover it.* Typically: pack breaker off, press/hold the pack's power button, breaker on, then the inverter resumes charging once the BMS reports.
4. If the pack does not wake: isolate it (breaker off) so the rest of the bank can run, then force-charge it at the pack terminals with the 51.2 V charger until the BMS wakes and reports. The installer's advice is to **own that charger before it is needed** so this never becomes a service call.
5. If it still will not wake, call the installer / Pytes support.
6. Before returning to service, raise the Sol-Ark `Shutdown` setpoint if it allowed the bank to get this low.

## Setpoints to verify (Battery Setup → Discharge)

| Setting | Purpose | Sanity check |
|---|---|---|
| `Shutdown` % | Inverter stops output | Comfortably above the BMS sleep point (~5 % on Pytes) — 15 % is the installer's value |
| `Restart` % | Output resumes | 5–10 points above Shutdown so it does not cycle |
| `Low Batt` % | Yellow warning; TOU floor on grid-tied | Between Shutdown and your normal daily floor |
| `Start %` (Gen Charge) | Generator auto-start | Above Low Batt, well above Shutdown — 35 % leaves ~20 points of reserve |
| Max Gen Runtime | Ends a run by time | Long enough to reach ~90 % from Start % at the set Amps |
| `BMS_Err_Stop` | Stop on loss of BMS comms | Know what it is set to — it decides what slaves do if the master (and its CAN cable) fails |
| Capacity (Ah/kWh) | Used for % SOC and limits | Matches the installed bank |
| Charge Efficiency / Batt Empty V | SOC calculation | Leave at manufacturer values; do not tune |

Set a SolarAssistant or Home Assistant alert a few points above `Low Batt` so the first
warning is a notification, not a yellow icon nobody is looking at.
