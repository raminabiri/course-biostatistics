<div dir="rtl">

# پاسخ تمرین 2 — python

[بازگشت به تمرین‌ها](../python/README.md)

```python
uti["sex"] = uti["sex"].map({1: "Female", 2: "Male"}).astype("category")  # پیوند کد با نام رده
uti["ward"] = pd.Categorical(  # تعریف رده‌های داده
    uti["ward"].map({1: "Internal", 2: "Surgery", 3: "ICU"}),  # پیوند کد با نام رده
    categories=["Internal", "Surgery", "ICU"])  # تعیین رده‌ها و ترتیب آن‌ها
uti["organism"] = uti["organism"].astype("category")
uti["cipro_res"] = uti["cipro_res"].map(  # پیوند کد با نام رده
    {0: "Susceptible", 1: "Resistant"}).astype("category")
uti["severity"] = pd.Categorical(  # تعریف رده‌های داده
    uti["severity"].map({1: "Mild", 2: "Moderate", 3: "Severe"}),  # پیوند کد با نام رده
    categories=["Mild", "Moderate", "Severe"], ordered=True)  # تعیین رده‌ها و ترتیب آن‌ها
print(uti.dtypes)  # دیدن نوع ستون‌ها
print(uti["severity"].cat.ordered)  # نمایش نتیجه در خروجی
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

</div>
