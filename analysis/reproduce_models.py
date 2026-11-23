#!/usr/bin/env python3
"""Reproduce the paper's first-order optical and brightness model.

Does not represent experimental validation or a simulator for clinical use.
"""

import argparse
import csv
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from models import (
    R_BRANCH, RHEOSTAT_MAX, LED_COUNT, V_SOURCE, V_FORWARD,
    blood_mu_a, current_per_led, idealized_contrast, potentiometer_power,
    relative_brightness, skin_fraction, skin_mu_eff, vein_fraction_of_source,
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=Path('analysis/generated'))
    args = parser.parse_args()
    target = args.output_dir
    target.mkdir(parents=True, exist_ok=True)
    xs = list(range(0, int(RHEOSTAT_MAX) + 1))
    ys = [relative_brightness(x) for x in xs]

    with (target / 'brightness_theoretical.csv').open('w', newline='', encoding='utf-8') as handle:
        writer = csv.writer(handle)
        writer.writerow(['potentiometer_ohm', 'relative_brightness_percent', 'current_per_led_mA'])
        for x, y in zip(xs, ys):
            writer.writerow([x, f'{y:.6f}', f'{1000*current_per_led(x):.6f}'])

    fig, ax = plt.subplots(figsize=(8, 4.8))
    ax.plot(xs, ys, linewidth=2)
    ax.set(title='Theoretical brightness vs. common rheostat resistance',
           xlabel='Rheostat resistance (Ω)', ylabel='Relative brightness (%)',
           xlim=(0, RHEOSTAT_MAX), ylim=(0, 100))
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(target / 'brightness_theoretical.png', dpi=160)
    plt.close(fig)

    theoretical_max_pot = R_BRANCH / LED_COUNT
    values = {
        'model_type': 'theoretical; not measured',
        'source_voltage_V_nominal': V_SOURCE,
        'forward_voltage_V_assumed': V_FORWARD,
        'branch_resistance_ohm_recommended': R_BRANCH,
        'led_count': LED_COUNT,
        'led_current_at_0_ohm_mA': 1000.0 * current_per_led(0),
        'total_current_at_0_ohm_mA': 1000.0 * LED_COUNT * current_per_led(0),
        'resistor_power_at_0_ohm_mW': 1000.0 * current_per_led(0) ** 2 * R_BRANCH,
        'rheostat_peak_power_W_approx': potentiometer_power(theoretical_max_pot),
        'skin_mu_eff_per_mm': skin_mu_eff(),
        'blood_mu_a_per_mm': blood_mu_a(),
        'skin_fraction_of_source': skin_fraction(),
        'vein_fraction_of_source': vein_fraction_of_source(),
        'idealized_vein_contrast': idealized_contrast(),
    }
    (target / 'optical_and_electrical_theory.json').write_text(
        json.dumps(values, indent=2), encoding='utf-8')
    print(json.dumps(values, indent=2))
    print(f'Files saved under: {target.resolve()}')


if __name__ == '__main__':
    main()
