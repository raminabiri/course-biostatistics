# پاسخ تمرین 4 — python

[بازگشت به تمرین‌ها](../python/README.md)

```python
print(uti["ward"].cat.codes.add(1).mean())  # به‌دست‌آوردن میانگین
print(uti["ward"].value_counts(sort=False))  # شمار هر رده
print(uti["organism"].value_counts(sort=False))  # شمار هر رده
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

[بازگشت به تمرین‌ها](../python/README.md)
