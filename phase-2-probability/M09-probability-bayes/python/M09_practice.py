"""Build the M09 probability tables from one row per individual."""
import csv
from collections import Counter
from math import isclose
from pathlib import Path

source = Path(__file__).resolve().parents[1] / "data" / "M09_individuals.csv"
with source.open(encoding="utf-8", newline="") as stream:
    rows = list(csv.DictReader(stream))

assert len(rows) == 11000
assert len({row["id"] for row in rows}) == len(rows)


def make_table(population):
    """Count each (reference, test) pair in one population."""
    return Counter(
        (row["reference"], row["test"])
        for row in rows
        if row["population"] == population
    )


base = make_table("baseline")
tp = base["positive", "positive"]
fn = base["positive", "negative"]
fp = base["negative", "positive"]
tn = base["negative", "negative"]
total = sum(base.values())
assert (tp, fn, fp, tn) == (90, 10, 90, 810)
print("L1: table", dict(base), "P(D or T) =", (tp + fn + fp) / total)

sensitivity = tp / (tp + fn)
specificity = tn / (tn + fp)
print("L2: P(T|D) =", sensitivity, "P(D|T) =", tp / (tp + fp))

for name in ("baseline", "low"):
    counts = make_table(name)
    actual_positive = counts["positive", "positive"]
    false_positive = counts["negative", "positive"]
    prevalence = (actual_positive + counts["positive", "negative"]) / sum(counts.values())
    observed_ppv = actual_positive / (actual_positive + false_positive)
    true_share = prevalence * sensitivity
    false_share = (1 - prevalence) * (1 - specificity)
    bayes_ppv = true_share / (true_share + false_share)
    assert isclose(observed_ppv, bayes_ppv)
    print(f"L3: {name}, n={sum(counts.values())}, prevalence={prevalence:.0%}, "
          f"PPV={observed_ppv:.4%}")
