# Runbook — Solar panels: cleaning, snow, tilt changes, and replacing a damaged panel

Use this page when the panels are dirty, covered in snow or ice, when the solar
production looks low or one part of the array has stopped, when it is time to change
the tilt of the racking for the season, or when a panel is cracked and needs to come
out. It is written for the ground-mounted array on the adjustable Sinclair Designs
mounts. You do not need electrical training to do the cleaning, snow and tilt jobs. The
panel-replacement job involves live DC wiring — read its warnings twice.

> **⚠ STOP — read before touching anything**
>
> - **The panels are live whenever there is light on them — including moonlight.** A
>   breaker or disconnect only stops current flowing *past* it. The panels and the wires
>   on the array side of the breaker stay at full voltage (up to 600 V DC). Treat every
>   cable on the array as live, always.
> - **Never use a pressure washer** on the panels. Hose nozzle only.
> - **Never put cold water on hot glass.** It cracks like a hot windshield. Wash early
>   morning or late evening only.
> - **Never put warm or hot water on ice.** Never chip at ice. Let the sun melt it.
> - **Never stand, sit, kneel or lean on a panel.**
> - **Ladders go across the lower row only, laid flat, the way the installer showed
>   you** — or use a tall ladder from behind the array. Never lean a ladder on a panel.
> - **Do not open the combiner boxes, the wall disconnect, or the inverters.** You only
>   ever turn their handles or breakers.

## What you see → what to do

| What you see | What to do |
|---|---|
| Panels look dusty, coated with a film of pollen, or streaked with bird droppings | Procedure 1 — wash the panels |
| Fresh snow sitting on the panels | Procedure 2 — snow and ice |
| Ice on the panels, or snow that has frozen hard | Procedure 2 — snow and ice (leave the ice) |
| It is early April or early October | Procedure 3 — change the tilt for the season |
| Solar production is lower than it should be on a sunny day, or the inverter shows one MPPT at **0 V** | Procedure 4 — find why part of the array is off |
| A panel is cracked, shattered, or has a burnt-looking spot | Procedure 5 — replace a damaged panel |
| There was a lightning storm or high wind last night | Procedure 6 — after a storm |
| You are at the array anyway (wash day) | Procedure 7 — walk-around inspection |

## Procedure 1 — wash the panels (once a year, more if pollen is heavy)

**You will need:**
- Garden hose long enough to reach every panel
- Spray nozzle for the hose
- 3–5 gallon bucket
- Dawn dishwashing liquid, 1 to 1.5 cups
- Warm water to half-fill the bucket
- Window squeegee on a pole at least 6–8 ft long
- Shoes with grip; the ground under the array gets wet

Do this **early in the morning or late in the evening**, never when the panels are hot in
full sun. Work two panels at a time — one on the top row and the one below it.

- [ ] Half-fill the bucket with warm water. Add 1 to 1.5 cups of Dawn. Top up with water until the foam reaches the rim (the bucket is about ¾ full).
- [ ] Wet two panels with the hose. **You should see** the water sheeting off; if it sizzles or steams, the glass is too hot — stop and come back later.
- [ ] Dip the squeegee in the bucket and wash the top panel. Rinse it with the hose.
- [ ] Do the same for the bottom panel.
- [ ] Squeegee both panels dry, top to bottom, like a car windshield.
- [ ] Move to the next pair and repeat until the whole array is done.
- [ ] While you are there, do Procedure 7 (walk-around inspection).
- [ ] The next sunny day, open SolarAssistant and look at the solar (PV) peak. **You should see** it close to the forecast line. **If not →** one part of the array may be off; go to Procedure 4.

> **⚠ WARNING:** **No abrasive pads, no solvents, no "glass cleaner" sprays.** They
> scratch or strip the anti-reflective coating, which permanently lowers output.

Keep the ground under the array mowed and clear of tall growth. These panels are
"bifacial" — the back side makes power from light bouncing up off the ground, so a clean,
light-coloured surface underneath helps.

## Procedure 2 — snow and ice

**You will need:**
- A soft-bristle broom on a long handle, **or** a leaf blower
- Gloves and boots with grip

