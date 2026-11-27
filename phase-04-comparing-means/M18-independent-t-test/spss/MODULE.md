<div dir="rtl">

# M18 در SPSS

[فایل دادهٔ آموزشی](../data/values.csv) را دانلود کنید. ستون A و B هر کدام زمان هشت نفر جداگانه را دارند. اولین عدد A برابر ۴۷ و اولین عدد B برابر ۴۵ است. این دو عدد صرفاً در یک ردیف نوشته شده‌اند. جهت اثر در تمام مراحل A منهای B است.

## اجرا با منو

[دادهٔ بلند](../data/long.csv) را از File → Import Data → CSV Data باز کنید. در Variable View باید group از نوع String و value از نوع Numeric باشد. در Data View ستون group کد A یا B و ستون value زمان هر فرد را نشان می‌دهد. از Analyze → Compare Means → Independent-Samples T Test، متغیر value را به Test Variable(s) و group را به Grouping Variable ببرید. از Define Groups به ترتیب A و B را وارد کنید. در جدول Independent Samples Test ردیف Equal variances not assumed را بخوانید.

## بازتولید با Syntax

[فایل فرمان](M18_module.sps) را دانلود و از File → Open → Syntax باز کنید. در دستور GET DATA مسیر FILE را با مسیر کامل فایل CSV جایگزین کنید و گیومه‌ها را نگه دارید. Run → All را بزنید. `FIRSTCASE=2` سطر سرستون را کنار می‌گذارد. `GROUPS=grp('A','B')` هم دو گروه و هم ترتیب تفاضل را تعیین می‌کند. نسخهٔ فرمان، ستون اول CSV را grp می‌نامد. گزینهٔ `CI(.95)` سطح فاصله را روی ۹۵٪ می‌گذارد.

## خواندن جدول

اختلاف ۳٫۸۷۵، آمارهٔ t برابر ۱٫۷۶۸۴۴، درجهٔ آزادی ۱۳٫۷۰۹۷، مقدار P دوطرفه ۰٫۰۹۹۲۲ و فاصلهٔ اطمینان ۹۵٪ از −۰٫۸۳۴ تا ۸٫۵۸۴ است. اگر جدول P کوچک را به صورت .000 نشان داد، رقم‌های نمایش را بیشتر کنید یا آن را به صورت P<۰٫۰۰۱ بنویسید. در تمرین کنترلی، ابتدا عنوان تفاضل و سپس مقدار P و کران‌ها را در خروجی پیدا کنید.

<details>
<summary>فیلم و مرجع نوشتاری</summary>

- [فیلم آموزشی](https://guides.lib.uoguelph.ca/c.php?g=525348&p=5374874). در صفحهٔ دانشگاه Guelph ویدئوی Independent Samples T-Test را باز کنید.
- [مرجع نوشتاری](https://www.ibm.com/docs/en/spss-statistics/31.0.0?topic=tests-independent-samples-t-test).

</details>

[بازگشت به درس](../lessons/README.md) · [پاسخ‌ها](../solutions/module.md)

</div>
