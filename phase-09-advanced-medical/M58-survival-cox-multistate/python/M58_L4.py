from csv import DictReader
from math import isclose
from pathlib import Path

with (Path(__file__).resolve().parents[1]/"data/M58_transitions.csv").open() as f:
    matrix = [[float(r[k]) for k in ("stable","followup","exit")] for r in DictReader(f)]
assert all(isclose(sum(row),1) for row in matrix)
v = [1,0,0]
for _ in range(2):
    v = [sum(a*b for a,b in zip(v,column)) for column in zip(*matrix)]
    print(v)
assert all(isclose(a,b) for a,b in zip(v,(.49,.26,.25)))
