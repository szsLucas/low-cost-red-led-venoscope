# Reproducibility checklist

Status is based on the supplied six-page manuscript, later supplied editable KiCad sources, and four KiCad screenshots. **No physical inspection, ERC/DRC, or electrical measurement has been performed.**

| Deliverable | Status | Why it matters / next action |
|---|---|---|
| Academic manuscript (PDF) | **Available** | Included under `article/` |
| Prototype and forearm images from manuscript | **Available** | Retain attribution and publication permissions |
| KiCad 3D renders, PCB layout and schematic screenshots | **Available** | Four supplied CAD previews included under `hardware/kicad/previews/` |
| LED count, nominal supply, controls | **Described** | Validate installed parts and electrical supply range |
| Precise LED datasheet / measured wavelength | **Missing** | Identify part; 630 nm is an assumed nominal value |
| 220 Ω limit resistor per LED | **Proposed in paper** | Confirm real resistors and connection topology with multimeter |
| Editable schematic (KiCad) | **Supplied, unverified** | Check against fabricated PCB and correct all discrepancies |
| Verified as-built electrical schematic | **Missing** | Trace actual PCB; confirm netlist and values with measurements |
| Measured current vs brightness setting | **Missing** | Record battery voltage, total current, per-branch currents |
| PCB CAD layout | **Supplied, unverified** | KiCad file and screenshots available; inspect routing and run DRC |
| Verified Gerbers / drills / mechanical dimensions | **Missing** | Generate only after schematic, layout and physical revision have been verified |
| 3D CAD / STL / assembly dimensions | **Missing** | Obtain Tinkercad/print exports and document tolerances |
| Quantified BOM and procurement sources | **Incomplete** | Identify vendor, exact models, unit costs and purchase date |
| Potentiometer electrical rating | **Not verified** | Article recommends ≥0.5 W; verify installed part and temperature |
| LED / enclosure thermal measurements | **Missing** | Assess safe contact and operation |
| Irradiance / spectra | **Missing** | Measure with suitable calibrated instruments |
| Power consumption and battery life | **Missing** | Report tested battery type, voltages, settings and runtime |
| Standardized imaging conditions | **Missing** | Control ambient light, distance, exposure, camera and settings |
| Tissue-mimicking optical phantom | **Not performed** | Future work to quantify known vein-depth contrast |
| Study protocol, consent / ethical approval | **Not performed** | Needed before systematic participant experiments |
| Real-world diagnostic/cannulation performance | **Not established** | Do not report as validated or assume clinical suitability |
| Publication and image redistribution permissions | **Verify before publication** | Agree with all authors and confirm image permissions |

## Recommended upload order

**P0 — establish factual hardware provenance:** original photographs, schematic trace, component model numbers, PCB top/bottom, and the 3D source.

**P1 — make it reproducible:** cleaned-up EDA files, component list, measurement data with units, assembly guide, schematic-to-PCB verification.

**P2 — characterize performance:** repeatable power, thermal and optical measurements, then objective image-based contrast with a phantom.

**P3 — new research iteration:** redesigned current drive and NIR architecture if appropriate. Keep version history so that future capabilities are not attributed to the current prototype.
