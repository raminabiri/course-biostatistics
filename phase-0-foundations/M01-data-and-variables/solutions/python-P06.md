<div dir="rtl">

# پاسخ تمرین 6 — python

[بازگشت به تمرین‌ها](../python/README.md)

```python
wide = pd.read_csv("../data/M01_crp_wide.csv")  # خواندن فایل و ساخت جدول
long = wide.melt(id_vars="id", var_name="day", value_name="crp")  # تبدیل جدول پهن به بلند
long["day"] = long["day"].str.replace("crp_d", "").astype(int)  # برداشتن پیشوند و ساخت روز عددی
print(long.shape)  # شمار سطر و ستون
```
```
(24, 3)
```
**جواب: ۲۴ سطر** (۸ × ۳).

[بازگشت به تمرین‌ها](../python/README.md)

</div>
