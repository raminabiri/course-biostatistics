import csv
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with (root / "data/M09_screening.csv").open() as source:
    counts = {(r["reference"], r["test"]): int(r["count"]) for r in csv.DictReader(source)}

tp = counts["positive", "positive"]
fn = counts["positive", "negative"]
fp = counts["negative", "positive"]
tn = counts["negative", "negative"]
print("L1: P(disease or positive) =", (tp + fn + fp) / sum(counts.values()))
sensitivity = tp / (tp + fn)
specificity = tn / (tn + fp)
print("L2: P(positive | disease) =", sensitivity)
print("L2: P(disease | positive) =", tp / (tp + fp))
for prevalence in (0.01, 0.10):
    true_positive = prevalence * sensitivity
    false_positive = (1 - prevalence) * (1 - specificity)
    print(f"L3: prevalence={prevalence:.0%}, PPV={true_positive / (true_positive + false_positive):.4%}")
