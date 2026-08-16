# 09 — Sol-Ark ↔ SolarAssistant terminology

[Index](README.md) · Prev: [08 — Recommended settings](08-recommended-settings.md)

The two products name the same inverter registers differently. An installer commissioning
a site will have both open — the MySolArk app to change a setting, SolarAssistant to see
whether the change landed — and the labels rarely match.

This page maps one to the other. It is a naming reference, not a settings recommendation:
for the values at a real site see [07 — Worked example](07-worked-example.md), and for
which settings are worth changing see [08 — Recommended settings](08-recommended-settings.md).

> **Labels drift between app versions.** These were captured from the MySolArk app in
> August 2026. Sol-Ark renames fields between releases; the *registers* are stable, the
> *labels* are not. If a name below is not on your screen, match by position and range
> rather than assuming the setting is missing.

> **What is screen-dependent.** MySolArk hides whole blocks of fields behind a toggle —
> `Time Of Use`, `Gen Charge`, and the `Grid Mode` profile all reveal or conceal settings
> below them. A field being absent usually means the thing that reveals it is switched
> off, not that your firmware lacks it. The MySolArk columns below are drawn from two
> Sol-Ark 15K sites, one off-grid and one grid-tied, so that the toggle-dependent screens
> appear here in both states.

## The two that catch people out

