import csv
from statistics import mean
from math import isclose
with open("data/M71_L1.csv", newline="") as stream:
    rows = list(csv.DictReader(stream))
sir = [int(r["observed"])/int(r["expected"]) for r in rows]
smooth = [(int(r["observed"])+5)/(int(r["expected"])+5) for r in rows]
z = [value-mean(sir) for value in sir]
edges = [(i,j) for i,r in enumerate(rows) for j,s in enumerate(rows)
         if abs(int(r["x"])-int(s["x"]))==1]
moran = (len(rows)/len(edges))*sum(z[i]*z[j] for i,j in edges)/sum(x*x for x in z)
assert isclose(moran,.4) and isclose(smooth[-1],5/3)
print(sir,smooth,moran)
