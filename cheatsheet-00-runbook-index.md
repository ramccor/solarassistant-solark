# Runbook — Start here

This is the front page of the runbook for the off-grid solar system. You do not need to
understand how the system works to use it. Find the line that matches what you are
seeing, go to that page, and follow the numbered steps. Each page tells you when to stop
and call for help.

> **⚠ STOP — three rules that apply to every page**
>
> - **Never open an inverter, a battery pack, or the generator's control panel door while
>   anything is running.** The only things you touch are breakers, the round PV switch on
>   the side of each inverter, the power button, the touchscreen, and the generator's
>   buttons.
> - **The solar panels and their wires are live whenever there is light on them — even
>   moonlight.** Turning a breaker off does not make the wires before it safe.
> - **Lights are named by their printed label** (ALM, RUN, DC, AC, Normal, Alarm) and by whether they are steady or flashing — you never need to tell colors apart to use these pages.
> - **If you are not sure, stop and call.** Nothing in this system gets worse by waiting an
>   hour for a phone call. Some things get much worse if the wrong button is pressed.

## What you see → which page

| What you see | Go to |
|---|---|
| House has no power; inverter screens dark, or the indicator labelled **Alarm** is lit | **Batteries** page, Procedure 3 — then **Inverter failed** page if only one inverter is dark |
| Inverter screen shows **Low Batt** (the battery symbol changes from its normal look) | **Batteries** page, Procedure 2 |
| Inverter has switched the house power off to protect the batteries (screen shows the battery symbol changed, or is dark) | **Batteries** page, Procedure 3 |
| On a battery pack, the light marked **ALM** is on steadily and nothing else is lit — or no lights at all | **Batteries** page, Procedure 4 |
| Generator should have started but didn't | **Generator** page, Procedure 2 |
| You want to run the generator now to charge | **Generator** page, Procedure 1 |
| Generator is running but keeps stopping, or the inverter won't take its power | **Generator** page, Procedure 3 |
| The big generator is broken and you have a portable one | **Generator** page, Procedure 5 |
| One inverter's screen is dark or its **Alarm** indicator is lit; the other shows **Normal** | **Inverter failed** page, Procedure 1 |
| Both inverter screens show **F41** or **F29** | **Inverter failed** page, Procedure 1 |
| SolarAssistant shows one inverter column frozen | **Inverter failed** page, Procedure 1 |
| Solar production is low, or one MPPT shows 0 V | **Solar panels** page, Procedure 4 |
| Snow or ice on the panels | **Solar panels** page, Procedure 2 |
| A panel is cracked or damaged | **Solar panels** page, Procedure 5 (call first) |
| It is spring or autumn and the panels need tilting | **Solar panels** page, Procedure 3; **Calendar** page |
| Routine upkeep — what to do this month | **Calendar** page |

## The pages

| Page | File |
|---|---|
| Batteries — low battery, power went out, a pack shut itself off | `cheatsheet-low-battery` |
| Generator — starting it, charging, when it won't run | `cheatsheet-generator` |
| Inverter failed — one inverter down, house still has some power | `cheatsheet-inverter-failure` |
| Solar panels — cleaning, snow, tilt, replacing a panel | `cheatsheet-array-maintenance` |
| Maintenance calendar — each month, and what to keep on hand | `cheatsheet-maintenance-calendar` |
| Technician appendix — reference tables, specs and technician-only procedures (not needed by end users) | `cheatsheet-99-technician-appendix` |

## Who to call

| Who | When | Contact |
|---|---|---|
| **Installer — Ernie Williams, Mainstream Green Solutions**, Lexington TN | First call for anything on these pages | (731) 697-1665 · Ernie.williams@mainstreamgreensolutions.com · www.mainstreamgreensolutions.com |
| **Sol-Ark Technical Support** | Inverter fault codes, settings | support@sol-ark.com — 7 days a week, not 24 h |
| **Pytes** (battery maker) | A pack that will not wake after charging | ess_support@pytesgroup.com |
| **Generator dealer** | Engine faults that will not clear | Number on the generator nameplate |

## Where things are

| Thing | Where |
|---|---|
| Inverter touchscreens and power buttons | On the front of each Sol-Ark inverter |
| Round **PV Disconnect** switch | On the side of each inverter |
| Battery pack lights and buttons | Front of each Pytes pack in the battery rack |
| Solar DC wall disconnect | Exterior wall (single-line drawing is engraved beside it) |
| Combiner boxes (solar breakers) | At the end of each array |
| Generator control panel (DSE) | Inside the generator enclosure, **left rear door** |
| Generator 120 V inlet (sump heater + battery charger) | Power-panel door on the generator |
| Portable generator inlet | 50 A outdoor receptacle (feeds the inverters' GEN inputs) |
| SolarAssistant | `https://pnc-home.us.solar-assistant.io` |
