from collections import Counter
from csv import DictReader
from math import isclose, sqrt
from pathlib import Path

from scipy import stats

with (Path(__file__).resolve().parents[1] / "data/M34_practice.csv").open() as source:
    rows = list(DictReader(source))

n = len(rows)
k = sum(int(row["on_time"]) for row in rows)
counts = Counter(row["route"] for row in rows)
assert n == len({row["id"] for row in rows}) == 100
assert k == 60 and [counts[c] for c in "ABC"] == [65, 25, 10]

exact = stats.binomtest(k, n, .5)
z = (k/n-.5) / sqrt(.5*.5/n)
gof = stats.chisquare([counts[c] for c in "ABC"], f_exp=[50, 30, 20])
print("L1:", stats.binomtest(k, n, .5, alternative="greater").pvalue, exact.pvalue)
print("L2:", z, stats.norm.sf(z), 2*stats.norm.sf(abs(z)))
print("L3:", gof.statistic, 2, gof.pvalue)
assert isclose(exact.pvalue, .056887933641, abs_tol=1e-10)
assert isclose(gof.statistic, 31/3)

z_cc = max(0, abs(k - n*.5) - .5) / sqrt(n*.5*.5)
print("Corrected P:", 2*stats.norm.sf(z_cc))
print("95% exact interval:", exact.proportion_ci(.95, method="exact"))
print("95% Wilson interval:", exact.proportion_ci(.95, method="wilson"))

# Enumerate counts with the Pearson statistic defining the tail.
tables = [(a, b, n-a-b) for a in range(n+1) for b in range(n-a+1)]
expected = [50, 30, 20]
tail = [table for table in tables
        if sum((obs-exp)**2/exp for obs, exp in zip(table, expected)) >= gof.statistic-1e-10]
exact_gof = stats.multinomial.pmf(tail, n, [.5,.3,.2]).sum()
print("Exact multinomial Pearson tail:", exact_gof)
assert isclose(exact_gof, .00586547283532, abs_tol=1e-10)
