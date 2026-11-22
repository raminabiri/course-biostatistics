# رسم در Python

از پوشهٔ M08 و در محیط دارای pandas و matplotlib اجرا کنید.

```python
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data/M08_followup.csv")
for group, rows in data.groupby("group"):
    plt.scatter(rows["age"], rows["day0"], label=group)
plt.xlabel("Age (years)")
plt.ylabel("Baseline systolic BP (mmHg)")
plt.legend()
plt.show()
```

برای توزیع از `hist`، `boxplot` یا `violinplot` و برای پیگیری یک `plot` برای هر شناسه به کار ببرید. در نمودار زمانی مقادیر NaN را نگه دارید تا خط در نوبت گمشده شکاف داشته باشد.
