# Reproduce the manuscript's mathematical models

The manuscript describes a **simplified analytical model**, not a validated optical simulation or measured dataset. `models.py` implements its formulas and reported nominal constants for:

- one resistor and one LED in each of 12 parallel branches, with a common 1 kΩ rheostat;
- nominal LED current and relative brightness;
- effective skin attenuation and an illustrative venous absorption scenario;
- idealized contrast `(I_skin - I_vein)/I_skin`.

Run at the repository root:

```bash
python -m pip install -r requirements.txt
python analysis/reproduce_models.py --output-dir analysis/generated
python -m unittest discover -s tests -v
```

Outputs (locally generated, git-ignored):

- `analysis/generated/brightness_theoretical.png` — theoretical curve, like Fig. 3;
- `analysis/generated/brightness_theoretical.csv` — theoretical rheostat response;
- `analysis/generated/optical_and_electrical_theory.json` — model summary.

All files are **new reproducibility calculations**, not original experimental datasets. The article's existing graph is preserved in `assets/figures/brightness-theoretical-paper.png`.
