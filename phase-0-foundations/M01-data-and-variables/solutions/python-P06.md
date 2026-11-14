# پاسخ تمرین 6 — python

[بازگشت به تمرین‌ها](../python/README.md)

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

[بازگشت به تمرین‌ها](../python/README.md)
