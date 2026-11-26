import csv
from pathlib import Path
from statistics import median
from scipy import stats

with (Path(__file__).resolve().parents[1]/"data/practice.csv").open() as source:
    rows=list(csv.DictReader(source))
a,b=([float(row["value"]) for row in rows if row["group"]==label] for label in "AB")
w=stats.mannwhitneyu(a,b,method="exact")
k=stats.ks_2samp(a,b,method="exact")
table=stats.median_test(a,b,ties="below",correction=False)[3]
p=stats.fisher_exact(table).pvalue
print("L1:",w.statistic,w.pvalue)
print("L2:",k.statistic,k.pvalue)
print("L3:",median([x-y for x in a for y in b]),p)
