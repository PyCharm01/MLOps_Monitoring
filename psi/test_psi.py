import numpy as np
from psi_calculation import calculate_psi

expected = np.random.normal(0, 1, 1000)
actual = np.random.normal(0.5, 1.2, 1000)

print("PSI Score:", calculate_psi(expected, actual))