from math import sqrt
from statistics import mean, stdev
from scipy import stats
before = [47,50,51,53,55,56,59,61]
after = [45,46,48,49,50,52,54,57]
d = [y-x for x,y in zip(before,after)]
fit = stats.ttest_rel(after,before)
print("L1:", mean(d), fit.statistic)
print("L2:", stdev(d), stdev(d)/sqrt(len(d)))
print("L3:", stats.ttest_rel(after,before,alternative="less").pvalue, fit.confidence_interval())
