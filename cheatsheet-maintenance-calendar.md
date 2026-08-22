# Maintenance calendar — off-grid solar, battery and generator

Standalone reference; not part of the guide sequence or the slide decks. Sources: the
Wildcat Patriot / Hyundai O&M manual (Table 37 service schedule), Sol-Ark *15K
Installation Manual* Rev. 13, the installer's training deck, and the tilt analysis on the
site page. Tilt dates assume the two-switch schedule (15° summer / 55° winter). Generator
hours accrue slowly on an off-grid site, so the **calendar limits in Table 37 govern**, not
the hour counts.

## Recurring — not tied to a month

| Every | Item | Source |
|---|---|---|
| **Day** (or each site visit) | Glance at SolarAssistant: every inverter column live, battery SOC sensible, PV peak matches the day. Battery Tender LED **green steady**. | — |
| **Monday 08:00** | Sol-Ark generator exercise, 20 min. Confirm it ran (gen energy on the day's chart). If it did not: DSE in Auto? Fault latched? Two-wire loop? | Sol-Ark §4 |
| **Week** | Bank reaches **100 % SOC** at least once (needs a clear day — generator stops at 95 %). | deck |
| **Before every generator run** (walk-around) | Fuel, oil, coolant leaks; oil and coolant level; air-cleaner restriction indicator; **drain fuel/water separator**; hoses and clamps. | Table 37 daily |
| **After every generator run** | Check the DSE for fault messages; note hours in the log. Confirm it went back to **Auto**. | manual |
| **Every diesel fill** (Oct–Mar, or any fill that may still be in the tank by October) | **Anti-gel** treatment. | deck |
| **Every racking adjustment** | Update `Advanced → Solar PV → Tilt` in SolarAssistant; re-torque rack hardware. | page 08 |

## By month

### January
- Cold-start watch: after each auto-start check the DSE for *Start Failure*; sump heater and Battery Tender both powered.
- Fresh snow: broom / leaf blower before it refreezes. Ice: leave it.
- Review December's generator hours and fuel against expectation; compare PV actual vs forecast on a clear day (winter tilt should track closely).

### February
- Nothing scheduled. Keep the daily and weekly items going; fuel level check — winter runs burn 2–3.6 gal/h.

### March
- Order wash supplies and any MC4 spares before the spring visit.
- Check the combiner boxes and wall disconnect after winter storms — look for a tripped breaker, water ingress, rodent damage.

### April — *spring changeover*
- **Early April: racking to summer tilt (≈15°)**, torque clamps (20 ft-lb on Sinclair mounts), **set Tilt in SolarAssistant**.
- **Annual panel wash** (early morning or evening, warm Dawn solution, pole squeegee, hose nozzle only) — do it the same day as the tilt change while you are at the array.
- **Full array inspection** (checklist on the maintenance sheet): glass, clamps, cabling, J-boxes, bonding, vegetation at the winter sun angle.
- Validate the forecast over 2–3 clear days after the tilt change.

### May
- **Generator annual service — the 250 h / 1 year column of Table 37** (do it in spring so the set is fresh for winter): primary and secondary fuel filters, belt check and adjust, centrifugal filter clean, oil and filter if 500 h is near or the oil is over a year old. Radiator fins. Log in Table 38.
- Load-test the generator: Gen Force from the Sol-Ark, let it qualify and charge for 30 min under real load, then release and confirm it returns to Auto.
- Mow and clear under the array — the bifacial rear side wants a light, open surface.

### June
- Check inverter and battery enclosure ventilation; clean filters and fans; the Sol-Ark derates above 75 °C internal.
- Review the Pytes pack cards in SolarAssistant for any pack drifting in voltage or temperature from the others.

### July
- Fuel: if the tank will not be empty by October, it needs anti-gel at the next fill — plan it now.
- Mid-season vegetation check under and around the array.

### August
- Nothing scheduled. Good month for an annual firmware check: Sol-Ark (COMM/MCU must match across units — schedule updates with Sol-Ark, never one unit alone), SolarAssistant, Pytes.
- Review SolarAssistant alerts/automations still fire (trigger a test notification).

### September
- **Generator pre-winter check:** starting battery load test or replace if >4 years old; coolant strength; anti-gel added; spare fuel filters on the shelf; **order oil and filters** if the 500 h / 2 year items (air-cleaner element, belt replacement) fall this year.
- Inspect the generator's 120 V inlet cord, the outlet it plugs into, and the Battery Tender clips and lead.

### October — *winter changeover*
- **Early October: racking to winter tilt (≈55°)**, torque clamps, **set Tilt in SolarAssistant**.
- **By 15 October: confirm the generator's 120 V NEMA 5-15 inlet is plugged in and live** — it powers the magnetic sump heater (needed below 32 °F) and the built-in battery charger. Verify with a meter or by feeling the sump after a cold night. Confirm the circuit feeding it stays up at low SOC.
- Battery Tender: green steady.
- Confirm the DSE is in **Auto**, no latched faults, E-stop released.
- Raise the generator Start % or lower Max Gen Runtime if last winter's runs were too long or too short (see the generator sheet).
- Validate the forecast over 2–3 clear days after the tilt change.

### November
- First sub-freezing night: check the sump heater is actually warm and that the first cold auto-start succeeds; watch for *Start Failure* on the DSE.
- Drain the water separator — condensation increases with temperature swings.
- Snow kit staged: soft broom or leaf blower reachable.

### December
- Fuel level and anti-gel confirmed before any long cold spell.
- Review Shutdown / Restart / Start % against the expected winter deficit; low-SOC alert tested.
- Year-end: generator hours and fuel used logged; decide whether next May's service is the 250 h or the 500 h column.

## Two-year and longer

| Interval | Item | Source |
|---|---|---|
| 500 h / 2 years | Generator: air-cleaner element, fan belt replacement, oil and filter (if not done on hours) | Table 37 |
| 1500 h | Generator: valve clearance, mounts, starter, charging alternator, water pump, thermostat | Table 37 |
| 3–5 years | Generator starting battery | general practice |
| 10 years | Pytes and Sol-Ark warranties end; plan capacity review | deck |
| 25 years | Panel power warranty (≥80 %) | deck / datasheet |
