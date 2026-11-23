# PCB production documentation — pending verification

An **editable PCB layout** is available as [`../kicad/Venoscopio.kicad_pcb`](../kicad/Venoscopio.kicad_pcb). It is a supplied source file, not a verified, fabrication-ready board. A matching editable schematic is in the same directory.

Before publishing manufacturing outputs, compare the CAD with the as-built board, review the LED current-limiting topology, components and rated values, battery pack, board outline, mounting, polarity, clearances and mechanical overlap. Run ERC and DRC in KiCad; document remaining exceptions. The CAD shows a 3×AAA footprint and the article describes four cells in series. See [`../../docs/kicad-vs-paper.md`](../../docs/kicad-vs-paper.md).

Place verified Gerbers (`.gbr`), drill files (`.drl`), layer previews, assembly drawings and board photos here only after confirming revision and manufacturability. Do not invent fabrication data from the manuscript.
