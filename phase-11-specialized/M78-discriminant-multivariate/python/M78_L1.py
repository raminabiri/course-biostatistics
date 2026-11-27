import csv
from statistics import mean,correlation
with open("data/M78_L1.csv") as f:
    rows=list(csv.DictReader(f))
centers=[mean(int(r["score"]) for r in rows if r["group"]==g) for g in ["A","B"]]
boundary=mean(centers)
counts=(30,10,10,30)
inertia=sum((x-20)**2/20 for x in counts)/sum(counts)
assert boundary==4 and inertia==.25
print(boundary,abs(correlation([1,2,3],[2,4,6])),inertia)
