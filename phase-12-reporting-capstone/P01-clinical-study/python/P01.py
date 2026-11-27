import csv
from collections import Counter
from math import isclose
with open("data/P01.csv") as f:
    c=Counter((r["mobility_issue"],r["delayed"]) for r in csv.DictReader(f))
a,b=c["1","1"],c["1","0"]
d,e=c["0","1"],c["0","0"]
r0,r1=d/(d+e),a/(a+b)
assert (a,b,d,e)==(9,11,3,17) and isclose(r1-r0,.3)
print(r1-r0,r1/r0,a*e/(b*d))
