<div dir="rtl">

# M19 در Python

[فایل دادهٔ آموزشی](../data/values.csv) را دانلود کنید. هر ردیف یک فرد است و ستون‌های before و after دو زمان را برای همان فرد نشان می‌دهند. ردیف نخست از ۴۷ به ۴۵ رسیده و تفاضل آن −۲ است. جهت اثر در تمام مراحل بعد منهای قبل است.

## اجرا

پوشهٔ ماژول را در ویرایشگر باز کنید. اگر NumPy و SciPy را در همان مفسر M01 نصب نکرده‌اید، در Terminal اجرا کنید `python -m pip install numpy scipy`. سپس [اسکریپت تمرین](M19_workshop.py) را با `python python/M19_workshop.py` اجرا کنید. اگر دستور Python در سیستم شما `python3` است آن را در هر دو فرمان یکسان به کار ببرید.

## خواندن داده و آزمون

```python
import numpy as np
from scipy.stats import ttest_rel

before, after = np.loadtxt("data/values.csv", delimiter=",", skiprows=1, unpack=True)
fit = ttest_rel(after, before, alternative="two-sided")
print(fit.statistic, fit.df, fit.pvalue)
print(fit.confidence_interval(confidence_level=0.95))
```

`delimiter=","` جداکنندهٔ CSV است. `skiprows=1` سرستون متنی را می‌گذرد. `unpack=True` یک آرایه برای هر ستون می‌دهد. `ttest_rel` به دو آرایهٔ هم‌طول و هم‌ردیف نیاز دارد. اگر ردیف‌ها را مرتب می‌کنید کل جدول را با هم مرتب کنید. واژهٔ `two-sided` یعنی انحراف از صفر را در هر دو جهت بررسی می‌کنیم.

اختلاف −۳٫۸۷۵، آمارهٔ t برابر −۱۱٫۰۵۹۳۴، درجهٔ آزادی ۷، مقدار P دوطرفه ۰٫۰۰۰۰۱۰۹۸ و فاصلهٔ اطمینان ۹۵٪ از −۴٫۷۰۴ تا −۳٫۰۴۶ است. اگر Python عدد کوچکی را با e چاپ کرد، مثل `1.0976e-05`، معنی آن ۱٫۰۹۷۶ ضربدر ۱۰ به توان منفی ۵ است. اگر FileNotFoundError دریافت کردید، مسیر اجرای ترمینال و وجود پوشهٔ data را بررسی کنید.

<details>
<summary>فیلم و مرجع نوشتاری</summary>

- [فیلم آموزشی](https://www.youtube.com/watch?v=tSOSOlWQq-s). در فیلم به ورود آرایه و خواندن نتیجهٔ ttest_rel توجه کنید.
- [مرجع نوشتاری](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html).

</details>

[بازگشت به درس](../lessons/README.md) · [پاسخ‌ها](../solutions/module.md)

</div>
