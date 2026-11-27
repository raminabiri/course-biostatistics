import csv
from statistics import mean
with open("data/M70_L2.csv", newline="") as stream:
    values = [int(row["requests"]) for row in csv.DictReader(stream)]
train, test = values[:8], values[8:]
baseline = train[-4:]
growth = mean(new-old for old,new in zip(train,baseline))
base_error = mean(abs(y-p) for y,p in zip(test,baseline))
adjusted_error = mean(abs(y-p-growth) for y,p in zip(test,baseline))
drift = (train[-1]-train[0])/(len(train)-1)
forecast = [train[-1]+h*drift for h in range(1,len(test)+1)]
assert (base_error,adjusted_error)==(4,0)
print(base_error,adjusted_error,forecast)
