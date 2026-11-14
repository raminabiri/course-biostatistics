# پاسخ تمرین 5 — python

[بازگشت به تمرین‌ها](../python/README.md)

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

[بازگشت به تمرین‌ها](../python/README.md)
