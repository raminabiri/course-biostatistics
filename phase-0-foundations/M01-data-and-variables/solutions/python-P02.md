# پاسخ تمرین 2 — python

[بازگشت به تمرین‌ها](../python/README.md)

```python
uti["sex"] = uti["sex"].map({1: "Female", 2: "Male"}).astype("category")
uti["ward"] = pd.Categorical(
    uti["ward"].map({1: "Internal", 2: "Surgery", 3: "ICU"}),
    categories=["Internal", "Surgery", "ICU"])
uti["organism"] = uti["organism"].astype("category")
uti["cipro_res"] = uti["cipro_res"].map(
    {0: "Susceptible", 1: "Resistant"}).astype("category")
uti["severity"] = pd.Categorical(
    uti["severity"].map({1: "Mild", 2: "Moderate", 3: "Severe"}),
    categories=["Mild", "Moderate", "Severe"], ordered=True)
print(uti.dtypes)
print(uti["severity"].cat.ordered)
```
```
id              int64
age             int64
sex          category
ward         category
organism     category
temp          float64
crp           float64
wbc           float64
pain            int64
severity     category
los             int64
cipro_res    category
True
```

`dtypes` ترتیبی بودن را نشان نمی‌دهد؛ با `.cat.ordered` بررسی می‌کنیم (`True`). `pain` را با خواست قبلی عددی نگه داشتیم (درس ۱.۲، دام ۲).

[بازگشت به تمرین‌ها](../python/README.md)
