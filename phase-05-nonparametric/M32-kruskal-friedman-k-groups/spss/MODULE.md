<div dir="rtl">

# M32 در SPSS

دو طرح مجزا داریم. [گروه‌های مستقل](../data/independent.csv) شامل ۱۸ فرد در سه گروه شش‌نفره است. [جدول بلوکی](../data/blocked_wide.csv) یک ردیف برای هر نفر و یک ستون برای هر وضعیت دارد. [دادهٔ اصلی](../data/practice.csv) هر دو را با ستون `design` جدا می‌کند. اگر فایل پهن را دوباره می‌سازید، ستون وضعیت را از کد `group` بگیرید و ترتیب سطرها را ملاک قرار ندهید.

## گروه‌های مستقل

۱. فایل [دستورها](M32_module.sps) را در `File → Open → Syntax` باز کنید. در دو فرمان `GET DATA` مسیر کامل CSV را در کوتیشن بنویسید یا پوشهٔ جاری SPSS را به پوشهٔ همین ماژول ببرید. تا خط `K-W` را انتخاب کنید و `Run → Selection` را بزنید. `FIRSTCASE=2` سطر سربرگ را رد می‌کند. `K-W` آزمون مستقل است و `group_id(1,3)` دامنهٔ کد گروه را تعیین می‌کند.

۲. از منو هم می‌توان فایل مستقل را از `File → Import Data → CSV Data` وارد کرد. در `Variable View` هر دو ستون باید عددی باشند. در `Analyze → Nonparametric Tests → Legacy Dialogs → K Independent Samples`، `value` را به `Test Variable List` و `group_id` را به `Grouping Variable` ببرید. در `Define Range` کمینهٔ ۱ و بیشینهٔ ۳ را بدهید. `Kruskal–Wallis H` را انتخاب کنید. در `Ranks` شش فرد برای هر گروه و در `Test Statistics` آماره و P را بخوانید.

۳. در نسخهٔ دارای `Exact Tests` یا `Premium` بعد از واردکردن دادهٔ مستقل جملهٔ `NPAR TESTS /J-T=value BY group_id(1,3).` را جدا اجرا کنید. از ستارهٔ ابتدای خط در فایل بگذرید و تنها خود دستور را اجرا کنید. علامت Z جهت را نشان می‌دهد. P دوطرفه و دقیق را جدا از تقریب یک‌طرفهٔ دوره بخوانید. اگر گزینهٔ J–T در دسترس نیست، J و P را از کاربرگ یا کد R و Python بازتولید کنید.

## داده‌های وابسته

۱. قسمت دوم `GET DATA` را اجرا کنید تا دادهٔ پهن باز شود. `Data View` هشت ردیف با `block_id`، `t1`، `t2` و `t3` دارد. در منو `Analyze → Nonparametric Tests → Legacy Dialogs → K Related Samples`، ستون‌های `t1` تا `t3` را به فهرست ببرید و `Friedman` و `Kendall’s W` را انتخاب کنید. `block_id` شناسه است و در فهرست سنجش‌ها جایی ندارد.

۲. در جدول رتبه، میانگین‌ها پیش از گرد کردن باید ۱٫۳۷۵، ۲ و ۲٫۶۲۵ باشند. تعداد بلوک‌ها هشت است. `Asymp. Sig.` فقط P تقریبی است. برای Dunn و Conover با Holm و برای Quade و P دقیق، فایل Excel یا کد R و Python را دنبال کنید. اگر از رابط دیگری از SPSS جدول مقایسهٔ جفت‌ها گرفته‌اید، نوع تعدیل را از پاورقی همان جدول بخوانید.

## کنترل خروجی

در نمونهٔ مستقل `H=4.5263`، `P=0.1040` و میانگین رتبه‌ها ۶، ۱۰ و ۱۲٫۵ هستند. روند افزایشی `J=81` و P یک‌طرفهٔ تقریبی ۰٫۰۱۴۵ می‌دهد. در نمونهٔ بلوکی `Q=6.25`، `P≈0.04394`، `W=0.390625` و `F Quade=5.28070` است. اگر شمارش دقیق Friedman را اجرا می‌کنید، مقدار کنترل `78786 / 1679616 = 0.04690715` است. برای جفت‌ها نام روش و تعدیل را کنار عدد نگه دارید. [جدول کامل کنترل‌ها](../lessons/README.md)

<details>
<summary>فیلم و مرجع نوشتاری</summary>

- [فیلم آموزشی](https://www.youtube.com/watch?v=3CzMIMCZbrU). محاسبه و تفسیر Kruskal–Wallis در SPSS. برای دادهٔ پهن و Friedman راهنمای مکتوب همین ماژول را دنبال کنید.
- [مرجع نوشتاری](https://www.ibm.com/docs/en/spss-statistics/30.0.0?topic=reference-npar-tests).
- [دستور J–T و نیازمندی نسخه](https://www.ibm.com/docs/en/spss-statistics/30.0.0?topic=tests-j-t-subcommand-npar-command).

</details>

[بازگشت به درس](../lessons/README.md) · [پاسخ‌ها](../solutions/module.md)

</div>
