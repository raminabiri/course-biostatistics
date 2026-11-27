<div dir="rtl">

# M19 در SPSS

[فایل دادهٔ آموزشی](../data/values.csv) را دانلود کنید. هر ردیف یک فرد است و ستون‌های before و after دو زمان را برای همان فرد نشان می‌دهند. ردیف نخست از ۴۷ به ۴۵ رسیده و تفاضل آن −۲ است. جهت اثر در تمام مراحل بعد منهای قبل است.

## اجرا با منو

از File → Import Data → CSV Data فایل values.csv را باز کنید. گزینهٔ نام متغیر در سطر اول را فعال کنید و در Variable View نوع هر دو ستون را Numeric ببینید. مسیر Analyze → Compare Means → Paired-Samples T Test را باز کنید. after را در جای اول و before را در جای دوم زوج بگذارید. پس از OK عنوان after − before را در Paired Samples Test بررسی کنید.

## بازتولید با Syntax

[فایل فرمان](M19_module.sps) را دانلود و از File → Open → Syntax باز کنید. در دستور GET DATA مسیر FILE را با مسیر کامل فایل CSV جایگزین کنید و گیومه‌ها را نگه دارید. Run → All را بزنید. `FIRSTCASE=2` سطر سرستون را کنار می‌گذارد. `PAIRS=after WITH before` ترتیب زوج را تعیین می‌کند. گزینهٔ `CI(.95)` سطح فاصله را روی ۹۵٪ می‌گذارد.

## خواندن جدول

اختلاف −۳٫۸۷۵، آمارهٔ t برابر −۱۱٫۰۵۹۳۴، درجهٔ آزادی ۷، مقدار P دوطرفه ۰٫۰۰۰۰۱۰۹۸ و فاصلهٔ اطمینان ۹۵٪ از −۴٫۷۰۴ تا −۳٫۰۴۶ است. اگر جدول P کوچک را به صورت .000 نشان داد، رقم‌های نمایش را بیشتر کنید یا آن را به صورت P<۰٫۰۰۱ بنویسید. در تمرین کنترلی، ابتدا عنوان تفاضل و سپس مقدار P و کران‌ها را در خروجی پیدا کنید.

<details>
<summary>فیلم و مرجع نوشتاری</summary>

- [فیلم آموزشی](https://guides.lib.uoguelph.ca/c.php?g=525348&p=5374874). در صفحهٔ دانشگاه Guelph ویدئوی Paired Samples T-Test را باز کنید.
- [مرجع نوشتاری](https://www.ibm.com/docs/en/spss-statistics/30.0.0?topic=tests-paired-samples-t-test).

</details>

[بازگشت به درس](../lessons/README.md) · [پاسخ‌ها](../solutions/module.md)

</div>
