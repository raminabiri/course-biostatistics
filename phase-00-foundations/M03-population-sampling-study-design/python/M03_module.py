import csv
from pathlib import Path
from statistics import mean

data = Path(__file__).resolve().parents[1] / "data"

def read_rows(name):
    with (data / name).open(newline="") as stream:
        return list(csv.DictReader(stream))

def sort_key(row):
    return float(row["u"]), int(row["id"])

frame = read_rows("M03_frame.csv")
sample = sorted(frame, key=sort_key)[:10]
trial = sorted(read_rows("M03_trial.csv")[:4], key=sort_key)
assert [int(r["id"]) for r in sample] == [552,542,273,104,361,229,279,440,127,175]
assert len(frame)==600 and sum(int(r["htn"]) for r in frame)==165
assert sum(int(r["htn"]) for r in sample)==4
assert [int(r["id"]) for r in trial]==[3,2,1,4]
frame_rate = mean(int(r["htn"]) for r in frame)
sample_rate = mean(int(r["htn"]) for r in sample)
print(frame_rate, sample_rate, round(100*(sample_rate-frame_rate), 6))
print([(r["id"], "program" if i < 2 else "control") for i,r in enumerate(trial)])
