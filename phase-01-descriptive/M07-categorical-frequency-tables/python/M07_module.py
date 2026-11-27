import csv
from pathlib import Path
path = Path(__file__).resolve().parents[1] / "data" / "M07_module.csv"
with path.open(newline="") as f:
    tab={(r["center"],r["status"]):int(r["count"]) for r in csv.DictReader(f)}
def at(center,status):
    return tab[center,status]
rates={c:at(c,"positive")/(at(c,"positive")+at(c,"negative")) for c in ("A","B")}
bounds=(12/50,(12+10)/50)
assert rates=={"A":.3,"B":.4} and bounds==(.24,.44)
print(rates,sum(at(c,"positive") for c in rates)/60,12/20,bounds)
