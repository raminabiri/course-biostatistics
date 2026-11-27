import csv
from itertools import combinations
from pathlib import Path
from scipy import stats

with (Path(__file__).resolve().parents[1]/"data/practice.csv").open() as source:
    rows=list(csv.DictReader(source))
x=[int(row["after"])-int(row["before"]) for row in rows if row["design"]=="paired"]
k,n=sum(v>0 for v in x),sum(v!=0 for v in x)
print("L1:",stats.binomtest(k,n,alternative="less").pvalue,stats.binomtest(k,n).pvalue)
w=stats.wilcoxon(x,method="exact")
print("L2:",w.statistic,w.pvalue)
seq=[int(row["before"]) for row in rows if row["design"]=="runs"]
def count(x):
    return 1+sum(a!=b for a,b in zip(x,x[1:]))
reference=[]
for places in combinations(range(len(seq)),sum(seq)):
    ones=set(places)
    reference.append(count([i in ones for i in range(len(seq))]))
observed=count(seq)
tail=min(sum(x<=observed for x in reference),sum(x>=observed for x in reference))/len(reference)
print("L3:",observed,min(1,2*tail))
