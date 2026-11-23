"""Regenerate the synthetic M09 CSV files using Python's standard library."""
from csv import writer
from pathlib import Path
from random import Random


out = Path(__file__).resolve().parents[1] / "data"
rng = Random(909)
cells = [(1, "positive", "positive"), (2, "positive", "negative"),
         (3, "negative", "positive"), (4, "negative", "negative")]
populations = {"baseline": (90, 10, 90, 810), "low": (90, 10, 990, 8910)}
codes = {}
with (out / "M09_individuals.csv").open("w", newline="", encoding="utf-8") as stream:
    table = writer(stream, lineterminator="\n")
    table.writerow(["id", "population", "reference", "test", "joint_code"])
    serial = 1
    for name, counts in populations.items():
        group = [cell for cell, count in zip(cells, counts) for _ in range(count)]
        rng.shuffle(group)
        codes[name] = [row[0] for row in group]
        for code, reference, test in group:
            table.writerow([serial, name, reference, test, code])
            serial += 1

for name, values in codes.items():
    with (out / f"M09_prism_{name}.csv").open("w", newline="", encoding="utf-8") as stream:
        table = writer(stream, lineterminator="\n")
        table.writerow([name])
        table.writerows((v,) for v in values)
