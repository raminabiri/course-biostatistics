import csv
from pathlib import Path
from statistics import mean

path = Path(__file__).resolve().parents[1] / "data" / "M62_missing.csv"
with path.open(newline="") as stream:
    rows = list(csv.DictReader(stream))
group_mean = {
    group: mean(float(row["y"]) for row in rows if row["group"] == group and row["y"])
    for group in ("A", "B")
}
scenarios = (0, -3, -6, -4.5)
results = []
for delta in scenarios:
    scores = []
    for row in rows:
        if row["y"]:
            scores.append(float(row["y"]))
        else:
            shift = delta if row["group"] == "B" else 0
            scores.append(group_mean[row["group"]] + shift)
    results.append(mean(scores))
    print(delta, results[-1])
assert results == [17, 16, 15, 15.5]
