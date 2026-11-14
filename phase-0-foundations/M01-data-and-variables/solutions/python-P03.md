# پاسخ تمرین 3 — python

[بازگشت به تمرین‌ها](../python/README.md)

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

[بازگشت به تمرین‌ها](../python/README.md)
