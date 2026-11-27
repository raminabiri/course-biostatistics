<div dir="rtl">

# M27 در SPSS

[practice.csv](../data/practice.csv) ۳۲ ردیف دارد. a و b کد دو عامل، y و z پاسخ پایان و baseline هم‌متغیر است. مدل نخست تنها با B0 اجرا می‌شود. در هر سه مدل از x=baseline−25 کمک می‌گیریم.

## اجرای مدل در یک تنظیم

۱. از File → Import Data → CSV Data، سرستون‌ها و جداکنندهٔ Comma را انتخاب کنید. در Variable View، y و z و baseline عددی‌اند. از Transform → Compute Variable نام x و عبارت baseline−25 را وارد کنید. با Data → Select Cases و شرط b=0 مدل نخست را آماده کنید.

۲. از Analyze → General Linear Model → Multivariate، y و z را در Dependent Variables، a را در Fixed Factor(s) و x را در Covariate(s) بگذارید. مدل دارای x و a است. در Multivariate Tests، ردیف a و سپس Pillai را بخوانید. برای پیش‌بینی در ۲۵، ESTIMATED MEANS را در x=0 درخواست کنید. [فایل Syntax](M27_module.sps) خط دقیق `EMMEANS=TABLES(a) WITH(x=0) COMPARE(a)` را دارد.

## آزمون دو تعامل

فیلتر را با All cases بردارید. برای مدل دوم a و b را عامل و x را هم‌متغیر بگذارید. در Custom Model، x، a، b و a*b را انتخاب کنید. در مدل سوم a*x را به همین فهرست اضافه کنید. در ردیف a*b و a*x از جدول چندمتغیره F و P را بخوانید. در فایل Syntax، TEMPORARY سبب می‌شود فیلتر b=0 فقط برای مدل اول برقرار باشد. مسیر FILE را کامل کنید و Run → All را بزنید.

[فرمان ماتریسی](M27_matrix.sps) مدل‌ها را در PSPP نیز اجرا می‌کند. دستور GET دادهٔ دو پاسخ را وارد محاسبه می‌کند. دو ماتریس طراحی اثر یک‌درجه‌ای را جدا می‌کنند. سه ردیف آزمون به‌ترتیب A در B0، تعامل A×B و تعامل A×x هستند.

## کنترل خروجی

در B0 و خط پایهٔ ۲۵، بردار پیش‌بینی A0 حدود (۴۴٫۳۶۶،۲۶٫۰۷۳) و A1 حدود (۴۷٫۹۵۵،۲۴٫۰۵۲) است. P آزمون مشترک A≈۰٫۰۱۰۹۶۴، برای A×B≈۰٫۲۷۳۴۶۹ و برای A×خط پایه≈۰٫۲۹۹۳۷۹ است.

<details>
<summary>فیلم و مرجع نوشتاری</summary>

- [فیلم آموزشی](https://www.youtube.com/watch?v=GrX7tW8nqbw). متوسط. در ویدئوی یک‌عاملی، تعیین دو پیامد، عامل و هم‌متغیر و خواندن آزمون چندمتغیره را ببینید.
- [مرجع نوشتاری](https://www.ibm.com/docs/en/spss-statistics/32.0.0?topic=statistics-glm-multivariate-analysis).

</details>

[بازگشت به درس](../lessons/README.md) · [پاسخ‌ها](../solutions/module.md)

</div>
