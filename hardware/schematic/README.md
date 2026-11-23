# Conceptual reference schematic

`reference-circuit.svg` is a **conceptual diagram of the circuit recommended in the article**: four 1.5 V cells, a switch, a common 1 kΩ rheostat, and 12 LED branches, each with its own 220 Ω resistor. It is **not a rendering of the supplied KiCad schematic** or the verified as-built board.

For editable originals, use [`../kicad/Venoscopio.kicad_sch`](../kicad/Venoscopio.kicad_sch) and the matching PCB file. See the [difference report](../../docs/kicad-vs-paper.md): the KiCad schematic includes only one resistor `R1`, while the paper explicitly recommends an individual limiting resistor per LED. Keep the supplied design and any proposed redesign under distinct versioned files. Before assembling or manufacturing, confirm wiring and component values and conduct electrical and optical safety review.
