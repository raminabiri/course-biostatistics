<div dir="rtl">

# M21 در SPSS

[دادهٔ آموزشی](../data/practice.csv) ۴۰ مشاهدهٔ مستقل دارد. a، b و c سه عامل با کدهای صفر و یک‌اند. value پاسخ عددی است. از ۲۰ ردیف c=0 برای مدل دوطرفه استفاده می‌کنیم.

## خواندن فایل و تعریف مدل

از File → Import Data → CSV Data فایل را باز کنید. سرستون‌ها را در ردیف اول بگیرید. در Variable View، متغیرهای a، b و c را Numeric و Measure را Nominal بگذارید. value عددی و Scale است.

برای مدل اول از Data → Select Cases و شرط `c=0` استفاده کنید. در Analyze → General Linear Model → Univariate، پاسخ value را به Dependent Variable و a و b را به Fixed Factor(s) ببرید. Model را Full factorial بگذارید. در Tests of Between-Subjects Effects ردیف a*b و سپس Error را بخوانید. در Estimated Marginal Means جدول a*b را درخواست کنید. فایل فرمان مقایسهٔ a در هر b را هم به همین جدول می‌افزاید.

قبل از مدل سه‌طرفه از Data → Select Cases گزینهٔ All cases را برگردانید. c را به Fixed Factor(s) اضافه کنید و دوباره Full factorial را اجرا کنید. جدول a*b*c را بخوانید.

## استفاده از Syntax

از File → Open → Syntax، [فایل M21](M21_module.sps) را باز کنید. در FILE، مسیر CSV را کامل کنید و Run → All را بزنید. `TEMPORARY` باعث می‌شود شرط `SELECT IF` فقط برای آزمون بعدی باشد. `DESIGN` هر اثر را صریح فهرست می‌کند. `SSTYPE(3)` نوع سوم مجموع مربعات را درخواست می‌کند. در این طرح متوازن مقدار تعامل با محاسبهٔ تفاضل‌ها همخوان است. [نسخهٔ فرمان GLM برای PSPP](M21_pspp.sps) دو جدول آزمون را بازتولید می‌کند.

## کنترل نتیجه

با C0، تعامل A×B برابر ۴ واحد و F(۱،۱۶)=۸ با P≈۰٫۰۱۲۱۱ است. اثر سادهٔ A در B1 برابر ۷ واحد است. در دادهٔ کامل، تعامل A×B×C برابر ۲ واحد و F(۱،۳۲)=۰٫۴ با P≈۰٫۵۳۱۵۸ است.

<details>
<summary>فیلم و مرجع نوشتاری</summary>

- [فیلم آموزشی](https://libguides.lib.msu.edu/SPSS/inferential/anova). در صفحهٔ دانشگاه Michigan State، بخش Two Way ANOVA را باز کنید.
- [مرجع نوشتاری](https://www.ibm.com/docs/en/spss-statistics/31.0.0?topic=unianova-overview-command).

</details>

[بازگشت به درس](../lessons/README.md) · [پاسخ‌ها](../solutions/module.md)

</div>
