"""First-order analytical models reported in the supplied venoscope paper.

All values are *illustrative theoretical assumptions*; none are measured here.
"""

from math import exp, sqrt

LED_COUNT = 12
V_SOURCE = 6.0  # nominal battery voltage, V
V_FORWARD = 2.2  # assumed LED forward voltage, V
R_BRANCH = 220.0  # recommended per-LED resistor, ohm
RHEOSTAT_MAX = 1000.0  # ohm

SKIN_MU_A = 0.066  # 1/mm
SKIN_MU_S = 11.05  # 1/mm
G = 0.8
SKIN_DEPTH = 1.5  # mm equivalent path
BLOOD_DEPTH = 1.5  # mm equivalent path

# From the paper at approximately 630 nm, cm^-1/M
EPS_HBO2 = 610.0
EPS_HB = 5148.8
VENOUS_OXYGEN_SATURATION = 0.70  # illustrative
HB_G_PER_L = 150.0
HB_MOLAR_MASS = 64500.0  # g/mol


def current_per_led(potentiometer_ohms=0.0):
    """Approximate LED current [A] for 12 nominally identical branches."""
    if not 0 <= potentiometer_ohms <= RHEOSTAT_MAX:
        raise ValueError('Potentiometer resistance must lie between 0 and 1000 ohms')
    return (V_SOURCE - V_FORWARD) / (R_BRANCH + LED_COUNT * potentiometer_ohms)


def relative_brightness(potentiometer_ohms):
    """Percentage relative to current at zero potentiometer resistance."""
    return 100.0 * current_per_led(potentiometer_ohms) / current_per_led(0.0)


def potentiometer_power(potentiometer_ohms):
    """Power dissipated in common rheostat [W]."""
    return (LED_COUNT * current_per_led(potentiometer_ohms)) ** 2 * potentiometer_ohms


def skin_mu_eff(mu_a=SKIN_MU_A, mu_s=SKIN_MU_S, anisotropy=G):
    """Effective attenuation coefficient [1/mm]."""
    if mu_a < 0 or mu_s < 0 or not 0 <= anisotropy <= 1:
        raise ValueError('Invalid optical coefficients or anisotropy')
    mu_s_reduced = mu_s * (1.0 - anisotropy)
    return sqrt(3.0 * mu_a * (mu_a + mu_s_reduced))


def skin_fraction(depth_mm=SKIN_DEPTH):
    if depth_mm < 0:
        raise ValueError('Optical path must be nonnegative')
    return exp(-skin_mu_eff() * depth_mm)


def blood_mu_a():
    """Illustrative venous absorption [1/mm], converting from cm^-1."""
    eps_mix = (VENOUS_OXYGEN_SATURATION * EPS_HBO2
               + (1.0 - VENOUS_OXYGEN_SATURATION) * EPS_HB)
    mu_cm = 2.303 * eps_mix * HB_G_PER_L / HB_MOLAR_MASS
    return mu_cm / 10.0


def vein_fraction_of_skin(depth_mm=BLOOD_DEPTH):
    if depth_mm < 0:
        raise ValueError('Optical path must be nonnegative')
    return exp(-(blood_mu_a() - SKIN_MU_A) * depth_mm)


def vein_fraction_of_source():
    return skin_fraction() * vein_fraction_of_skin()


def idealized_contrast():
    return 1.0 - vein_fraction_of_skin()
