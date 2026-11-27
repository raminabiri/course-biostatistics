import csv
from math import isclose
with open("data/M82_L1.csv") as f:
    rates={r["arm"]:int(r["improved"])/int(r["n"]) for r in csv.DictReader(f)}
difference=rates["program"]-rates["control"]
assert isclose(difference,1/3)
print(rates,difference)
