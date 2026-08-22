# Cheat sheet — generator charging on a Sol-Ark 15K-2P

Standalone reference; not part of the guide sequence or the slide decks. Sources: Sol-Ark
*15K Installation Manual* MA-00007 Rev. 13 (§2.5 Integrating a Generator, §3.4 Battery
Setup, §4 Operation Notes), the installer's customer-training deck (as-delivered version),
and the Wildcat Patriot / Hyundai *Operation and Maintenance Manual* (20–100 kW mobile
generating sets) for the generator side. Written for an
**off-grid site with the prime generator on the GRID input** and two-wire auto-start,
plus a separate inlet for a portable generator on the **GEN input**.

## How it behaves when left alone

| Rule | Source |
|---|---|
| Auto-start fires when the bank reaches **Start V or Start %** (one condition, not both) | §3.4 Gen Charge |
| Charging from the generator **stops at ~95 % SOC** — *"the batteries will charge until the battery bank accepts 5 % of its rated capacity in Amperes"*. It will **never** reach 100 % on generator power; that is normal. | §4 note 6 |
| The 95 % ceiling is *"non-modifiable unless Time of Use is enabled and programmed"* | §4 note 6 |
| **If TOU is on**, the generator will not auto-start in any interval that does not have **☑ Charge** ticked, *"even if the Start V or Start % condition has been met"* | §2.5 |
| **Gen/Grid "A" is per inverter.** Multiply by the number of inverters for the current into the bank. | §2.5 |
| Off-grid: keep the **Gen A and Grid A values equal** *"to avoid logic issues"* | training deck |
| Max Gen Runtime (firmware 7228+, bottom of the Charge tab) and Gen Down Time can end or block a run regardless of SOC | training deck; §3.4 |
| Charge rate **tapers above 90 % SOC** (roughly 10 A per pack between 90 and 95 %) — the last 5 % is slow, expensive generator time. Size Max Gen Runtime to reach ~90 %, not 95 %. | training deck |
| Typical off-grid setpoints from the installer: auto-start **35 %**, Sol-Ark shutdown **15 %**. The gap is deliberate reserve. | training deck |
| Weekly exercise: **Monday 08:00, 20 min** by default. Disable with `00 \| 00 min`. | §4 note 6; §3.4 |
| With a generator on the GRID input, **☑ GEN connect to Grid input** must be set, Grid Mode *General Standard*, Grid Reconnect Time 30 s | §3.4 Grid Charge; §4 note 5 |
| GEN terminal continuous limit **80 A** — do not exceed | §2.5 |

## Force a generator run (charge now, or test auto-start)

On the **master** inverter's screen (or MySolArk):

1. ⚙ Settings → **Battery Setup** → **Charge** tab
2. Tick **☑ Gen Charge** and **☑ Gen Force** → **OK**
3. Back to the home screen. **"Gen Signal" shows within ~2 minutes** — pins 7 & 8 have closed and the generator should be cranking.
4. The Sol-Ark **qualifies** the supply over the next **1–3 minutes** (voltage and frequency must be stable). Only then does it start drawing power.
5. Watch the charge current on the battery page or SolarAssistant. It should be ≈ Gen A × number of inverters.

**To stop:** same page → untick **Gen Force** (and Gen Charge if you only wanted a one-off) → **OK** → **wait for Gen Signal to drop** → then let the generator cool down and stop. Do not kill the generator while the Sol-Ark is still drawing from it.

Gen Force is a test function: *"The generator will not provide power during this test if grid power is available"* (§3.4). On an off-grid site it simply runs **until unticked** — it does not stop at 95 %.

## Adjusting the auto-start point on the fly

Start % is just a setting. If it is 06:00 on a clear-sky morning and the bank is sitting
just above Start %, lowering it a few points avoids a pointless run; raise it back
afterwards. **Never routinely below ~10 %** (LFP warranty) — the installer's stated
emergency floor is **11 %**, and only if the generator will not start and you need the
capacity.

