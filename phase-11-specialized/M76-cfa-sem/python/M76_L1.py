import csv
from math import isclose
with open("data/M76_L1.csv") as f:
    rows=list(csv.DictReader(f))
pred=[float(r["loading_i"])*float(r["loading_j"]) for r in rows]
res=[float(r["observed"])-p for r,p in zip(rows,pred)]
assert all(isclose(a,e,abs_tol=1e-10) for a,e in zip(res,[.04,0,-.02]))
print(pred,res)
