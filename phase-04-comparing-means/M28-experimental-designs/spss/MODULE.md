<div dir="rtl">

# M28 در SPSS

[practice.csv](../data/practice.csv) چهار گروه ردیف دارد. design را قبل از تحلیل روی یکی از block، latin، nested و cross بگذارید. نقش ستون‌های u، v و w را از بخش همان طرح بخوانید.

## مدل‌های جمع‌پذیر

از File → Import Data → CSV Data، سرستون و Comma را انتخاب کنید. با Data → Select Cases، design را برای هر تحلیل جدا کنید. در Analyze → General Linear Model → Univariate، برای block پاسخ value، عوامل u و w، و در Custom Model فقط u و w را بگذارید. برای latin به همین ترتیب v را هم اضافه کنید. در جدول Tests of Between-Subjects Effects، ردیف w به شیوه مربوط است.

## آزمون آشیانه‌ای و متقاطع

برای nested در Transform → Compute Variable، lab=10*u+v را بسازید. در Data → Aggregate، u و lab را Break Variables و میانگین value را lab_mean بگذارید. روی جدول شش آزمایشگاه از Analyze → Compare Means → One-Way ANOVA، lab_mean را پاسخ و u را عامل بگذارید. چون چهار ثبت در هر آزمایشگاه داریم، آزمون بر میانگین آزمایشگاه‌ها F کلاسیک بازو را بازتولید می‌کند.

در نسخهٔ دارای Linear Mixed Models، فایل خامِ nested را دوباره بردارید. lab را Subject، u را اثر ثابت و عرض از مبدأ آزمایشگاه را Random بگذارید. برآورد مؤلفه و درجهٔ آزادی به روش انتخابی بستگی دارد. نتیجه را با عنوان روش گزارش کنید.

برای cross، در Univariate، value را پاسخ و u، period و w را عامل بگذارید. فقط سه اثر اصلی را فعال کنید. اثر w مقایسهٔ شیوه با کنترل فرد و دوره است. جهت B−A را در کاربرگ یا ضرایب مدل ببینید. [فایل کامل فرمان](M28_module.sps) و [نسخهٔ PSPP](M28_pspp.sps) داده را برای هر طرح جدا می‌خوانند. مسیر FILE را کامل و Run → All را بزنید.

## کنترل خروجی

بلوک F(۲،۸)≈۸٫۹۷۷ و P≈۰٫۰۰۹۰۳، مربع لاتین F(۳،۶)≈۲۸٫۸۲۲ و P≈۰٫۰۰۰۵۸۳، آشیانه F(۱،۴)≈۹٫۶۱۸ و P≈۰٫۰۳۶۱۸ است. در طرح متقاطع B−A=۲٫۶، اثر دوره=۱٫۳ و فاصلهٔ ۹۵٪ اثر شیوه ۱٫۴۶۷ تا ۳٫۷۳۳ است.

<details>
<summary>فیلم و مرجع نوشتاری</summary>

- [فیلم آموزشی](https://www.youtube.com/watch?v=d2DrsVQwdso). متوسط. در فیلم مربع لاتین، وارد کردن سطر، ستون و شیوه در مدل را دنبال کنید. بخش اثر تصادفی در مرجع IBM آمده است.
- [مرجع نوشتاری](https://www.ibm.com/docs/en/spss-statistics/32.0.0?topic=mixed-examples).

</details>

[بازگشت به درس](../lessons/README.md) · [پاسخ‌ها](../solutions/module.md)

</div>
