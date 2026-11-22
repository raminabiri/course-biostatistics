from scipy import stats
a = [47,50,51,53,55,56,59,61]
b = [45,46,48,49,50,52,54,57]
w = stats.ttest_ind(a,b,equal_var=False)
s = stats.ttest_ind(a,b,equal_var=True)
print("L1:", w.statistic, w.df)
print("L2:", s.statistic, s.pvalue)
print("L3:", stats.ttest_ind(a,b,equal_var=False,alternative="greater").pvalue, w.confidence_interval())
