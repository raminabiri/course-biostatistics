from csv import DictReader
from math import erfc, exp, log, sqrt
from pathlib import Path

with (Path(__file__).resolve().parents[1]/"data/M51_counts.csv").open() as file:
    counts = [tuple(int(row[k]) for k in ("no","partial","full")) for row in DictReader(file)]

beta, left, right = .7428791, -.4912285, 1.0693590
loglik = saturated = 0.0
for group, row in enumerate(counts):
    a, b = [1/(1+exp(-(cut-beta*group))) for cut in (left,right)]
    probabilities = a, b-a, 1-b
    loglik += sum(n*log(p) for n,p in zip(row,probabilities))
    saturated += sum(n*log(n/sum(row)) for n in row)
    print(probabilities)
lr = 2*(saturated-loglik)
print(beta, lr, erfc(sqrt(lr/2)))
assert abs(lr-.9174931)<1e-5