## If the generator stalls, trips, or the Sol-Ark drops it

| Symptom | Cause | Fix |
|---|---|---|
| Generator bogs / breaker trips shortly after qualifying | Charge current + loads exceed generator rating | Lower **Gen A** (per inverter!) on the Charge tab. Shed heavy loads while charging. |
| Sol-Ark shows AC briefly then rejects it; **F60** Gen_Volt_or_Fre_Fault | Frequency or voltage drifting outside limits — usually overload pulling it under 60 Hz | Lower Gen A; check the generator's governor; keep loads light until SOC recovers |
| Gen Signal on but nothing cranks | Two-wire loop open, generator not in AUTO, or wiring on the wrong inverter | Generator must be in auto mode; loop is on the **master's** pins 7 & 8 (N.O. dry contact) |
| Gen Signal never comes on | TOU interval without ☑ Charge; Gen Down Time still counting from the last run; Max Gen Runtime hit | Check TOU intervals; check Gen Down Time; wait or clear with Gen Force |
| Charging stops at ~95 % with generator still running | Normal cutoff | Nothing — that is the design. If you need it to stop *sooner*, set an upper limit via TOU. |
| Generator ran for hours, SOC barely moved | Gen A too low for the bank size, or heavy loads consuming the output | Raise Gen A within generator capacity; check load |

Rule of thumb for Gen A: generator continuous kW × 1000 ÷ ~55 V ÷ number of inverters,
then back off 10–20 % for loads and governor headroom.

## Portable 240 V generator on the GEN-input receptacle

For when the prime generator is down. The outdoor 50 A receptacle is wired to the
Sol-Arks' **GEN** terminals — a different input from the prime generator, so the charge
logic has to be switched over. **120 V generators will not work**; 240 V only, **12 kW
maximum** on a 50 A inlet.

1. Place the generator outdoors, clear of intakes — carbon-monoxide risk.
2. Plug the 240 V cable into the inlet, then into the generator. Start it; let it warm up **2–5 min**. The Sol-Ark should not load it yet.
3. Battery Setup → Charge: **untick Grid Charge** (the prime-generator path) and **tick ☑ Gen Charge**.
4. **Lower the charge Amps to about 50 % of the portable generator's capacity.** Amps are DC into the battery: ~20 A × ~50 V ≈ 1 kW per inverter, and the value is **per inverter** — 20 A on the master with two inverters is 40 A into the bank. Example: 12 kW portable → ~6 kW for charging → ~120 A DC total → **60 A per inverter** on a two-inverter system, less if loads are running.
5. Tick **☑ Gen Force** → OK. Gen Signal within 120 s; qualification 1–3 min.
6. Keep loads minimal while charging.
7. Finished: untick Gen Force and Gen Charge → wait for the signal to stop → shut the generator down → unplug at the generator, then at the inlet → **re-tick Grid Charge** and restore the normal Amps so the prime generator works again.
8. If it overloads or the Sol-Ark stops taking power, you are charging too many amps — reduce on the Charge tab.

## The generator side — Wildcat Patriot 40 kW (DSE 6110 MKIII controller)

**Ratings (single-phase 120/240 V):** 36 kW prime, **150 A** per leg, 50 kVA nameplate.
Derate 1.5 % per 10 °F above 77 °F. Fuel: **3.6 gal/h full load, 2.8 at 75 %, 2.0 at
50 %**. Oil change interval 500 h. Control panel is inside the enclosure behind the
**left rear door**: control-supply switch, DSE controller, MCCB, emergency stop.

**For the Sol-Ark to start it, the controller must be in AUTO** (the Sol-Ark manual:
*"the gen must be in automatic mode"*). In Auto the DSE waits for the remote-start
contact — the Sol-Ark's pins 7 & 8 — and runs its own start, warm-up, cool-down and stop
timers. After any manual use, **put it back in Auto** or the next low-SOC event will not
start it.

