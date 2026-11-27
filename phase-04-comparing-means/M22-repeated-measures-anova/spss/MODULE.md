<div dir="rtl">

# M22 در SPSS

از [جدول پهن](../data/wide.csv) ستون‌های id، t0c0، t1c0 و t2c0 را پیدا کنید. هر ردیف یک فرد است. هر سه اندازه باید برای همان ردیف کنار هم بمانند. شرط صفر همان c0 در نام ستون‌هاست.

## تعریف عامل درون‌فردی

۱. از File → Import Data → CSV Data فایل پهن را انتخاب کنید. سطر اول نام ستون‌هاست. از Variable View نگاه کنید که t0c0، t1c0 و t2c0 از نوع Numeric هستند. در Data View بررسی کنید هر شناسه فقط یک ردیف دارد.

۲. از Analyze → General Linear Model → Repeated Measures، نام time و Number of Levels = 3 را وارد کنید. Add و سپس Define را بزنید. ستون‌های t0c0، t1c0 و t2c0 را به همین ترتیب در خانه‌های عامل بچینید. ستون‌های c1 مربوط به شرط دیگری‌اند. در Options، Descriptive statistics را برای دیدن میانگین‌ها فعال کنید.

۳. خروجی Mauchly جدولی دربارهٔ کرویت است. در Tests of Within-Subjects Effects ردیف time را پیدا کنید. Sphericity Assumed عددهای کلاسیک و Greenhouse-Geisser عددهای بازبینی‌شده را می‌دهد. F زمان در هر دو ردیف یکسان است. درجه‌های آزادی و P متفاوت‌اند. df مخرج را از ردیف Error(time) بخوانید.

## مقایسه‌ها و اجرای آماده

برای آزمون زوجی مستقیم از Analyze → Compare Means → Paired-Samples T Test کمک بگیرید. t2c0 را نخست و t0c0 را دوم بگذارید. جدول Paired Samples Test تفاضل، فاصلهٔ تکی و P دوطرفه را نشان می‌دهد. برای خانوادهٔ سه جفت، هر سه P خام را بردارید و Holm را مانند درس انجام دهید.

[فایل فرمان SPSS](M22_module.sps) را از File → Open → Syntax باز کنید. اگر پوشهٔ کاری شما پوشهٔ ماژول نیست، مسیر FILE را به مسیر کامل wide.csv تغییر دهید. Run → All را بزنید. WSFACTOR سه سطح زمان را معرفی می‌کند و WSDESIGN مشخص می‌کند زمان عامل درون‌فردی است. در سطر T-TEST دو فهرست پیش و پس از WITH به ترتیب خانه‌های جفت‌اند. [فایل PSPP](M22_pspp.sps) آزمون زمان با فرض کرویت و سه آزمون زوجی را بازتولید می‌کند.

## کنترل نتیجه

F(۲،۲۲)≈۲۵٫۱۰۹۶ و P خام زمان ≈۰٫۰۰۰۰۰۲۰۹۶ است. ضریب گرین‌هاوس–گایزر ≈۰٫۹۰۴۵۶۵ و P بازبینی‌شده ≈۰٫۰۰۰۰۰۵۶۵۵ است. تغییر T2−T0 برابر ۵٫۲۰۸۳ و P خام زوجی ≈۰٫۰۰۰۰۲۲۹۱۴ است.

<details>
<summary>فیلم و مرجع نوشتاری</summary>

- [فیلم آموزشی](https://www.youtube.com/watch?v=I7e6mr11-Rc). متوسط. پس از شناخت طرح زوجی، فیلم را برای تعریف عامل درون‌فردی و ترتیب ستون‌ها ببینید.
- [مرجع نوشتاری](https://www.ibm.com/docs/en/spss-statistics/30.0.0?topic=reference-glm-repeated-measures).

</details>

[بازگشت به درس](../lessons/README.md) · [پاسخ‌ها](../solutions/module.md)

</div>
