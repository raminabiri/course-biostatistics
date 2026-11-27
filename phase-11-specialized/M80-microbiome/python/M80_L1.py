import csv
from math import log
from statistics import mean
with open("data/M80_L1.csv") as f:
    rows=[[int(r[k]) for k in ("t1","t2","t3")] for r in csv.DictReader(f)]
for row in rows:
    p=[x/sum(row) for x in row]
    logs=list(map(log,row))
    print(-sum(v*log(v) for v in p),[v-mean(logs) for v in logs])
a,b=rows
distance=sum(abs(x-y) for x,y in zip(a,b))/(sum(a)+sum(b))
assert distance==.25
print(distance)