| Want to… | On the DSE panel |
|---|---|
| Start by hand | **Manual** mode key (LED lights) → **Start** once. Watch it crank. Let it run unloaded ~3 min before closing the MCCB. |
| Stop by hand | Open the MCCB (unload), let it idle ~5 min, **Stop** once — the controller runs a cool-down timer, then stops. |
| Clear a fault | **Long-press Stop/Reset** until the displayed fault clears. Fix the cause first — a cleared fault that recurs will re-trip. |
| Return to auto-start | **Auto** mode key. Confirm the LED. |
| Switch the controller off entirely | Open the breakers inside the controller panel. |

**Start Failure lockout.** If the engine does not catch after several crank attempts the
DSE latches *Start Failure* and refuses to crank again until reset. This is the usual
reason "Gen Signal is on but nothing happens": check the DSE display before touching the
Sol-Ark. Low fuel, a gelled filter, or a flat starting battery are the common causes.

**Safety stops that latch:** low oil pressure, high coolant temperature, over/under-speed,
E-stop pressed, alternator under/over-voltage or over-frequency. All stay in alarm until
manually reset on the panel; the Sol-Ark cannot clear them.

**Starting battery.** Two things can keep it up, and at least one must be powered at all
times — the DSE controller sitting in Auto is a constant small drain, and a flat starting
battery is the most common reason an auto-start fails on a cold morning:

- The generator's own **automatic charger**, fed (together with the **magnetic sump
  heater**, which keeps the engine startable below 32 °F and is the 1000–1500 W draw the
  installer mentioned) from the **120 V NEMA 5-15 inlet** on the power-panel door.
- An external **Battery Tender Plus 12 V / 1.25 A** (Deltran 022-0185G-DL-WH) clipped
  to the battery. It is a 4-stage float maintainer designed to stay connected
  indefinitely; draw is ~20 W, so it costs nothing to leave on. Its LED tells you the
  state at a glance: **red** = charging, **green flashing** = >80 % and topping up,
  **green steady** = float/maintained, **red flashing** = fault or reversed clips. Check
  it on the daily walk-around.

Either device alone will float the battery. If both are powered, two float chargers on
one battery is harmless, but do not rely on the tender in place of the inlet in winter —
the sump heater still needs that 120 V feed. Keep whichever circuit feeds them on a load
that stays up at low SOC, and budget the heater into winter overnight load.

**Disconnect the tender (or open the inlet breaker) before disconnecting the battery**
for work — clips first, then the battery negative.

**Daily / before-run checks (manual Table 37):** walk-around for fuel, oil and coolant
leaks; air-cleaner restriction indicator; oil level; coolant level; **drain the fuel/water
separator**; hoses and clamps. After start: watch oil pressure, coolant temperature,
battery voltage, frequency (60 Hz) and that the load is within rating.

**Service intervals:** oil and filter at 500 h (first change at 50 h); fuel primary and
secondary filters, belt check and centrifugal filter clean at the 250 h / 1 year column
of Table 37; air-cleaner element and belt replacement at 500 h / 2 years; valve
clearance, mounts, starter, water pump and thermostat at 1500 h. Hours accrue slowly on
an off-grid set — **the calendar limits apply**, so plan an annual service regardless of
hours. Log it in the manual's Table 38.

**Cold weather:** **anti-gel in every diesel fill** unless the tank will certainly be
empty before freezing weather; fuel-pump damage from gelled fuel is not covered by
warranty. Drain the water separator more often. Keep the sump heater powered.

**Disabling it for work:** disconnect the battery negative so it cannot start from a
remote-start command while someone is inside the enclosure. Untick Gen Force on the
Sol-Ark as well.

**Weekly exercise** (Sol-Ark default Monday 08:00, 20 min) keeps the starting battery
and fuel system healthy; leave it enabled. It only runs if the DSE is in Auto.
