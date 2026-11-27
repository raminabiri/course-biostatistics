from collections import defaultdict
from csv import DictReader
from math import isclose, log
from pathlib import Path

totals = defaultdict(lambda: [0, 0])
with (Path(__file__).resolve().parents[1] / "data/M52_rates.csv").open() as f:
    for row in DictReader(f):
        group = totals[row["group"]]
        group[0] += int(row["events"])
        group[1] += int(row["exposure"])
rates = {key: events/time for key, (events, time) in totals.items()}
ratio = rates["B"]/rates["A"]
print(rates, ratio, log(ratio))
assert isclose(ratio, 1.4)
