# Cheat sheet — solar array maintenance

Standalone reference; not part of the guide sequence or the slide decks. Source: the
installer's customer-training deck (as-delivered version), plus the PV-forecast notes in
page 08. Written for a ground-mounted array on adjustable-tilt racking.

## Annual wash (ground mounts)

Once a year is enough in most conditions; more often if pollen, dust or bird traffic is
heavy. Do it **early morning or late evening**, never on hot glass in full sun.

**Kit:** garden hose that reaches the array, spray nozzle, 3–5 gal bucket, Dawn
dishwashing liquid (1–1.5 cups), window squeegee on a **6–8 ft or longer pole**.

**Method, two panels at a time:**

1. Half-fill the bucket with warm water, add the Dawn, top up until the foam reaches the rim (~¾ full).
2. Wet two panels with the hose.
3. Dip the squeegee, wash the upper panel, rinse. Repeat for the lower panel.
4. Squeegee both dry, windshield-style.
5. Move to the next pair.

**Never:**
- a pressure washer — hose nozzle only
- cold water on a hot panel (thermal shock, same as a windshield)
- abrasive pads, solvents, or anything that could scratch the anti-reflective coating
- standing or leaning on a module

Bifacial modules gain from a clean, light-coloured surface under the array. Keep the ground
beneath a ground mount mowed and clear of tall growth.

## Snow and ice

- Fresh snow: sweep with a soft broom or blow off with a leaf blower **before it refreezes overnight**.
- Ice: **leave it**. Never use warm or hot water; never chip at it. Let the sun melt it.
- Acceptable assist on a ground mount: space heat (e.g. a high-BTU propane heater) placed **under** the array.
- A steep winter tilt (see below) sheds snow on its own and is the best prevention.

## Seasonal tilt (adjustable racking)

If the racking is adjusted, do it on a consistent schedule and treat the SolarAssistant
forecast field as part of the job:

| | Typical angle | When |
|---|---|---|
| Summer | latitude −15° to −20° (not below ~15° on a bifacial ground mount) | early spring |
| Winter | latitude +15° to +20°, or the rack's maximum | early autumn |

**Every time the racking moves, update `Configuration → Advanced → Solar PV → Tilt` in
SolarAssistant** (Disconnect on the Devices panel → edit → Save → Connect). The forecast has
no seasonal model and will be wrong for the half-year otherwise. Tighten the rack hardware
to the maker's torque after each move; check it again before the first winter storm.

## Visual inspection checklist (same visit as the wash)

- [ ] Glass: cracks, delamination, discoloured cells, snail trails
- [ ] Frames and clamps: loose, shifted, corroded
- [ ] Wiring: connectors seated, cables off the ground and out of standing water, no chafe at rack edges, no rodent damage
- [ ] Junction boxes and combiner/disconnects: lids sealed, no water ingress, no discolouration from heat
- [ ] Ground bonding continuous from modules to rack to the inverter ground bar
- [ ] Vegetation: nothing shading any row at the winter sun angle
- [ ] After the wash, compare a clear-day PV peak in SolarAssistant against the forecast — a string that is down shows up as a step below the expected curve

## An MPPT shows 0 V — the three PV disconnect points

Solar reaches the inverters only when **all three** of these are on; any one off kills that
path:

1. **Combiner box at the end of each array** — one DC breaker per 14-panel group (two strings of 7 in parallel).
2. **DC disconnect on the exterior wall** — must be on to send power to the inverters.
3. **Round PV Disconnect switch on the side of each inverter.**

All strings are the same size (7 in series), so on a clear day every MPPT should show a
similar voltage and power. One MPPT at 0 V is a breaker or disconnect; one MPPT low is a
shaded, dirty or failed panel in that group. The single-line drawing engraved on the
exterior wall shows which breaker feeds which MPPT.

## Replacing a damaged panel

> **DC is live whenever there is light on the array — including moonlight.** Breakers
> and disconnects only stop current flowing *past* them; the panels and the wiring on
> the array side of the breaker stay at full string voltage. Treat every conductor as live.

1. Turn **off** the combiner breaker for that 14-panel group **and** the wall disconnect.
2. Remove the plastic cover if fitted and unplug the damaged panel's two MC4 connectors (positive and negative) with an **MC4 disconnect tool** — in a pinch two small flat screwdrivers or needle-nose pliers.
3. Unclamp the panel — mid- and end-clamps take a socket from the sunny side; upper rows may need a ladder laid carefully across the lower row, or a tall ladder from behind.
4. Fit an identical panel; torque clamps to the rack maker's figure (**20 ft-lb** for the Sinclair Designs mounts on this type of build).
5. Reconnect the two MC4s, restore the breaker and disconnect, and confirm that MPPT's voltage and power match its neighbours.
6. If a connector breaks: a wire-nut works electrically in an emergency, but replace it with a **genuine MC4 (Stäubli preferred) as soon as possible** — improvised DC joints are a fire risk.

## After a storm

- Arc-fault alarm (**F63**) after lightning is often a false alarm; clear it manually on the inverter (*Clear Arc Fault*) and watch for recurrence, which points to a real connector fault.
- Walk the array for displaced modules and cable damage before re-energising anything that tripped.
- Check each combiner breaker — a surge can trip one without any visible damage.
