import csv
from math import isclose
from pathlib import Path
from statistics import mean

path = Path(__file__).resolve().parents[1] / "data" / "M01_module.csv"
with path.open(newline="") as stream:
    rows = list(csv.DictReader(stream))
by_patient = {}
for row in rows:
    dates = by_patient.setdefault(row["patient_id"], {})
    assert row["day"] not in dates
    dates[row["day"]] = float(row["temperature"]) if row["temperature"] else None

daily = {}
for day in ("0", "3"):
    scores = [dates[day] for dates in by_patient.values()]
    observed = [score for score in scores if score is not None]
    daily[day] = len(scores), len(observed), mean(observed)
changes = [dates["3"] - dates["0"] for dates in by_patient.values()
           if dates["3"] is not None and dates["0"] is not None]
assert len(rows) == 6 and len(by_patient) == 3
assert sum(row["day"] == "0" and row["ward"] == "internal" for row in rows) == 2
assert daily["0"][:2] == (3, 3) and daily["3"][:2] == (3, 2)
assert isclose(daily["0"][2], 37.3666666667)
assert isclose(daily["3"][2], 37.2) and isclose(mean(changes), -.25)
for day, (total, valid, average) in daily.items():
    print(f"Day {day}: rows={total}, valid={valid}, mean={average:.4f}")
print(f"Paired mean change: {mean(changes):.2f}")
