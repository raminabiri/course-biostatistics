import csv
from math import sqrt
with open("data/M68_L1.csv", newline="") as stream:
    rows = list(csv.DictReader(stream))
effects = [float(row["effect"]) for row in rows]
variance = [float(row["se"])**2 for row in rows]
weights = [1/v for v in variance]
def weighted_mean(values, weights):
    return sum(x*w for x,w in zip(values,weights))/sum(weights)
pooled = weighted_mean(effects,weights)
q = sum(w*(x-pooled)**2 for x,w in zip(effects,weights))
df = len(rows)-1
c = sum(weights)-sum(w**2 for w in weights)/sum(weights)
tau2 = max(0,(q-df)/c)
random = [1/(v+tau2) for v in variance]
assert (pooled,q,tau2)==(3,14,6)
print(pooled,q,(q-df)/q,tau2,weighted_mean(effects,random),sqrt(1/sum(random)))
