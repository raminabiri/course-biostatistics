<div dir="rtl">

# M26 در SPSS

[practice.csv](../data/practice.csv) شامل ۳۲ ردیف است. از y و z برای پایان و از y−y0 و z−z0 برای تغییر کمک می‌گیریم. a و b کد شیوه و تنظیم‌اند.

## اجرای جدول‌های MANOVA

۱. از File → Import Data فایل CSV را باز کنید. در Variable View ستون‌های y، z، y0 و z0 عددی‌اند و a و b را به عنوان کد گروه بشناسید. از Analyze → General Linear Model → Multivariate، y و z را در Dependent Variables و a را در Fixed Factor(s) بگذارید.

۲. در Options، Descriptive statistics و Homogeneity tests را برای بازبینی انتخاب کنید. ردیف a و سپس Pillai’s Trace را در جدول Multivariate Tests پیدا کنید. جداول Box و Levene اطلاعاتی دربارهٔ فرض‌ها می‌دهند. P و درجات آزادی را از همان ردیف اثر بردارید.

۳. برای مدل دو عاملی، b را اضافه کنید و Model را Full factorial بگذارید. این بار ردیف a*b را بخوانید. برای مدل تغییر، در Transform → Compute Variable، dy=y−y0 و dz=z−z0 بسازید. dy و dz را جای دو پاسخ پایان و a را تنها عامل بگذارید.

## فرمان و خواندن نتیجه

[فایل SPSS](M26_module.sps) را از File → Open → Syntax باز کنید. مسیر FILE را در صورت نیاز کامل و Run → All را بزنید. `GLM y z BY a` هر دو پاسخ را در یک مدل قرار می‌دهد. `/DESIGN=a b a*b` دو اثر اصلی و تعامل را در مدل می‌گذارد. `SSTYPE(3)` نوع مجموع مربعات را درخواست می‌کند. در این فایل متوازن، F تعامل با روش R همخوان است.

[فایل ماتریسی](M26_matrix.sps) را نیز می‌توانید در PSPP اجرا کنید. سه ردیف به ترتیب اثر گروه بر پایان، تعامل و اثر گروه بر تغییرها هستند. `SSCP` حاصل ضرب ترانهادهٔ مانده‌ها در خودشان است. `TRACE` ردّ نسبت اثر به خطا را برمی‌گرداند. برای اثر یک‌درجه‌ای، همان تنها ریشهٔ ناصفر است. هر ردیف از Pillai تا مقدار P خوانده می‌شود.

## کنترل خروجی

در مدل پایان، اثر A به Pillai≈۰٫۷۱۹۳۸۶ و F(۲،۲۹)≈۳۷٫۱۷۲ می‌رسد. برای تعامل A×B، Pillai≈۰٫۰۹۴۵۳۰ و P≈۰٫۲۶۱۶۹۷ است. برای تفاوت تغییر A، Pillai≈۰٫۰۰۱۱۶۰ و P≈۰٫۹۸۳۳۱۷ است.

<details>
<summary>فیلم و مرجع نوشتاری</summary>

- [فیلم آموزشی](https://www.youtube.com/watch?v=UTi6NqV_9Qs). متوسط. پس از شناخت دو ستون پیامد، انتقال هر دو به Dependent Variables، تعریف عامل و خواندن جدول Multivariate Tests را ببینید.
- [مرجع نوشتاری](https://www.ibm.com/docs/en/spss-statistics/32.0.0?topic=statistics-glm-multivariate-analysis).

</details>

[بازگشت به درس](../lessons/README.md) · [پاسخ‌ها](../solutions/module.md)

</div>