**Fresh snow** (fell today, still soft):

- [ ] Clear it **before nightfall, before it refreezes.** Sweep or blow it off from the bottom edge upward. **You should see** the snow slide off in sheets — the steep winter tilt helps.
- [ ] Do not scrape. If the broom drags on something hard, stop — that is ice; see below.

**Ice, or snow that has frozen overnight:**

- [ ] **Leave it.** Let the sun melt it. This is the only safe option.
- [ ] If you must speed it up, you may place a space heater (for example a high-BTU propane heater) on the ground **under** the array so warm air rises against the back of the panels. Never aim heat or flame at the glass. Never leave it unattended.

> **⚠ WARNING:** **Never pour warm or hot water on an iced panel, and never chip or
> hammer at ice.** Both crack the glass. A cracked panel is Procedure 5 and a new panel.

The steep winter tilt (Procedure 3) sheds snow on its own most of the time. If you are
getting snow build-up every storm, check the tilt was actually changed in October.

## Procedure 3 — change the tilt for the season (early April and early October)

The racking is adjustable. The panels sit flatter in summer (about 15°) and steeper in
winter (about 55°) to catch the low winter sun and shed snow. The SolarAssistant
forecast needs to be told the new angle every time — it has no idea the rack moved.

**You will need:**
- The Sinclair mount's adjustment hardware and the mount's own instruction sheet (part: see Sinclair Designs manual / dealer)
- Socket or wrench set that fits the mount's pivot bolts
- Torque wrench (clamp torque on these mounts is **20 ft-lb**)
- **A helper** — the panels are heavy and the mount must not swing free
- A phone or laptop to update SolarAssistant afterwards
- Gloves

- [ ] Pick a calm, dry day. Do **not** do this in wind.
- [ ] With your helper holding the frame, loosen the pivot bolts on one mount per the Sinclair instructions.
- [ ] Move the mount to the new angle: **about 15° in April** (nearly flat, but not flatter than 15°), **about 55° in October** (or as steep as the mount allows if it stops short).
- [ ] Tighten the pivot bolts. Then check every panel clamp on that mount with the torque wrench at 20 ft-lb. **You should feel** the wrench click without the bolt turning further.
- [ ] Repeat for the other two mounts. All three must be at the same angle.
- [ ] Walk the array. **You should see** no cables pinched or stretched by the move, and no panel shifted in its clamps. **If not →** fix it before leaving.
- [ ] On SolarAssistant, open **Configuration → Devices** and click **Disconnect**. Then **Configuration → Advanced → Solar PV → Tilt**, type the new angle (15 or 55), click **Save**, go back to **Configuration → Devices** and click **Connect**. **You should see** the inverter columns on the status page start updating again within about 15 seconds. **If not →** click Connect again, then call the installer if still blank after 2 minutes.
- [ ] Over the next two or three sunny days, check that the forecast line and the actual solar line in SolarAssistant sit close together.
- [ ] Before the first winter storm, check the clamps and pivot bolts once more.

> **⚠ WARNING:** **Do not skip the SolarAssistant step.** Left at the old angle, the
> forecast is wrong for six months — it tells you the wrong thing about whether the
> generator will need to run tonight.

## Procedure 4 — find why part of the array is off (an MPPT at 0 V, or low production)

The array is wired as groups of 14 panels: a row of 7 along the bottom of a mount joined
in a "string", in parallel with the 7 above it. Each 14-panel group feeds one **MPPT**
(a solar input on the inverter — there are three per inverter) through its own breaker.

**You will need:**
- A sunny day (this cannot be judged in cloud or at night)
- A flashlight

There are **three** places solar power can be switched off. **All three must be on.**

![Ground-mount array: 7 bottom panels in series, paralleled with the top 7 at the ends, one 600 V DC breaker per 14 panels](images/cheat-array-string-layout-photo.png)
*Each mount carries groups of 14 panels. The text box over the lower row of panels explains it: the 7 bottom panels are wired in series, joined to the top 7 at the ends, with one breaker in the combiner box at the end of the array serving each group of 14.*

