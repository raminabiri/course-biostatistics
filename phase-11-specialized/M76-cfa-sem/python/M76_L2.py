import csv
from math import sqrt,isclose
from statistics import mean
with open("data/M76_L2.csv") as f:
    records=csv.reader(f)
    next(records)
    matrix=[[float(x) for x in row[1:]] for row in records]
def loads(start):
    i,j,k=range(start,start+3)
    first=sqrt(matrix[i][j]*matrix[i][k]/matrix[j][k])
    return first,matrix[i][j]/first,matrix[i][k]/first
fatigue,activity=loads(0),loads(3)
cross=[matrix[i][j+3]/(f*a) for i,f in enumerate(fatigue) for j,a in enumerate(activity)]
assert all(isclose(value,.35) for value in cross)
print(fatigue,activity,mean(cross))
