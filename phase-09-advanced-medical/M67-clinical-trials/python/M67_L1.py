import csv
from math import isclose
with open("data/M67_L1.csv", newline="") as stream:
    program, control = list(csv.DictReader(stream))
def rate(row, numerator, denominator):
    return int(row[numerator])/int(row[denominator])
itt = rate(program,"success","n")-rate(control,"success","n")
adherent = rate(program,"adherent_success","adherent_n")-rate(control,"adherent_success","adherent_n")
assert isclose(itt,.1) and isclose(adherent,37/240)
print(itt,adherent,1+19*.05)
