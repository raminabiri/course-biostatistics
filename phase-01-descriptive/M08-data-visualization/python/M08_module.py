import csv
from pathlib import Path
from statistics import mean

path = Path(__file__).resolve().parents[1] / "data" / "M08_followup.csv"
with path.open(newline="") as stream:
    rows=list(csv.DictReader(stream))
starts=[int(row["day0"]) for row in rows]
counts=[sum(lo<=x<hi for x in starts) for lo,hi in ((110,130),(130,150),(150,170))]
change=[int(row["day14"])-int(row["day0"]) for row in rows if row["day14"]]
assert counts==[9,6,1] and len(change)==15 and sum(change)==-88
print(counts,len(change),mean(change))
