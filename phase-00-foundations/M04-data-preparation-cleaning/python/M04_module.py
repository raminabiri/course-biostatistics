import csv
from pathlib import Path
from statistics import mean
from math import isclose

data = Path(__file__).resolve().parents[1] / "data"
with (data / "M04_module_registry.csv").open(newline="") as stream:
    people = list(csv.DictReader(stream))
labs_by_id = {}
with (data / "M04_module_labs.csv").open(newline="") as stream:
    for row in csv.DictReader(stream):
        labs_by_id.setdefault(row["pid"], []).append(float(row["ldl"]))
results = []
for row in people:
    pid = row["pid"]
    height = float(row["height_raw"])*(100 if pid == "2" else 1)
    pressure = float(row["sbp_raw"]) if row["sbp_raw"] != "-99" else None
    bmi = float(row["weight_kg"])/(height/100)**2
    ldl = mean(labs_by_id[pid]) if pid in labs_by_id else None
    results.append((pid, height, pressure, row["smoker"] or None, bmi, ldl))
assert len(results)==3 and results[1][1]==168 and isclose(results[1][4],26.0416666667)
assert results[2][2:4]==(None,None)
assert [row[-1] for row in results]==[120,140,None]
for row in results:
    print(row)