| MySolArk | SolarAssistant | Why it matters |
|----------|----------------|----------------|
| **Limited power to Load** | **Zero export to load** | The same work mode under two unrelated names. Nothing in either string suggests the other |
| **Grid Start %** | **Start grid charge capacity** | On a site whose generator feeds the grid input, this is the setting that actually starts charging — not the generator settings. See [the charge-path note](#a-note-on-generator-settings) |

## Battery Setting

| MySolArk | SolarAssistant |
|----------|----------------|
| Batt Type → `Lithium Batt` | Battery → Type → `Lithium` |
| BMS Lithium Batt Mode (0–20) | Battery → Lithium protocol — `0` is CAN |
| Battery Capacity (0–9999 Ah) | Battery → Capacity |
| Max A Charge (0–275 A) | Charging → Max charge current |
| Max A Discharge (0–275 A) | Charging → Max discharge current |
| Batt Shutdown % | Work mode → Output shutdown capacity |
| Batt Low % | Work mode → Stop battery discharge capacity |
| Batt Restart % | Work mode → Start battery discharge capacity |
| Grid Charge | Work mode → Grid charge |
| Grid Start % (10–90%) | Work mode → Start grid charge capacity |
| Grid Start A (0–275 A) | Charging → Max grid charge current |
| Gen Charge | Charging → Generator charge |

`Batt Empty V`, `Batt Resistance`, `Batt charging efficiency`, `Activate Battery`,
`Grid Signal`, `Gen Signal`, `Gen Force`, and `Low Noise Mode` have no SolarAssistant
equivalent — SolarAssistant does not surface them.

## Grid Settings

| MySolArk | SolarAssistant |
|----------|----------------|
| Grid Frequency (`50HZ` / `60HZ`) | Grid → Frequency |
| Grid Type → `120/240V Split Phase` | Grid → Type → `120/240 V two phase` |
| Normal Connect → Low / High voltage | Grid → Voltage limits |
| Normal Connect → Low / High frequency | Grid → Frequency limits |

Everything else on this screen — `Grid Mode`, `INV Output voltage`, the whole
*Reconnect After Trip* block, `Reconnection Time`, `PF`, and the `HV1`–`HV3` / `LV1`–`LV3` /
`HF1`–`HF3` / `LF1`–`LF3` trip points with their `-T` timers — is grid-protection
configuration that SolarAssistant does not read or display. Change it in MySolArk only.

> **`Grid Mode` selects a utility interconnection profile, and it changes what else is on
> this screen.** An off-grid site may sit on a generic profile; a grid-tied site is
> normally set to whatever its utility requires — a `SRD-UL1741`-style entry in North
> America. Selecting one narrows the trip windows and can expose an additional block of
> frequency-watt fields (`start freq f`, `stop freq f`, `start delay f`, `stop delay f`)
> that a generic profile hides. None of it reaches SolarAssistant either way.

## System Work Mode

| MySolArk | SolarAssistant |
|----------|----------------|
| Work Mode → `Limited power to Load` | Work mode → Mode → `Zero export to load` |
| Max Solar Power (W) | Work mode → Max solar power |
| Max Sell Power (W) | Work mode → Max sell power |
| Energy pattern → `Batt First` | Work mode → Energy pattern → `Battery first` |
| Time Of Use | Work mode → Use timer — **see below** |

`Solar sell` and `Zero export power` have no SolarAssistant equivalent.

### What Time Of Use unfolds

Switching `Time Of Use` on expands the screen rather than opening a new one, and the
structure is worth knowing before you go looking for it:

| MySolArk control | What it is |
|------------------|------------|
| `Mon.` … `Sun.` | Day selectors the schedule applies to |
| **`Charge` → `Time 1`…`Time 6`** | **Which intervals may charge.** A highlighted slot is the manual's "☑ Charge" |
| `Sell` → `Time 1`…`Time 6` | Which intervals may sell |
| `Time N` | Start time of slot N |
| `Power N` (0–14000 W) | Power limit for slot N |
| `Battery SOC N` (0–100%) | Target SOC for slot N |

The six slots are a **series of start times**, not start/end pairs — each runs until the
next one begins, so the six together tile the whole day and there is no gap to leave
unconfigured.

> The `Charge` row is the control behind
> [the trap described below](#moving-the-95-cutoff-means-enabling-time-of-use). It is easy
> to read the row as decorative: the slots look like labels rather than toggles, and
> nothing on screen states that an unhighlighted slot forbids charging.

MySolArk offers two further work modes, `Grid Selling` and `Limited to Home`. Their
SolarAssistant names are **not mapped here** — only the mode a site is actually running can
be confirmed by comparing the two screens, and guessing at the others would defeat the
point of this page. Set the mode in MySolArk, then read back what SolarAssistant calls it.

## SmartLoad

The screen name gives no hint that it holds the generator wiring configuration.

| MySolArk | SolarAssistant |
|----------|----------------|
| SmartLoad Setup → `Generator Input` | Auxiliary → Aux port → `Generator input` |
| GEN connect to Grid input | Auxiliary → Generator connected to grid input |

`AC couple on load side` / `AC couple on grid side` have no SolarAssistant equivalent.

## Basic Setting

Display and housekeeping. Almost none of it maps, but one row matters:

| MySolArk | SolarAssistant |
|----------|----------------|
| **`Lock out all changes`** | No equivalent — **but see below** |
| `Time Syncs` | No equivalent |
| `ARC Setup`, `BEEP`, `AM/PM`, `Auto Dim` | No equivalent — display and arc-fault behaviour |
| `Factory Reset` | No equivalent |

> **`Lock out all changes` is the inverter-side write lock.** SolarAssistant has its own
> write control — the MQTT `Allow setting changes` flag on
> [page 08](08-recommended-settings.md#1-enable-mqtt-and-home-assistant-discovery) — and
> the two are independent. If writes are failing from SolarAssistant or Home Assistant,
> check both. Neither reports the other's state.

## Advanced Setting

| MySolArk | SolarAssistant |
|----------|----------------|
| Grid peak-shaving + Grid peak-shaving power | Grid → Peak shaving |
| Equipment mode (`Master` / `Slave`) | Parallel role |
| Modbus SN (1–16) | Modbus № |

> **This is where the numbering gotcha becomes visible from both sides.** MySolArk shows
> each inverter's own `Equipment mode` and `Modbus SN`; SolarAssistant numbers its device
> list independently. The two do not correspond — see
> [00 — Overview](00-overview.md) and the worked example in
> [07](07-worked-example.md#inverters).

## Where the two disagree

**`Time Of Use` vs `Use timer`.** MySolArk is authoritative for its own hardware. A site
whose inverter reports Time Of Use **off** can still have SolarAssistant render
`Use timer` as **checked**. The numeric registers agree exactly — it is this boolean that
is misreported, and it appears to be a driver bug rather than a configuration problem.

Check MySolArk before concluding that a work-mode timer is active. If SolarAssistant shows
`Use timer` checked and MySolArk shows Time Of Use off, believe MySolArk.

## A note on generator settings

On a site where the generator feeds the **grid input** (`GEN connect to Grid input`
enabled, `Grid Charge` enabled), the inverter treats a running generator as grid. Both the
trigger and the current limit therefore come from the **grid** fields:

| What you are trying to set | The field that actually does it |
|----------------------------|---------------------------------|
| SOC at which generator charging starts | `Grid Start %` |
| Charge current drawn from the generator | `Grid Start A` |

**There is no stop setting to find.** `Grid Charge` → `Grid Start %` → `Grid Start A` is
the entire grid-charge group; no `Grid Stop %` exists. Charging ends on **current taper,
not an SOC setpoint** — the manual puts generator charging as continuing "until the battery
bank accepts 5% of its rated capacity in Amperes," which it equates to roughly 95% SOC.
On a 1200 Ah bank that is about 60 A of acceptance.

> **The manual addresses the grid-input case directly.** For a generator connected to the
> grid input it states the system uses the `Start V` / `Start %` / `A` conditions and stops
> "charging at 95% SOC," adding: *"Adjustable upper limit if Time of Use is enabled."*
> Elsewhere it calls the 95% ceiling *"a non-modifiable upper limit unless Time of Use is
> enabled and programmed."*
>
> The practical consequence: an alert or automation that waits for 100% while on generator
> power will never fire.

The generator-specific settings are inert on such a site. SolarAssistant will still report
a `Max generator charge current` and generator start/stop capacities, and they will still
hold whatever values they were commissioned with — but nothing reads them while charging
runs through the grid path. **Lowering a generator charge-current limit to throttle a
generator does nothing; change `Grid Start A` instead.**

This is also why the table above has no row for `Max generator charge current`. With
`Gen Charge` toggled **off**, MySolArk hides its dependent generator-charge fields, so
there is no visible Sol-Ark label to map onto it. Enabling `Gen Charge` to reveal them is
a real configuration change — it adds a second charging path — not a display toggle.

## Moving the 95% cutoff means enabling Time of Use

The 95% ceiling is the only stop condition, and Time of Use is the only way to move it.
That makes it a package deal, because enabling TOU also changes when the generator is
permitted to start at all:

> "If 'Time of Use' (TOU) is enabled, a time to charge from that GRID or GEN source MUST be
> designated. **'☑ Charge' must be checked on desired time intervals, otherwise the
> generator will not start automatically even if the Start V or Start % condition has been
> met.**"
>
> — Sol-Ark 15K-2P-N manual, generator and grid charge settings

> **This is a silent failure.** With TOU enabled and `Charge` unticked on an interval, the
> generator will not auto-start for the length of that interval no matter how far SOC
> falls. There is no fault code and no alarm — the symptom is simply a generator that does
> not run, and on a multi-hour interval that is a long time to spend diagnosing it.

If you enable TOU to lower the cutoff:

- **Tick `Charge` on every interval where the generator should be able to start**, not only
  the ones you expect it to need.
- **Verify in MySolArk after saving.** SolarAssistant renders `Use timer` as checked either
  way — see [Where the two disagree](#where-the-two-disagree) — so it cannot confirm that
  the change took, or that TOU was off beforehand.
- **The work-mode timer goes live at the same time.** Its stored slot values are inert while
  TOU is off; once TOU is on they take precedence over the work-mode settings, and anything
  writing those can be silently overridden.

A low-SOC notification will fire during such a window, but it looks identical to "generator
running and not keeping up." Knowing which one you are looking at means checking whether the
generator is actually running, not just how low the battery is.

---

[Index](README.md)
