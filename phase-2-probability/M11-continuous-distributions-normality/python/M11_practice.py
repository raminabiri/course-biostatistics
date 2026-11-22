import csv
from math import exp, log
from pathlib import Path

import matplotlib.pyplot as plt
from scipy.stats import chi2, f, norm, probplot, t

print("L1: upper tail =", norm.sf(130, loc=100, scale=15))
print("L1: percentile 95 =", norm.ppf(.95, loc=100, scale=15))
print("L2: lognormal mean =", exp(log(10) + .5**2 / 2))
print("L2: exponential survival =", exp(-2))
print("L3: t percentile =", t.ppf(.975, 9))
print("L3: chi-square probability =", chi2.cdf(5, 3))
print("L3: F probability =", f.cdf(2, 3, 7))

root = Path(__file__).resolve().parents[1]
with (root / "data/M11_measurements.csv").open() as source:
    x = [float(row["value"]) for row in csv.DictReader(source)]
figure, axis = plt.subplots()
probplot(x, dist="norm", plot=axis)
figure.savefig(root / "M11_python_qq.png", dpi=120, bbox_inches="tight")
plt.close(figure)
