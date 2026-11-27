import csv
from math import comb, isclose
with open("data/M64_L2.csv", newline="") as stream:
    row = next(csv.DictReader(stream))
k, n = int(row["k"]), int(row["n"])
null = comb(n,k) * 0.5**n
alternative = 1/(n+1)
bf = alternative/null
assert isclose(bf, 128/165)
print(null, alternative, bf, bf/(1+bf))