- [ ] On the inverter screen (or SolarAssistant), look at the three MPPT readings on each inverter. On a sunny day **you should see** all six showing similar voltage and similar power. Note which one is at 0 V or far below the others.
- [ ] **Combiner box** at the end of that array: open its cover and look at the two breakers. **You should see** both in the ON position. **If not →** push the tripped one firmly OFF, then ON. Wait 1 minute and recheck the MPPT reading.
- [ ] **Wall disconnect** on the outside wall of the house: **you should see** the handle in ON. **If not →** turn it on.
- [ ] **Round PV Disconnect switch** on the side of each inverter: **you should see** it in ON. **If not →** turn it on. The inverter's indicator labelled **DC** should come on within a minute.
- [ ] If all three are on and the MPPT is still at 0 V, the breaker may be tripping again as soon as it is reset — that is a wiring fault. **Stop and call the installer.**
- [ ] If the MPPT is *low* but not zero, one panel in that group is shaded, dirty, or failing. Walk that group: look for shade from a tree or post, a dirty panel, or a cracked one (Procedure 5).

The single-line drawing engraved on the exterior wall shows which breaker feeds which
MPPT — use it to match the reading to the right combiner breaker.

## Procedure 5 — replace a damaged panel

> **⚠ WARNING:** **This job touches live DC wiring.** Turning the breakers off stops the
> power from reaching the house — it does **not** make the panel cables safe. Each panel
> still makes around 50 V and a string makes up to 350 V in daylight, **including
> moonlight**. If you have not been shown this job by the installer, **call them** and
> leave the panel disconnected-at-the-breaker until they come. A cracked panel that is
> still wired is not an emergency in itself; a shock is.

**You will need:**
- One identical replacement panel — **Trina TSM-NE09RC.05, 410 W**. If none is available, a panel of the same series and size, **approved by the installer before it goes in**
- MC4 disconnect tool (the little plastic two-prong unlocking tool). In a pinch: two small flat screwdrivers or needle-nose pliers
- Socket set that fits the Sinclair mid- and end-clamps
- Torque wrench set to **20 ft-lb**
- Ladder (to lay across the lower row, or a tall one from behind)
- Thick dry gloves, safety glasses, dry boots
- Spare genuine **MC4 connectors, Stäubli brand** (in case one breaks)
- Flashlight
- A second person

- [ ] Find which combiner breaker serves the damaged panel's group of 14 (engraved drawing on the wall, or count along the mount).
- [ ] Turn that breaker **OFF** in the combiner box at the end of the array.
- [ ] Turn the **wall disconnect OFF**.
- [ ] At the damaged panel, remove the plastic cover under it if one is fitted.
- [ ] Using the MC4 tool, unplug the panel's **two** connectors — one positive, one negative. **You should see** each connector come apart with the tool pressed in; they do not pull apart without it.
- [ ] Unbolt the mid-clamps and end-clamps holding that panel. They are reached from the sunny side with a socket. Top-row panels: lay the ladder across the bottom row as shown, or work from a tall ladder behind the array. Your helper steadies the panel as the last clamp comes off.
- [ ] Lift the panel out. Set it face down on cardboard, away from the work.
- [ ] Lift the new panel in. Refit the clamps and **torque each one to 20 ft-lb**.
- [ ] Plug the two MC4 connectors back in — positive to positive, negative to negative (they only fit one way). **You should hear** each one click.
- [ ] Refit the plastic cover.
- [ ] Turn the wall disconnect back **ON**, then the combiner breaker **ON**.
- [ ] On the inverter screen or SolarAssistant, **you should see** that MPPT's voltage and power come back to match its neighbours within a minute. **If not →** re-check both connectors, then the breaker. If still dead, call the installer.

> **⚠ WARNING:** **If a connector breaks,** a wire-nut will make it work for a day in an
> emergency, but improvised DC joints are a fire risk. **Fit a genuine MC4 (Stäubli) as
> soon as possible** — same day if you can.

## Procedure 6 — after a storm

**You will need:** a flashlight; nothing else.

