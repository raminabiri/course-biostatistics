from csv import DictReader
from math import exp, isclose, log
from pathlib import Path

with (Path(__file__).resolve().parents[1] / "data/M49_counts.csv").open() as f:
    rows = {row["group"]: row for row in DictReader(f)}

odds = {group: int(row["completed"]) / int(row["not_completed"])
        for group, row in rows.items()}
intercept = log(odds["A"])
coefficient = log(odds["B"]) - intercept
probabilities = [1 / (1 + exp(-(intercept + coefficient * group)))
                 for group in (0, 1)]
print(intercept, coefficient, exp(coefficient), probabilities)
assert isclose(exp(coefficient), 2.25)
assert all(isclose(p, expected) for p, expected in zip(probabilities, (.4, .6)))
