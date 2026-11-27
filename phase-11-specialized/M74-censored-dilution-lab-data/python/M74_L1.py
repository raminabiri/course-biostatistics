import csv
from math import prod
from statistics import mean
with open("data/M74_L1.csv", newline="") as stream:
    rows = [(r["kind"],float(r["lower"]),float(r["upper"])) for r in csv.DictReader(stream)]
lower = mean(lo for _,lo,_ in rows)
upper = mean(hi for _,_,hi in rows)
above = mean(lo>4 or (lo==4 and kind=="interval") for kind,lo,_ in rows)
possible = mean(hi>4 for _,_,hi in rows)
gm_upper = prod(hi for _,_,hi in rows)**(1/len(rows))
assert (lower,upper,above,possible)==(3.5,5.5,.5,.5)
print(lower,upper,gm_upper,above)
