"""Regression tests for values reported in the paper (theoretical only)."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'analysis'))
from models import (
    blood_mu_a, current_per_led, idealized_contrast, potentiometer_power,
    relative_brightness, skin_fraction, skin_mu_eff, vein_fraction_of_source,
)


class ModelTests(unittest.TestCase):
    def test_nominal_led_current(self):
        self.assertAlmostEqual(current_per_led(0) * 1000, 17.2727, places=3)

    def test_non_linear_brightness(self):
        self.assertAlmostEqual(relative_brightness(100), 15.49, delta=0.05)
        self.assertAlmostEqual(relative_brightness(500), 3.54, delta=0.05)
        self.assertAlmostEqual(relative_brightness(1000), 1.80, delta=0.05)

    def test_peak_pot_power(self):
        self.assertAlmostEqual(potentiometer_power(220.0 / 12), 0.1969, delta=0.001)

    def test_optical_values(self):
        self.assertAlmostEqual(skin_mu_eff(), 0.671, delta=0.002)
        self.assertAlmostEqual(blood_mu_a(), 1.056, delta=0.002)
        self.assertAlmostEqual(skin_fraction(), 0.365, delta=0.003)
        self.assertAlmostEqual(vein_fraction_of_source(), 0.083, delta=0.003)
        self.assertAlmostEqual(idealized_contrast(), 0.773, delta=0.003)

    def test_reject_invalid_input(self):
        with self.assertRaises(ValueError):
            current_per_led(-1)
        with self.assertRaises(ValueError):
            current_per_led(1001)


if __name__ == '__main__':
    unittest.main()
