from math import sqrt
from scipy.stats import nct, t

d = (54 - 50) / 8
g = d * (1 - 3/(4*38 - 1))
rd, rr, odds_ratio = .30-.20, .30/.20, (30/70)/(20/80)

def power(n, effect):
    df = 2*n - 2
    critical = t.ppf(.975, df)
    noncentrality = effect * sqrt(n/2)
    return nct.sf(critical, df, noncentrality) + nct.cdf(-critical, df, noncentrality)

n = next(n for n in range(2, 300) if power(n, d) >= .8)
assert n == 64 and power(n-1, d) < .8
print("L1:", d, g)
print("L2:", rd, rr, odds_ratio)
print("L3:", n, "per group; power =", power(n, d))
