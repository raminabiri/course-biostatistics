"""Read the M17 data and reproduce all three examples."""
import csv
from math import isfinite, sqrt
from pathlib import Path
from statistics import mean, stdev

from scipy import stats


data_path = Path(__file__).resolve().parents[1] / "data" / "values.csv"
with data_path.open(encoding="utf-8", newline="") as source:
    x = [float(row["value"]) for row in csv.DictReader(source)]
if len(x) != 8 or not all(isfinite(value) for value in x):
    raise ValueError("The supplied workbook example uses eight finite times.")

target = 50
sigma = 8
n = len(x)
average = mean(x)
sd = stdev(x)
se = sd / sqrt(n)
fit = stats.ttest_1samp(x, popmean=target)

# L1: the default alternative is two-sided.
print(f"L1: N={n}, mean={average:.6f}, SD={sd:.6f}, SE={se:.6f}")
print(f"t={fit.statistic:.6f}, df={fit.df:g}, p_two={fit.pvalue:.6f}")

# L2: use the known population SD from the exercise.
z = (average - target) / (sigma / sqrt(n))
print(f"L2: z={z:.6f}, p_right={stats.norm.sf(z):.6f}, "
      f"p_two={2 * stats.norm.sf(abs(z)):.6f}")

# L3: a tail area is separate from an interval's center.
mean_ci = fit.confidence_interval()
print(f"L3: p_right={stats.t.sf(fit.statistic, fit.df):.6f}, "
      f"p_left={stats.t.cdf(fit.statistic, fit.df):.6f}")
print(f"mean_ci=[{mean_ci.low:.6f}, {mean_ci.high:.6f}]")
print(f"difference_ci=[{mean_ci.low - target:.6f}, {mean_ci.high - target:.6f}]")
