# MOERC (Metal Oxide Electrolysis Refinement Chamber)
**Sand → Silicon (200 g target) | 120 V + Battery | <$10k v0.1**

> Earth‑first, ISRU‑ready benchtop line to convert ~1 kg of oxide feed (beach sand, crushed rock, or simulant) into ~200 g of refined silicon using **molten oxide electrolysis (MOE)** followed by **vacuum refining** and **ingot casting**. No external chemical reductants (no carbon, no chlorosilanes). Designed around off‑the‑shelf parts and minimal fabrication.

---

## 0) At‑a‑glance
- **Batch size:** ~1 kg dry feed (SiO₂‑dominant) → **~200 g Si** (learning target; improved yields with practice)
- **Core process:** MOE (Fe→Si→Al staging) → vacuum refining (P removal) → directional solidification
- **Operating temps:** **1600–1700 °C** MOE cell; **1600–1900 °C** vacuum refine; **1450–1550 °C** casting
- **Power:** 120 V AC, 15–20 A; **battery/inverter (≥1.8 kW)** inline for ride‑through; optional solar recharge
- **Atmosphere:** low‑leak sealed hot‑zone; argon backfill (closed‑loop reclaim); O₂ vent/capture
- **Footprint:** bench stack, approx 0.8 m × 0.6 m × 1.2 m total for all modules
- **Safety:** high‑T, high‑brightness, O₂ evolution, off‑gas management; multiple interlocks & E‑stop

---

## 1) System Architecture (modules)
1. **Feed Prep & Autofeed**
   - Hopper + auger feeder (vacuum‑tolerant), inline dryer (150–250 °C), screen (≤250 µm target), optional jaw‑crusher for rocks.
2. **MOE Cell (Melter + Electrolyzer)**
   - Insulated hot‑zone, crucible/liner set, refractory‑metal electrodes, 1600–1700 °C setpoint, staged potential for **Fe→Si→Al**.
3. **Phase Separation**
   - Weir/sump geometry to isolate Fe first, then collect molten Si away from slag/Fe (avoid Fe–Si alloying).
4. **Vacuum Refining Pot**
   - Dedicated vessel; 1600–1900 °C at ≤ 10 Pa; cold‑traps on exhaust to capture **SiO** and **P‑species**.
5. **Ingot Casting**
   - Directional solidification (Si₃N₄‑coated crucibles) for multicrystalline bricks; optional small float‑zone head for rods.
6. **Gas & Vacuum Skid**
   - Argon loop (buffer tank, dryer, filter), O₂ vent/capture, vacuum pump (HF‑free process), baffles/cold‑traps.
7. **Controls & Sensing**
   - PID/PLC, two‑color pyrometry, **LIBS** (pre‑feed/melt fingerprint), **OES** (process), **RGA** (vac/off‑gas), interlocks.
8. **Power & Energy**
   - 120 V mains → inverter/UPS (≥1.8 kW continuous) → heater supplies; DC bus for controls; optional PV input.

---

## 2) Bill of Materials (indicative, USD)
_Prices are ballparks (new/COTS). Substitute equivalents as available._

### 2.1 Hot‑Zone & MOE Cell (~$3,150)
- High‑temp insulation kit (alumina fiber boards/blanket, 1700 °C class), panels + fasteners — **$350**
- Modular steel frame (80/20 or welded), panels, hardware — **$250**
- **Crucibles/liners:** primary **ZrO₂** liner (1.5–2 L), backup **Al₂O₃** liners (x2) — **$400**
- Refractory‑metal electrodes: **W** cathode set + **Mo** spares; **IrO₂‑coated** inert anode option (or consumable C anode minimized) — **$900**
- Induction/element heater set: high‑temp **MoSi₂** elements (1700 °C rating) w/ holders OR compact induction coil + 3–5 kW driver (120 V input PFC) — **$950**
- Thermography: dual **two‑color pyrometers** (melt & wall), 600–2000 °C — **$300**
- Fixtures: ceramic feed‑port, viewports (UV‑grade fused silica), fast‑shut baffles — **$150**

### 2.2 Vacuum Refining Vessel (~$1,750)
- Small high‑vac furnace can (stainless shell, water‑cooled feedthroughs) — **$600**
- Heater: MoSi₂ element set or induction coil insert — **$450**
- Cold‑trap assembly (water‑cooled finger + removable cryo cup) — **$250**
- Vacuum hardware: KF25/KF40 set, valves, gauge (Pirani + capacitance manometer) — **$300**
- Si crucible (graphite or high‑density SiC **not in contact** with silica stage) — **$150**

