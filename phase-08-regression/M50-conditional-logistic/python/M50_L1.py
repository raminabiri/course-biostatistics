from csv import DictReader
from math import comb, log
from pathlib import Path

with (Path(__file__).resolve().parents[1] / "data/M50_pairs.csv").open() as f:
    pairs = {(int(r["case_exposed"]), int(r["control_exposed"])): int(r["pairs"])
             for r in DictReader(f)}
b, c = pairs[1, 0], pairs[0, 1]
n = b+c
p = min(1, 2*sum(comb(n, k) for k in range(min(b, c)+1))/2**n)
print(b/c, log(b/c), p)
assert b/c == 3 and n == 16
