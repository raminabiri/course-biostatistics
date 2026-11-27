from math import exp,log,isclose
from statistics import NormalDist
from scipy.stats import t
x=(NormalDist(100,10).cdf(110),exp(log(10)),exp(-.25*4),t.ppf(.975,9))
assert all(isclose(a,b) for a,b in zip(x,(.8413447461,10,.3678794412,2.2621571629)))
print(x)