### 2.3 Gas & Vacuum (~$1,600)
- Rotary vane pump (5–8 m³/h) + backing filter — **$700**
- Dry scroll (used or small new) _optional upgrade_ — **$700**
- Argon loop: 20–40 L buffer tank, 0.1 µm filter, desiccant dryer — **$200**

### 2.4 Feed & Casting (~$900)
- Hopper + auger (stainless screw, NEMA 17/23 stepper, driver) — **$300**
- Inline dryer (500 W cartridge + PID, 150–250 °C) — **$150**
- Screens (250 µm, 100 µm), small jaw‑crusher (benchtop) — **$250**
- DS casting station: Si₃N₄‑coated quartz crucibles (2–3), mold base & slow‑cool plate — **$200**

### 2.5 Controls & Sensing (~$1,900)
- PLC or industrial micro (e.g., Codesys/Compact PLC), IO modules, SSRs/contactors, E‑stop — **$600**
- **LIBS** mini head (OEM pulsed laser + gated spectrometer, 200–900 nm) — **$800** _(entry‑level; upgrade later)_
- **OES** spectrometer (300–900 nm, fiber, lens) — **$250**
- **RGA** (bench quadrupole, 1–100 amu, used/reconditioned) — **$250**

### 2.6 Power & Energy (~$1,500)
- 120 V line conditioner/UPS **or** portable power station (≥1.8 kW cont., ~1.5 kWh) — **$1,000**
- PDU, breakers, cabling, GFCI, ground kit — **$300**
- Optional 400–600 W PV input cabling for recharge — **$200**

**Subtotal (new parts): ~\$10,800**  
**Targeted v0.1 under‑\$10k strategies:** source used/auction items for RGA/pump/UPS (–\$800 to –\$1,500); choose resistance elements over induction (–\$300); use a single pyrometer (–\$150); DIY frame (–\$200). Practical **v0.1 BOM ≈ \$8.8–9.8k**.

---

## 3) Step‑by‑Step Build

### 3.1 Frame & Insulation
1. Build a rigid frame (80/20 extrusion or angle steel). Interior clear volume for hot‑zone: ~200 mm Ø × 250 mm H.
2. Line with 1700 °C fiber boards; add blanket layers; install reflective shields (Mo or W foil) with standoffs.
3. Add service ports: feeder entry, viewport, pyrometer peeks, electrode feedthroughs, gas ports. Keep leak paths short; use ceramic bushings.

### 3.2 Heater & Hot‑Zone
1. **Option A – MoSi₂ elements:** Install 3–4 elements around the liner; wire to SSRs/transformer per vendor specs; keep sightlines to melt.
2. **Option B – Induction:** Wind water‑cooled copper coil around liner zone; mount driver; ensure RF shielding/grounding.
3. Install primary **ZrO₂** liner (melter) nested in a structural setter. Place **W** cathode tip ~10–20 mm above floor sump; mount anode opposite wall (prefer inert anode or protected graphite with minimal exposure).

### 3.3 Phase Separation Geometry
1. Machine/fit a **weir** that lets light slag overflow to a slag pocket while dense Fe collects in a **deep sump** under cathode.
2. Add a **Si collection pocket** isolated from Fe sump by a sill. Later, a tilting ladle or tap hole can draw Si to a transfer ladle.

### 3.4 Vacuum Refining Pot
1. Assemble small vacuum can with internal crucible support and heater.
2. Fit cold‑trap on exhaust path; add baffles cooled by water loop. Route to pump via isolation valve; include pressure gauges at can & foreline.

### 3.5 Gas/Vacuum Skid
1. Mount rotary vane pump on vibration pads; plumb KF manifold to MOE cell and refining pot with isolations and check valves.
2. Build Argon loop: buffer tank → dryer → filter → mass‑flow controller → process. Return through filter to buffer.
3. O₂ vent line from MOE headspace to an exterior safe vent (or O₂ bottle if you choose to capture).

### 3.6 Controls & Sensing
1. Install PLC, IO, SSRs/contactors; wire interlocks (door, over‑temp, vacuum OK).
2. Mount **pyrometers** (two‑color) with purged sight tubes toward melt and refining pot.
3. Mount **LIBS** windowed port over feeder/melt; align fiber to gated spectrometer.
4. Mount **OES** fiber to watch electrode/plasma zone.
5. Plumb **RGA** to refining pot foreline (through throttled tee after cold‑trap).

### 3.7 Power
1. Route mains (120 V) → **portable power station/UPS** → PDU → heaters/controls.
2. Separate clean supplies for controls; bond grounds; GFCI where appropriate.
3. Verify breaker sizing (20 A recommended), wire gauge, and earth bonding.

---

## 4) Commissioning & First Run

