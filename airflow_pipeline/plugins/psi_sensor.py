def check_psi_threshold():
    import numpy as np
    from psi.psi_calculation import calculate_psi

    expected = np.load('/mlops/data/expected.npy')
    actual = np.load('/mlops/data/actual.npy')

    psi = calculate_psi(expected, actual)
    return psi > 0.25