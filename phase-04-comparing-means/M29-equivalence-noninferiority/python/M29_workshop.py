from pathlib import Path

import numpy as np
from scipy.stats import norm, t

data = Path(__file__).resolve().parents[1] / "data"

def groups(file):
    group, value = np.loadtxt(data / file, delimiter=",", skiprows=1, usecols=(1,2), unpack=True)
    return value[group == 1], value[group == 0]

def tost(d, se, lower, upper, distribution, alpha=.05):
    p_lower = distribution.sf((d-lower)/se)
    p_upper = distribution.cdf((d-upper)/se)
    half = distribution.ppf(1-alpha)*se
    return dict(estimate=d, se=se, p_lower=p_lower, p_upper=p_upper,
                p_tost=max(p_lower,p_upper), lo=d-half, hi=d+half)

print("L1: CI inside margins:", -1.1 > -2 and 1.3 < 2)
new, reference = groups("means.csv")
n1, n0 = len(new), len(reference)
df = n1+n0-2
pooled = ((n1-1)*new.var(ddof=1)+(n0-1)*reference.var(ddof=1))/df
se = np.sqrt(pooled*(1/n1+1/n0))
print("L2: means:", tost(new.mean()-reference.mean(), se, -2, 2, t(df)))
new, reference = groups("proportions.csv")
p1, p0 = new.mean(), reference.mean()
se = np.sqrt(p1*(1-p1)/len(new)+p0*(1-p0)/len(reference))
print("L3: proportions, unpooled Wald approximation:", tost(p1-p0, se, -.12, .12, norm))