### 4.1 Dry Runs
- Leak‑check with argon; verify < 50 sccm leak at 50 mbar over ambient.
- Heat‑soak hot‑zone to 1000 °C; check element balance, pyrometers, thermal uniformity.
- Pump down refining pot; test cold‑trap condensation with water/ice first.

### 4.2 Feed Characterization
- Sieve feed ≤250 µm; bake at 150–200 °C to dry salts/moisture.
- **LIBS scan** (190–900 nm) over a representative sample to estimate oxide fractions (Fe‑oxides, SiO₂, Al₂O₃, CaO, TiO₂, alkalis). Save the spectrum for the run file.

### 4.3 MOE Operation (Fe→Si→Al)
1. **Melt/hold:** Bring hot‑zone to **1600–1650 °C** under light argon (50–150 mbar over ambient).
2. **Fe stage:** Apply low cathodic overpotential/current density; monitor **OES** for Fe lines. Once Fe pool accumulates in sump, **tap/skim** Fe or park it (mechanically isolated).
3. **Si stage:** Step potential upward; watch **Si emission** grow, and **OES** oxygen lines. Maintain controlled headspace; ensure Fe sump temperature slightly lower to limit mixing.
4. Manage bubbles; avoid vigorous stirring. If **LIBS/OES** signals co‑reduction (alloying), step back, let Fe settle, then proceed.

### 4.4 Transfer to Refining Pot
- Ladle/tap molten Si into covered transfer crucible; minimize air exposure.
- Move to refining pot; close, evacuate to **≤10 Pa**; heat to **1600–1850 °C** for 30–90 min.
- **RGA watch:** P‑species decay; **SiO (m/z ~44)** rise indicates over‑evaporation → increase trapping/cool baffles or adjust temperature.

### 4.5 Casting
- Pour into **Si₃N₄‑coated quartz** mold; directional cool (1–5 K/min) from bottom to top to segregate residual impurities to the hot end; crop tail.
- Optional: **mini float‑zone** pass on a small rod for semiconductor experiments.

---

## 5) Control Logic (simplified)
1. Preheat to 1600 °C → stable for 20 min.
2. LIBS feed OK? If not, abort.
3. MOE: set **Fe window** → Fe sump mass threshold → tap or isolate.
4. MOE: set **Si window** → Si rate threshold met → end Si stage.
5. Transfer → vacuum refine → RGA P below setpoint → cool.
6. Cast → cool → log batch & spectra.

---

## 6) Safety
- **Thermal:** >1700 °C potential. Use shields, IR PPE, lockouts. No combustible clutter.
- **Gas:** O₂ evolution; ensure venting away from personnel. **No HF used**; off‑gas is primarily O₂/Ar/SiO; cold‑trap captures condensables.
- **Electrical:** 120 V at high current; bonded grounds; GFCI; E‑stop. UPS/inverter must be rated for continuous draw.
- **Optical:** Bright hot surfaces; **avoid direct viewing**; use proper IR/UV eye protection when inspecting.
- **Mechanical:** Interlocks on doors/panels; guarded auger; hot‑work signage.

---

## 7) Maintenance
- Inspect liners & electrodes every ~10 hours at temp; replace worn anodes.
- Bake argon dryer, change filters quarterly.
- Clean cold‑traps each run; reclaim condensed SiO where feasible.
- Calibrate pyrometers quarterly; verify LIBS/OES wavelength daily warm‑up.

---

## 8) Upgrade Path
- Inert anode (ceramic‑metal) to fully eliminate carbon contact.
- Larger MOE pot w/ dual‑zone heaters for higher throughput.
- Better spectrometers for trace **B/P** detection (deep‑UV arms).
- Automated tapping, robotic ladle, and closed‑loop recipe tuning from spectra.

---

## 9) Appendices

### A) Target Setpoints (starting)
- MOE hot‑zone: **1625 °C**
- Fe stage: low overpotential; current density ~0.2–0.4 A cm⁻² (tune by OES)
- Si stage: step +10–20% vs Fe stage; watch OES (Si) & headspace
- Vacuum refine: **1700–1800 °C**, **≤10 Pa**, **30–90 min**

### B) Minimal Tools
IR thermometer, torque drivers, crimp kit, TIG‑level gloves, face shield, tongs, scale, sieve set.

### C) Expected Consumables (per 10 runs)
- Argon: ≤1 m³ (with reclaim)
- Liners: 1 ZrO₂ primary + 1 Al₂O₃ backup
- Anode face: 1 (if consumable)

---

**v0.1 total (with used/auction gear):** **\$8.8–9.8k**  
**This document:** CC‑BY for your build/use. Please operate safely and within local regulations.
