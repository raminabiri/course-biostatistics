import csv
from itertools import combinations
from pathlib import Path
from statistics import mean

path = Path(__file__).resolve().parents[1] / "data" / "M63_permutation.csv"
with path.open(newline="") as stream:
    rows = list(csv.DictReader(stream))
a = [int(row["score"]) for row in rows if row["group"] == "A"]
b = [int(row["score"]) for row in rows if row["group"] == "B"]
observed = mean(b) - mean(a)
values = a + b
diffs = [(sum(values) - 2 * sum(group)) / len(a)
         for group in combinations(values, len(a))]
p = mean(abs(difference) >= abs(observed) for difference in diffs)
assert observed == 4 and len(diffs) == 20 and p == 0.1
print(observed, len(diffs), p)
