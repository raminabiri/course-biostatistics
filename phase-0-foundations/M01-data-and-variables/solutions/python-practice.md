# پاسخ‌های مسیر python

<a id="answer-1"></a>

## پاسخ 1

```python
uti = pd.read_csv("../data/M01_uti.csv")
print(uti.shape)
```
```
(30, 12)
```
**جواب: ۳۰ سطر، ۱۲ ستون.**

<a id="answer-2"></a>

## پاسخ 2

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

<a id="answer-3"></a>

## پاسخ 3

```python
print(round(uti["crp"].mean(), 2))                     # پیش از تبدیل
uti["crp"] = uti["crp"].replace(-99, pd.NA).astype("Float64")
print(uti["crp"].notna().sum())
print(round(float(uti["crp"].mean()), 2))              # پس از تبدیل
print(uti["wbc"].isna().sum())
```
```
35.1
28
44.68
1
```
**جواب:** میانگین از **35.10** (غلط) به **44.68** (درست) رسید. CRP **۲۸** و WBC **۲۹** (۳۰ − ۱) مقدار معتبر دارند.

<a id="answer-4"></a>

## پاسخ 4

```python
print(uti["ward"].cat.codes.add(1).mean())   # کدهای 0،1،2 ← 1،2،3
print(uti["ward"].value_counts(sort=False))
print(uti["organism"].value_counts(sort=False))
```
```
1.8
ward
Internal    12
Surgery     12
ICU          6
Name: count, dtype: int64
organism
E. coli       17
Klebsiella     9
Proteus        4
Name: count, dtype: int64
```
۱٫۸ «بخش» واقعی‌ای نیست؛ کدها برچسب‌اند (درس ۱.۲). درصدها: `value_counts(normalize=True) * 100` ← 40، 40، 20.

<a id="answer-5"></a>

## پاسخ 5

```python
print(pd.crosstab(uti["sex"], uti["cipro_res"]))
```
```
cipro_res  Resistant  Susceptible
sex                              
Female             7           13
Male               4            6
```
**جواب: ۷.** (ستون‌ها الفبایی مرتب شده‌اند، چون برای `cipro_res` ترتیب `categories` تعیین نکردیم. تمرین اضافه: با `pd.Categorical(..., categories=["Susceptible", "Resistant"])` ترتیب را درست کنید.)

<a id="answer-6"></a>

## پاسخ 6

```python
wide = pd.read_csv("../data/M01_crp_wide.csv")
long = wide.melt(id_vars="id", var_name="day", value_name="crp")
long["day"] = long["day"].str.replace("crp_d", "").astype(int)
print(long.shape)
```
```
(24, 3)
```
**جواب: ۲۴ سطر** (۸ × ۳).

<a id="answer-7"></a>

## پاسخ 7

```python
uti.to_pickle("M01_uti_labeled.pkl")
print(pd.read_pickle("M01_uti_labeled.pkl").dtypes)
```
همهٔ ستون‌های `category` و `crp` با نوع `Float64` سر جایشان هستند. **بله، مانده‌اند.**

