# Proposed evaluation protocol (NOT performed)

This document is a suggested **future** protocol. It does not describe completed experiments or provide clinical guidance.

## 1. Electrical characterization

- Identify battery model; record open-circuit and loaded voltage at several potentiometer positions.
- Measure total supply current and, where feasible, per-branch currents; compare with the 6 V / 2.2 V / 220 Ω theory.
- Verify the installed resistance values, topology, potentiometer terminal wiring and power rating.
- Record potentiometer and LED package temperatures over a specified, controlled operating interval.
- Record supply current over battery discharge to estimate autonomy empirically.

## 2. Optical characterization

- Record exact LED part number and datasheet; if possible, measure emission spectrum with appropriate equipment.
- Measure irradiance using a calibrated sensor at defined distances and maximum-output settings.
- Characterize ambient light and illumination uniformity across the observation region.
- Review applicable optical radiation and electrical safety requirements before future human testing.

## 3. Controlled imaging

- Prefer a tissue-mimicking optical phantom with channels of known depth and optical properties for initial evaluation.
- Fix the camera, exposure, gain, white balance, distance, angle and room lighting.
- Capture baseline / device-on / device-off images for each configuration.
- Record raw or minimally processed frames and metadata, without selecting only favorable examples.
- Quantify a consistent region-of-interest metric such as `C = (I_background - I_vein) / I_background` and report variability and uncertainty.
- Repeat at multiple depths / LED settings; distinguish theoretical estimates from measured optical data.

## 4. Human-subject research

- Do not start systematic participant experiments without the required ethics review, informed consent and safety assessment.
- Remove identifying metadata or use only explicitly authorized images.
- Do not evaluate cannulation success or make clinical claims without a suitable reviewed study design and qualified collaborators.
