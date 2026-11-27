from csv import DictReader
from math import isclose
from pathlib import Path
with (Path(__file__).resolve().parents[1]/"data/M60_table.csv").open() as f:
    c={(int(r["reference"]),int(r["test"])):int(r["count"]) for r in DictReader(f)}
tp,fn,fp,tn = [c[key] for key in ((1,1),(1,0),(0,1),(0,0))]
se,sp = tp/(tp+fn),tn/(tn+fp)
out = se,sp,tp/(tp+fp),tn/(tn+fn),se/(1-sp),(1-se)/sp
print(out)
assert all(isclose(a,b) for a,b in zip(out,(.9,.8,.75,12/13,4.5,.125)))
