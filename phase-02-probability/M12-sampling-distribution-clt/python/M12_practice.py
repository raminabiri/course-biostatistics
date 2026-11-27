from math import sqrt

import numpy as np

rng = np.random.default_rng(120)
sample = rng.exponential(scale=10, size=(5000, 5))
means = sample.mean(axis=1)  # هر سطر یک نمونه است.
print("L1: numbers of individuals and means:", sample.size, means.size)
print("L2: standard error:", 10 / sqrt(25))
for n in (1, 5, 30):
    means = rng.exponential(scale=10, size=(5000, n)).mean(axis=1)
    print(f"L3: n={n}, mean={means.mean():.2f}, simulated SE={means.std(ddof=1):.2f}, theoretical SE={10/sqrt(n):.2f}")
