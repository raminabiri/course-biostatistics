import csv
from collections import defaultdict
from math import isclose
events, years = defaultdict(int), defaultdict(int)
with open("data/P02.csv") as f:
    for r in csv.DictReader(f):
        g=r["exposure"]
        events[g]+=int(r["event"])
        years[g]+=int(r["time"])
rates={g:events[g]/years[g] for g in events}
assert years["1"]==30 and isclose(rates["1"]/rates["0"],20/9)
print({g:100*r for g,r in rates.items()},rates["1"]/rates["0"])
