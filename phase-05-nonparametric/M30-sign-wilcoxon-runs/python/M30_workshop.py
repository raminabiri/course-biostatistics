import csv
from math import comb
from pathlib import Path
from scipy import stats

data_dir=Path(__file__).resolve().parents[1]/"data"

def combinations(n, k):
    return comb(n, k) if 0 <= k <= n else 0

def runs_test(sequence):
    zero, one=sequence.count(0), sequence.count(1)
    if not zero or not one or zero+one != len(sequence):
        raise ValueError("Two observed classes coded 0 and 1 are required.")
    observed=1+sum(a!=b for a,b in zip(sequence,sequence[1:]))
    counts={}
    for r in range(2,len(sequence)+1):
        k=r//2
        a,b=combinations(zero-1,k-1),combinations(one-1,k-1)
        if r%2==0:
            counts[r]=2*a*b
        else:
            counts[r]=combinations(zero-1,k)*b+a*combinations(one-1,k)
    total=sum(counts.values())
    assert total==comb(len(sequence),one)
    lower=sum(value for r,value in counts.items() if r<=observed)
    upper=sum(value for r,value in counts.items() if r>=observed)
    return observed,min(1,2*min(lower,upper)/total)

def report(file, method):
    with (data_dir/file).open(newline="",encoding="utf-8") as source:
        rows=list(csv.DictReader(source))
    delta=[int(row["after"])-int(row["before"]) for row in rows if row["design"]=="paired"]
    nonzero=[d for d in delta if d!=0]
    positive=sum(d>0 for d in nonzero)
    print(file)
    print("L1: positive, negative, zero, left p, two-sided p:",
          positive,sum(d<0 for d in nonzero),sum(d==0 for d in delta),
          stats.binomtest(positive,len(nonzero),alternative="less").pvalue,
          stats.binomtest(positive,len(nonzero)).pvalue)
    ranks=stats.rankdata([abs(d) for d in nonzero])
    w_positive=sum(rank for d,rank in zip(nonzero,ranks) if d>0)
    fit=stats.wilcoxon(nonzero,zero_method="wilcox",correction=False,method=method)
    print("L2: W+, smaller rank sum, two-sided p, method:",
          w_positive,fit.statistic,fit.pvalue,method)
    ordered=sorted((row for row in rows if row["design"]=="runs"),key=lambda row:int(row["id"]))
    print("L3:",runs_test([int(row["before"]) for row in ordered]))

report("practice.csv","exact")
report("extended.csv","asymptotic")