- [ ] Walk the whole array. **You should see** every panel in place, no cables hanging or on the ground, no debris on the glass. **If not →** Procedure 5 for a damaged panel; call the installer for cable damage — do not touch loose cables.
- [ ] Open each combiner box cover and check the breakers. A lightning surge can trip one with no visible damage. **If one is OFF →** push it fully OFF then ON.
- [ ] Look at the inverter screens. If you see an **Arc Fault** alarm (code **F63**) after a lightning storm, it is often a false alarm. Clear it: ⚙ Settings → the arc-fault setting → **Clear Arc Fault**. **You should see** the alarm go away and the DC light return. **If it comes back** within a day, a connector is genuinely damaged — call the installer.

## Procedure 7 — walk-around inspection (same visit as the wash)

**You will need:** a flashlight, a notebook or your phone for photos.

- [ ] Glass: any cracks, bubbling or peeling inside the glass, cells that look darker or scorched compared with their neighbours, fine "snail trail" lines running across cells.
- [ ] Frames and clamps: anything loose, shifted, or rusty.
- [ ] Wiring: connectors pushed fully together, cables tied up off the ground and out of puddles, no rubbing on the rack edges, no chewed insulation (rodents).
- [ ] Junction boxes (the small sealed boxes on the back of each panel), the combiner boxes and the wall disconnect: lids sealed, no water inside, no heat marks (a discoloured or bubbled patch on the plastic).
- [ ] The bare ground wire runs from the panels to the rack to the house without a break.
- [ ] Nothing has grown up that will shade any row when the winter sun is low.
- [ ] Photograph anything you are not sure about and send it to the installer.

## Stop and call for help when…

- A combiner breaker trips again right after you reset it.
- Any cable is cut, chewed through, hanging, or lying on the ground.
- You smell burning, or see a dark heat mark on a junction box or connector.
- A panel is cracked and you have not been shown the replacement job.
- An arc-fault alarm keeps coming back after you clear it.
- Anything on the mounts is bent, or a pivot bolt will not tighten.
- You are not sure. It is always fine to call.

## Who to call

| Who | Contact |
|---|---|
| Installer — Ernie Williams, Mainstream Green Solutions, Lexington TN | (731) 697-1665 · Ernie.williams@mainstreamgreensolutions.com · www.mainstreamgreensolutions.com |
| Sol-Ark Technical Support (inverters) | 7 days a week, not 24 h — support@sol-ark.com |

## Reference — for the technician

**Sources:** installer's customer-training deck (as-delivered version); page 08 PV-forecast
notes; tilt analysis on the site page.

**Seasonal tilt.** Two-switch schedule, PVGIS-derived: summer latitude −15° to −20° (not
below ~15° on a bifacial ground mount, to keep rear-side gain and rain shedding), winter
latitude +15° to +20° or the rack's maximum. For this site: ≈15° early April, ≈55° early
October; ~+4.5 % front-side annual yield vs fixed 32°, Nov–Jan each up ~10–12 %. The
SolarAssistant forecast has no seasonal model; `Configuration → Advanced → Solar PV →
Tilt` must be updated on every move (Disconnect on the Devices panel → edit → Save →
Connect). Re-torque rack hardware after each move; recheck before the first winter storm.

**Array wiring.** Strings of 7 in series along the top and bottom of each mount; top
and bottom strings paralleled at the ends; one 600 V DC breaker per 14-panel group in a
Midnite combiner box at the end of each array. Three series switch points: combiner
breaker → exterior wall disconnect → inverter PV disconnect. All strings are equal, so on
a clear day all MPPTs should read alike; 0 V = switch point open; low = shade, soiling or
a failed module in that group. The single-line drawing is engraved on the exterior wall.

**Panel replacement.** Module: Trina TSM-NE09RC.05 410 W (Voc 50.1 V, 7 in series ≈
350 V, up to ~390 V cold). Sinclair Designs mid- and end-clamp torque 20 ft-lb. MC4
connectors: Stäubli preferred; wire-nut joints are emergency-only.

**Bifacial note.** 65 ±10 % bifaciality; keep the ground under the array mowed and
light-coloured; do not flatten below ~15° in summer.

**Storm.** F63 Arc_Fault after lightning is frequently spurious; clear manually
(*Clear Arc Fault*) and watch for recurrence, which indicates a real connector fault.
