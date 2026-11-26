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
