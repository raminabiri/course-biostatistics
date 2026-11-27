from csv import DictReader
from math import isclose
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "data/M49_calibration.csv"
with path.open() as f:
    rows = list(DictReader(f))
total = 0.0
for row in rows:
    n, probability, observed = (float(row[k]) for k in ("n", "mean_prediction", "observed"))
    expected = n * probability
    component = (observed - expected)**2 / (expected * (1 - probability))
    if row["bin"] == "1":
        assert isclose(component, 50 / 51)
    total += component
    print(row["bin"], expected, observed / n, component)
print("Sum:", total)
