from math import sqrt
from scipy import stats
x = [47,50,51,53,55,56,59,61]
fit = stats.ttest_1samp(x, popmean=50)
z = (sum(x)/len(x)-50)/(8/sqrt(len(x)))
ci = fit.confidence_interval()
print("L1:", fit.statistic, fit.pvalue)
print("L2:", z, stats.norm.sf(z))
print("L3:", ci.low-50, ci.high-50)
