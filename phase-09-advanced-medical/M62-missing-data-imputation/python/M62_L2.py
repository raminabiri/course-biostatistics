import csv
from pathlib import Path
from statistics import mean, variance
from math import isclose, sqrt

path = Path(__file__).resolve().parents[1] / "data" / "M62_pool.csv"
with path.open(newline="") as stream:
    rows = list(csv.DictReader(stream))
estimates = [float(row["estimate"]) for row in rows]
within = mean(float(row["within_variance"]) for row in rows)
between = variance(estimates)
extra = (1 + 1 / len(rows)) * between
total = within + extra
df = (len(rows) - 1) * (1 + within / extra) ** 2
assert isclose(total, 16 / 3) and isclose(df, 32)
print(mean(estimates), within, between, total, sqrt(total), df)
