from collections import defaultdict
from csv import DictReader
from math import exp, isclose
from pathlib import Path

sets = defaultdict(list)
with (Path(__file__).resolve().parents[1] / "data/M50_sets.csv").open() as f:
    for row in DictReader(f):
        sets[row["set_id"]].append((int(row["case"]), int(row["exposed"])))
if not sets or any(len(group) < 2 or sum(case for case, _ in group) != 1
                   or any(case not in (0, 1) or exposure not in (0, 1)
                          for case, exposure in group)
                   for group in sets.values()):
    raise ValueError("Each set must have one case, at least one control, and binary exposure.")

def score(beta):
    result = 0.0
    for group in sets.values():
        weights = [exp(beta * exposure) for _, exposure in group]
        expected = sum(w * exposure for w, (_, exposure) in zip(weights, group)) / sum(weights)
        observed = sum(case * exposure for case, exposure in group)
        result += observed - expected
    return result

low, high = -30, 30
if not score(low) > 0 > score(high):
    raise ValueError("No interior root in the search interval; check separation and exposure variation.")
for _ in range(80):
    mid = (low + high) / 2
    if score(mid) > 0:
        low = mid
    else:
        high = mid
beta = (low + high) / 2
print(len(sets), beta, exp(beta))
assert isclose(exp(beta), 4.0)
