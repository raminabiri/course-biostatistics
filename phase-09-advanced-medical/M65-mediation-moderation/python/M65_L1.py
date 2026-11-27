import csv
with open("data/M65_L1.csv", newline="") as stream:
    rows = list(csv.DictReader(stream))
low, high = (int(row["treated"]) - int(row["control"]) for row in rows)
interaction = high-low
indirect = 3*2
assert (low,high,interaction,indirect)==(4,7,3,6)
print(low, high, interaction, indirect, 4+indirect)
