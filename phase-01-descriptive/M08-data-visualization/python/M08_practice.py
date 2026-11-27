import csv
from pathlib import Path
from statistics import mean, stdev

import matplotlib.pyplot as plt

root = Path(__file__).resolve().parents[1]
with (root / "data/M08_followup.csv").open() as source:
    rows = list(csv.DictReader(source))
visits = ("day0", "day7", "day14")

# هر تمرین شکل خودش را در پوشهٔ ماژول ذخیره می‌کند.
fig, axes = plt.subplots(1, 3, figsize=(11, 4))
groups = [[r for r in rows if r["group"] == g] for g in "AB"]
pressure = [[int(r["day0"]) for r in group] for group in groups]
axes[0].hist(pressure[0] + pressure[1], bins=range(110, 171, 10))
axes[0].set(xlabel="Baseline BP (mmHg)", ylabel="Count")
axes[1].boxplot(pressure)
axes[2].violinplot(pressure)
for axis in axes[1:]:
    for i, values in enumerate(pressure, 1):
        axis.scatter([i] * len(values), values, color="black", s=10)
    axis.set_xticks([1, 2], ["A", "B"])
    axis.set_ylabel("Baseline BP (mmHg)")
fig.savefig(root / "M08_python_L1.png", dpi=120, bbox_inches="tight")

fig, axes = plt.subplots(1, 2, figsize=(8, 4))
for label, group, values in zip("AB", groups, pressure):
    axes[0].scatter([int(r["age"]) for r in group], values, label=label)
axes[0].set(xlabel="Age (years)", ylabel="Baseline BP (mmHg)")
axes[0].legend()
axes[1].bar(list("AB"), [mean(x) for x in pressure],
            yerr=[stdev(x) / len(x)**0.5 for x in pressure], capsize=5)
axes[1].set_ylabel("Mean baseline BP (mmHg), ± 1 SE")
fig.savefig(root / "M08_python_L2.png", dpi=120, bbox_inches="tight")

fig, axes = plt.subplots(1, 2, sharey=True, figsize=(8, 4))
for label, axis, group in zip("AB", axes, groups):
    for row in group:
        values = [float(row[v]) if row[v] else float("nan") for v in visits]
        axis.plot([0, 7, 14], values, marker="o", markersize=3)
    axis.set(title=f"Group {label}", xlabel="Day", ylabel="Systolic BP (mmHg)")
    axis.set_xticks([0, 7, 14])
    print(label, "valid counts:", [sum(bool(r[v]) for r in group) for v in visits])
    for name in ("age", "day0"):
        values = [int(r[name]) for r in group]
        print(name, f"mean={mean(values):.2f}, SD={stdev(values):.2f}")
fig.savefig(root / "M08_python_L3.png", dpi=120, bbox_inches="tight")
plt.close("all")
