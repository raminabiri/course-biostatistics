<div dir="rtl">

# M31 در GraphPad Prism

[دادهٔ پایه](../data/practice.csv) هفت مقدار A و هفت B دارد. [دادهٔ افزوده](../data/extended.csv) ۲۴ مشاهده در هر گروه و مقدارهای مساوی دارد. جهت برآورد در این درس A−B است.

## دو گروه و دو آزمون

۱. از File → New Project، جدول Column با دو ستون A و B بسازید. مقدارهای هر گروه را در ستون خودش بریزید. ردیف هم‌شماره در دو ستون جفت تعریف نمی‌کند. از Analyze → t tests (and nonparametric tests) طرح Unpaired و سپس Nonparametric را بگیرید.

۲. Mann–Whitney را انتخاب و در Results، U و P و روش محاسبه را بخوانید. در بعضی نسخه‌ها U کوچک‌تر نمایش داده می‌شود. برای دانستن جهت، میانگین رتبه‌ها و A−B را ببینید. در گزینه‌ها می‌توانید فاصلهٔ برآورد اختلاف را درخواست کنید. اگر خروجی Hodges–Lehmann یا Difference between medians دارد، برچسب و جهت آن را با برآورد ۲ در کاربرگ بسنجید. [راهنمای برآورد اختلاف](https://www.graphpad.com/guides/prism/latest/statistics/how_the_mann-whitney_test_works.htm)

۳. تحلیل تازهٔ همان جدول را با Kolmogorov–Smirnov اجرا کنید. داده‌های خام را در Column نگاه دارید. در نتایج بخش توزیع تجمعی و بزرگ‌ترین فاصله را ببینید. انتظار D≈۰٫۲۸۶ است. نسخه و نام روش P را بنویسید.

## جدول میانه

از داده یک جدول Contingency با ردیف‌های A و B و ستون‌های بالا و برابر یا پایین بسازید. شمارها A=(۴،۳) و B=(۳،۴) هستند. در Analyze آزمون Fisher exact و حالت دوطرفه را انتخاب کنید. P را کنار عنوان جدول میانه بنویسید. برای محاسبهٔ عددی دقیق یا نسخه‌های دارای مسیر متفاوت، [کاربرگ](../excel/M31_module.xlsx) و [روش R](../r/MODULE.md) همان داده را تحلیل می‌کنند.

## کنترل خروجی

پایه، U_A=۳۲ و P دقیق≈۰٫۳۸۲۸۶۷، D=۲/۷ و P دقیق≈۰٫۹۶۲۷۰۴، HL=۲ و P فیشر=۱. افزوده، U_A=۳۵۷ و P تقریبی بدون اصلاح پیوستگی≈۰٫۱۵۴۱۲۳، D≈۰٫۲۰۸۳۳۳ و P جایگشتیِ مشروط≈۰٫۵۷۸۴۰۲ است.

<details>
<summary>فیلم و مرجع نوشتاری</summary>

- [فیلم آموزشی](https://www.graphpad.com/series/key-analysis-t-test). مقدماتی. بخش مقایسهٔ دو گروه جدا را برای ورود دادهٔ خام ببینید. انتخاب Mann–Whitney یا KS در راهنمای مکتوب آمده است.
- [مرجع نوشتاری](https://www.graphpad.com/guides/prism/latest/statistics/stat_how_to_do_an_unpaired_t_test_w_3.htm).

</details>

[بازگشت به درس](../lessons/README.md) · [پاسخ‌ها](../solutions/module.md)

</div>
