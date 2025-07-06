import numpy as np

def calculate_psi(expected, actual, buckets=10):
    breakpoints = np.linspace(0, 100, buckets + 1)
    quantiles = np.percentile(expected, breakpoints)
    quantiles[0], quantiles[-1] = -np.inf, np.inf

    expected_counts = np.histogram(expected, bins=quantiles)[0]
    actual_counts = np.histogram(actual, bins=quantiles)[0]

    expected_percents = expected_counts / len(expected)
    actual_percents = actual_counts / len(actual)

    psi = np.sum((expected_percents - actual_percents) * np.log((expected_percents + 1e-6) / (actual_percents + 1e-6)))
    return psi