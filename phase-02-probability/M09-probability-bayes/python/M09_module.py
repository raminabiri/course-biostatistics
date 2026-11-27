from collections import Counter
import csv
from math import isclose
from pathlib import Path
path=Path(__file__).resolve().parents[1]/"data"/"M09_individuals.csv"
with path.open(newline="") as f:
    tally=Counter((r["population"],r["joint_code"]) for r in csv.DictReader(f))
base=[tally["baseline",str(i)] for i in range(1,5)]
low=[tally["low",str(i)] for i in range(1,5)]
a,b,c,d=base
result=(1-d/sum(base),a/(a+b),a/(a+c),low[0]/(low[0]+low[2]))
assert sum(base)+sum(low)==11000
assert all(isclose(got,expected) for got,expected in zip(result,(.19,.9,.5,1/12)))
print(base,low,result)
