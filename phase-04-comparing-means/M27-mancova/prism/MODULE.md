<div dir="rtl">

# M27 در GraphPad Prism

[practice.csv](../data/practice.csv) ۳۲ ردیف دارد. a و b کد دو عامل، y و z پاسخ پایان و baseline هم‌متغیر است. مدل نخست تنها با B0 اجرا می‌شود. در هر سه مدل از x=baseline−25 کمک می‌گیریم.

## دیدن خط پایه و تفاوت شیب

۱. از File → New Project جدول XY بسازید. در ردیف‌های B0، X را x=baseline−25 و Y را y بگذارید. برای هر کد A یک مجموعهٔ Y بسازید. در هر ردیف مقدار y فقط زیر مجموعهٔ گروه خودش وارد شود. همین چیدمان را با z در جدولی جدا تکرار کنید. نمودارهای پراکنش نشان می‌دهند کدام بازهٔ خط پایه مشترک است.

۲. در Analyze → Simple Linear Regression گزینهٔ آزمون تفاوت شیب و عرض از مبدأ را فعال کنید. در این خروجی، رابطهٔ یک سنجه با x را در دو گروه می‌بینید. نتیجه را با نام همان پاسخ بخوانید. X=0 همان خط پایهٔ ۲۵ است.

## پیش‌بینی تعدیل‌شدهٔ هر پاسخ

در جدول Multiple Variables، برای B0، ستون‌های y، z، a و x را با مقادیر همان ردیف وارد کنید. در Multiple linear regression یک بار y و بار دوم z را پاسخ و a و x را پیش‌بین بگذارید. پیش‌بینی A0 در x=0 همان Intercept و برای A1 جمع Intercept و ضریب a است. برای نمودار دو عاملی، شکل‌های B0 و B1 را با واحدهای محوری یکسان مقایسه کنید.

Prism در این مسیر پیش‌بینی تک‌پاسخی و نمودار می‌دهد. آزمون مشترک و درجات آزادی را از [کاربرگ](../excel/M27_module.xlsx) یا [R](../r/MODULE.md) بگیرید. [دامنهٔ تحلیل‌های Prism](https://www.graphpad.com/support/faq/do-any-graphpad-programs-perform-multivariate-statistical-tests/)

## کنترل خروجی

در B0 و خط پایهٔ ۲۵، بردار پیش‌بینی A0 حدود (۴۴٫۳۶۶،۲۶٫۰۷۳) و A1 حدود (۴۷٫۹۵۵،۲۴٫۰۵۲) است. P آزمون مشترک A≈۰٫۰۱۰۹۶۴، برای A×B≈۰٫۲۷۳۴۶۹ و برای A×خط پایه≈۰٫۲۹۹۳۷۹ است.

<details>
<summary>فیلم و مرجع نوشتاری</summary>

- [فیلم آموزشی](https://www.graphpad.com/series/data-analysis). متوسط. بخش Multiple linear regression را پس از شناخت خط پایه ببینید. این مسیر پیش‌بینی یک سنجه در هر مدل و نمودار را فراهم می‌کند.
- [مرجع نوشتاری](https://www.graphpad.com/guides/prism/latest/curve-fitting/reg_comparingslopesandintercepts.htm).

</details>

[بازگشت به درس](../lessons/README.md) · [پاسخ‌ها](../solutions/module.md)

</div>
