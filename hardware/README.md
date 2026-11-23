# Hardware source files — status

The paper reports a 12-red-LED device with a manually etched copper board, a 3D-printed enclosure, four 1.5 V cells, an on/off switch, and a 1 kΩ common rheostat.

The original contributors subsequently provided **editable KiCad schematic and PCB documents**, retained under [`kicad/`](kicad/). The CAD files are **not independently verified against the as-built prototype**. Their topology and mechanical component footprints differ from some values discussed in the manuscript: see [`../docs/kicad-vs-paper.md`](../docs/kicad-vs-paper.md).

The [`schematic/reference-circuit.svg`](schematic/reference-circuit.svg) is a **conceptual representation of the article's recommended design**, not an export of the KiCad schematic or a reconstruction of the physical board. It must not be presented as such.

Still needed: KiCad ERC/DRC review, measured component values and continuity mapping, board-layer exports and photographs, verified Gerbers/drills if appropriate, and 3D enclosure source files and dimensions. No files here represent validated clinical equipment.

The contributor also supplied four KiCad screenshots, now at [`kicad/previews/`](kicad/previews/). These help inspect layout and schematic directly from the GitHub README but do not validate the electrical or mechanical implementation.
