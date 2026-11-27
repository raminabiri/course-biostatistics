from csv import DictReader
from math import isclose, log
from pathlib import Path
with (Path(__file__).resolve().parents[1]/"data/M51_counts.csv").open() as file:
    a,b = [{k:int(row[k]) for k in ("no","partial","full")} for row in DictReader(file)]
ratios = [(b[k]/b["no"])/(a[k]/a["no"]) for k in ("partial","full")]
print(ratios,[log(x) for x in ratios],[b[k]/sum(b.values()) for k in b])
assert all(isclose(x,y) for x,y in zip(ratios,(2.5,20/7)))
