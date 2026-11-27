from math import sqrt
from scipy.stats import binomtest, t

def interval(center, critical, se):
    return center - critical * se, center + critical * se

mean_ci = interval(50, t.ppf(.975, 24), 2)
data = binomtest(2, 20)
exact = data.proportion_ci(method="exact")
wilson = data.proportion_ci(method="wilson")
v1, v2 = 4, 3.2
df = (v1 + v2)**2 / (v1**2/24 + v2**2/19)
diff_ci = interval(4, t.ppf(.975, df), sqrt(v1 + v2))
assert abs(mean_ci[0] - 45.87) < .01
assert abs(exact.high - .317) < .001
assert abs(diff_ci[1] - 9.41) < .02
print("L1:", mean_ci)
print("L2:", exact, wilson)
print("L3:", diff_ci)
