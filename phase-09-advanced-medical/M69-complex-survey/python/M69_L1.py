import csv
from collections import defaultdict
from math import sqrt
with open("data/M69_L1.csv", newline="") as stream:
    rows = [(r["stratum"],r["psu"],int(r["weight"]),int(r["y"])) for r in csv.DictReader(stream)]
total = sum(w for _,_,w,_ in rows)
estimate = sum(w*y for _,_,w,y in rows)/total
cluster = defaultdict(float)
for stratum, psu, weight, y in rows:
    cluster[stratum,psu] += weight*(y-estimate)
variance = sum((cluster[s,"1"]-cluster[s,"2"])**2 for s in ("A","B"))/total**2
assert estimate==.375 and variance==10/256
def regional_rate(region):
    return sum(w*y for s,_,w,y in rows if s==region)/sum(w for s,_,w,_ in rows if s==region)
print(estimate,sqrt(variance),variance/.025,regional_rate("B")-regional_rate("A"))
