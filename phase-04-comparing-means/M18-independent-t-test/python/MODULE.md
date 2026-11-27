<div dir="rtl">

# M18 در Python

[فایل دادهٔ آموزشی](../data/values.csv) را دانلود کنید. ستون A و B هر کدام زمان هشت نفر جداگانه را دارند. اولین عدد A برابر ۴۷ و اولین عدد B برابر ۴۵ است. این دو عدد صرفاً در یک ردیف نوشته شده‌اند. جهت اثر در تمام مراحل A منهای B است.

## اجرا

پوشهٔ ماژول را در ویرایشگر باز کنید. اگر NumPy و SciPy را در همان مفسر M01 نصب نکرده‌اید، در Terminal اجرا کنید `python -m pip install numpy scipy`. سپس [اسکریپت تمرین](M18_workshop.py) را با `python python/M18_workshop.py` اجرا کنید. اگر دستور Python در سیستم شما `python3` است آن را در هر دو فرمان یکسان به کار ببرید.

## خواندن داده و آزمون

```python
import numpy as np
from scipy.stats import ttest_ind

a, b = np.loadtxt("data/values.csv", delimiter=",", skiprows=1, unpack=True)
fit = ttest_ind(a, b, equal_var=False, alternative="two-sided")
print(fit.statistic, fit.df, fit.pvalue)
print(fit.confidence_interval(confidence_level=0.95))
```

`delimiter=","` جداکنندهٔ CSV است. `skiprows=1` سرستون متنی را می‌گذرد. `unpack=True` یک آرایه برای هر ستون می‌دهد. `equal_var=False` گزینهٔ Welch را فعال می‌کند. حذف این آرگومان، آزمون را به حالت واریانس برابر می‌برد. واژهٔ `two-sided` یعنی انحراف از صفر را در هر دو جهت بررسی می‌کنیم.

اختلاف ۳٫۸۷۵، آمارهٔ t برابر ۱٫۷۶۸۴۴، درجهٔ آزادی ۱۳٫۷۰۹۷، مقدار P دوطرفه ۰٫۰۹۹۲۲ و فاصلهٔ اطمینان ۹۵٪ از −۰٫۸۳۴ تا ۸٫۵۸۴ است. اگر Python عدد کوچکی را با e چاپ کرد، مثل `1.0976e-05`، معنی آن ۱٫۰۹۷۶ ضربدر ۱۰ به توان منفی ۵ است. اگر FileNotFoundError دریافت کردید، مسیر اجرای ترمینال و وجود پوشهٔ data را بررسی کنید.

<details>
<summary>فیلم و مرجع نوشتاری</summary>

- [فیلم آموزشی](https://www.youtube.com/watch?v=tSOSOlWQq-s). در فیلم به ورود آرایه و خواندن نتیجهٔ ttest_ind توجه کنید.
- [مرجع نوشتاری](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html).

</details>

[بازگشت به درس](../lessons/README.md) · [پاسخ‌ها](../solutions/module.md)

</div>
