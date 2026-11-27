import csv
from math import ceil,isclose,sqrt
from statistics import NormalDist
with open("data/P05.csv") as stream:
    rows=list(csv.DictReader(stream))
def summary(group):
    values=[r["outcome"] for r in rows if r["arm"]==group]
    return len(values),values.count("1"),values.count("")
n1,k1,m1=summary("program")
n0,k0,m0=summary("control")
observed=k1/(n1-m1)-k0/(n0-m0)
lower=k1/n1-(k0+m0)/n0
upper=(k1+m1)/n1-k0/n0
normal=NormalDist()
n=ceil((normal.inv_cdf(.975)*sqrt(2*.525*.475)+normal.inv_cdf(.80)*sqrt(.45*.55+.60*.40))**2/.15**2)
assert isclose(lower,.08) and isclose(upper,.20) and n==173
print(observed,lower,upper,n)
