<div dir="rtl">

# M20 در Python

[فایل practice.csv](../data/practice.csv) ۱۵ ردیف دارد. ردیف اول نام ستون‌هاست. group کد روش و value عدد مشاهده‌شده را نشان می‌دهد. پنج مشاهده به هر روش تعلق دارد.

## اجرا از پوشهٔ ماژول

[فایل کارگاه](M20_workshop.py) را باز کنید. اگر کتابخانه‌ها در مفسر M01 نصب نیستند، `python -m pip install numpy scipy` را در Terminal اجرا کنید. سپس `python python/M20_workshop.py` را بزنید. در سیستم‌هایی که فرمانشان python3 است، هر دو اجرا را با همان نام انجام دهید.

```python
import csv
from scipy import stats

groups = {"A": [], "B": [], "C": []}
with open("data/practice.csv", newline="", encoding="utf-8") as stream:
    for row in csv.DictReader(stream):
        groups[row["group"]].append(float(row["value"]))
result = stats.f_oneway(groups["A"], groups["B"], groups["C"])
print(result.statistic, result.pvalue)
```

`DictReader` نام‌ها را از سطر اول می‌گیرد. `row["group"]` تعیین می‌کند به کدام فهرست برویم. `float` متن هر مشاهده را به عدد تبدیل می‌کند. `append` مقدار را به انتهای فهرست می‌افزاید. در اسکریپت کارگاه، `*groups` فهرست آرایه‌ها را به چند ورودی جدا برای تابع باز می‌کند.

در بخش Welch، `x.var(ddof=1)` واریانس نمونه را با مخرج n−1 به دست می‌دهد. `np.average(means,weights=w)` میانگین وزن‌دار و `stats.f.sf` دنبالهٔ راست توزیع F با درجه‌های آزادی درست را محاسبه می‌کند. در بخش مقایسه‌ها `stats.tukey_hsd` سه آرایه را به همان ترتیب A، B، C می‌گیرد. سطر ۲ و ستون ۰ِ pvalue جفت C−A است، چون شمارش نمایه‌ها در Python از صفر آغاز می‌شود.

## عددهای کنترل

در مدل کلاسیک F≈۱۰٫۶۶۴ و P≈۰٫۰۰۲۱۸ است. در Welch، F≈۹٫۲۶۶ و P≈۰٫۰۰۹۵۵ است. برای C−A اختلاف ۸٫۸ واحد و در Tukey مقدار P تعدیل‌شده حدود ۰٫۰۰۱۶۹ است.

<details>
<summary>فیلم و مرجع نوشتاری</summary>

- [فیلم آموزشی](https://www.youtube.com/watch?v=wRvuJVAS5SM). در فیلم ساخت آرایهٔ هر گروه و خواندن F و P را دنبال کنید.
- [مرجع نوشتاری](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f_oneway.html).

</details>

[بازگشت به درس](../lessons/README.md) · [پاسخ‌ها](../solutions/module.md)

</div>
