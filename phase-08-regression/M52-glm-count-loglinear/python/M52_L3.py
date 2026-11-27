from collections import defaultdict
from csv import DictReader
from math import exp, log
from pathlib import Path
groups = defaultdict(dict)
with (Path(__file__).resolve().parents[1] / "data/M52_table.csv").open() as f:
    for row in DictReader(f):
        groups[row["stratum"]][row["a"],row["b"]] = int(row["count"])
g = 0
for table in groups.values():
    for (a,b), observed in table.items():
        expected = (sum(n for (i,j),n in table.items() if i==a)
                    * sum(n for (i,j),n in table.items() if j==b)
                    / sum(table.values()))
        if observed:
            g += 2*observed*log(observed/expected)
print(g,2,exp(-g/2))
assert abs(g-4.02710271)<1e-6
