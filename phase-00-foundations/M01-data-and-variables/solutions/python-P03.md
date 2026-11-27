<div dir="rtl">

# پاسخ تمرین 3 — python

[بازگشت به تمرین‌ها](../python/README.md)

```python
print(round(uti["crp"].mean(), 2))  # به‌دست‌آوردن میانگین
uti["crp"] = uti["crp"].replace(-99, pd.NA).astype("Float64")  # تبدیل کد ویژه به گمشده
print(uti["crp"].notna().sum())  # شناخت مقدارهای پر
print(round(float(uti["crp"].mean()), 2))  # به‌دست‌آوردن میانگین
print(uti["wbc"].isna().sum())  # شناخت خانه‌های گمشده
```
```
35.1
28
44.68
1
```
**جواب:** میانگین از **35.10** (غلط) به **44.68** (درست) رسید. CRP **۲۸** و WBC **۲۹** (۳۰ − ۱) مقدار معتبر دارند.

[بازگشت به تمرین‌ها](../python/README.md)

</div>
