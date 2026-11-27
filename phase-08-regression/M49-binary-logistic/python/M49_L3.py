from csv import DictReader
from math import isclose
from pathlib import Path

with (Path(__file__).resolve().parents[1] / "data/M49_separation.csv").open() as f:
    rows = list(DictReader(f))
counts = [(int(row["completed"]), int(row["not_completed"])) for row in rows]
probabilities = [(a + .5) / (a + b + 1) for a, b in counts]
odds = [(a + .5) / (b + .5) for a, b in counts]
ratio = odds[1] / odds[0]
print(probabilities, ratio)
assert isclose(ratio, 441)
