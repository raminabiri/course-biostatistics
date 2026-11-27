from csv import DictReader
from math import log
from pathlib import Path

with (Path(__file__).resolve().parents[1] / "data/M54_models.csv").open() as f:
    rows = list(DictReader(f))
scores = []
for row in rows:
    n, k, ll = (float(row[key]) for key in ("n", "k", "loglik"))
    scores.append((row["model"], -2*ll+2*k, -2*ll+k*log(n)))
print(scores)
assert min(scores,key=lambda row:row[1])[0]=="B"
assert min(scores,key=lambda row:row[2])[0]=="A"
