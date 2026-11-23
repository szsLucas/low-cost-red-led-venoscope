# KiCad CAD sources versus manuscript — preliminary review

**Purpose:** Keep source files transparent without claiming they describe the final assembled device. This is a **textual inspection** of the provided KiCad 10 files, not an electrical-rule check (ERC), design-rule check (DRC), or physical verification.

| Feature | Supplied KiCad files | Manuscript |
|---|---|---|
| LED quantity | `D1`…`D12` (12 LED instances) | 12 red LEDs |
| LED physical footprint | `LED_THT:LED_D3.0mm_Clear` on PCB | Typical 5 mm LED **assumed for calculations**; physical model not recorded |
| Series/current-limiting resistors | One symbol/footprint `R1`; numeric value not populated (`R`) | **Recommended** topology has one 220 Ω resistor **per LED** (12 branches). As-built wiring still needs confirmation |
| Battery | Schematic marks `BT1` as **6V**, but PCB footprint is `Battery:BatteryHolder_Keystone_2479_3xAAA` | Four 1.5 V batteries = nominal 6 V |
| Potentiometer | `RV1`, symbol field `R_Potentiometer_US` rather than a numeric value | 1 kΩ common rheostat; paper recommends ≥0.5 W rating |
| Switch | `SW1` symbol `SW_DPST_x2`, PCB footprint `SW_CK_JS202011AQN_DPDT_Angled` | On/off switch; exact part not reported |
| PCB layout | Two enabled copper layers, with routed segments and a rectangular outline plus inner circular cutout | Manually etched copper board; exact layer count, source CAD and manufacturing drawings not specified |

**Key caution:** A single current-limiting resistor shared by parallel LEDs is **not equivalent** to one resistor per LED. If the physical circuit is built with a shared resistor, currents can split unequally among the LEDs. The nominal 17.27 mA-per-LED model from the paper must **not** be applied directly to this PCB until the true values and wiring have been verified.

## Before marking the project 'validated'

1. Check whether these KiCad files match the actual board (trace routing, photographed front/back, continuity test).
2. Identify the real `R1` value, `RV1` value and potentiometer power rating; measure the supply voltage and branch/total currents.
3. Verify the battery holder: 3×AAA in the PCB footprint is not the article's four-cell source. Document the actual installed pack and any external wiring.
4. Confirm actual LED diameter, model, forward-voltage spread and wavelength (the paper's 630 nm is an assumption).
5. Review `SW1` pinout/footprint mapping and make sure the chosen switch implements the intended single on/off action.
6. Check board cutouts, clearance and components near/outside the outline; confirm mating with the 3D-printed case.
7. Run schematic ERC and board DRC in KiCad, record findings, and only then generate fabrication Gerbers and drill outputs.
8. Keep **as-built original** and **improved revision** as separate CAD versions rather than overwriting the historical design.

These design files are an appropriate addition to a research portfolio **when clearly marked as unverified source CAD**. Neither the original prototype nor a derived revision is a certified clinical device.

## Accompanying CAD captures

Four contributor-provided screenshots show the two 3D orientations, the KiCad PCB editor layout, and the KiCad schematic editor. They are stored under [`../hardware/kicad/previews/`](../hardware/kicad/previews/) and embedded in both top-level READMEs. **They are visual documentation, not evidence that all traces are routed or that ERC/DRC checks passed.**
