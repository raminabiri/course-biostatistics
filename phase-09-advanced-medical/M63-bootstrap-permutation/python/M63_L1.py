import csv
from itertools import product
from math import isclose, sqrt
from pathlib import Path
from statistics import mean, pstdev

path = Path(__file__).resolve().parents[1] / "data" / "M63_mini.csv"
with path.open(newline="") as stream:
    values = [int(row["waiting_minutes"]) for row in csv.DictReader(stream)]
averages = [mean(draw) for draw in product(values, repeat=len(values))]
assert len(averages) == 27 and mean(averages) == 4
assert isclose(pstdev(averages), sqrt(8 / 9))
print(len(averages), mean(averages), pstdev(averages))
