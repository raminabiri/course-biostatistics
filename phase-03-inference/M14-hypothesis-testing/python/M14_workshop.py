from math import sqrt
from scipy.stats import t

mean, ref, sd, n = 54, 50, 10, 25
df = n-1
se = sd / sqrt(n)
stat = (mean-ref) / se
right = t.sf(stat, df)
two = 2 * t.sf(abs(stat), df)
h = t.ppf(.975, df) * se
lo, hi = mean-ref-h, mean-ref+h
assert abs(two-.05694)<.0001 and lo < 0 < hi
print("L1:", stat, df)
print("L2:", right, two)
print("L3:", lo, hi)
