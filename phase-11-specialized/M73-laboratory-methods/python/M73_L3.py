import csv
from statistics import mean
with open("data/M73_L3.csv", newline="") as stream:
    rows = list(csv.DictReader(stream))
def average_delta(group):
    return mean(float(row["target"])-float(row["reference"])
                for row in rows if row["group"]==group)
contrast = average_delta("comparison")-average_delta("control")
ratio = 2**(-contrast)
assert contrast == -2 and ratio == 4
print(contrast, ratio)
