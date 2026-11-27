<div dir="rtl">

# M31 در SPSS

[دادهٔ پایه](../data/practice.csv) هفت مقدار A و هفت B دارد. [دادهٔ افزوده](../data/extended.csv) ۲۴ مشاهده در هر گروه و مقدارهای مساوی دارد. جهت برآورد در این درس A−B است.

## ورود داده و تحلیل دو گروه

۱. از File → Import Data → CSV Data داده را با سرستون و جداکنندهٔ Comma وارد کنید. در Transform → Recode into Different Variables، گروه A را ۱ و B را ۲ و نام متغیر را group_id بگذارید. value سنجهٔ عددی است.

۲. از Analyze → Nonparametric Tests → Legacy Dialogs → 2 Independent Samples، value را در Test Variable List و group_id را در Grouping Variable بگذارید. Define Groups را با ۱ و ۲ کامل کنید. Mann–Whitney U را برای رتبه و Kolmogorov–Smirnov را برای فاصلهٔ توزیع انتخاب کنید. اگر U=۱۷ چاپ شد، مقدار کوچک‌ترِ دو U است. برای KS، اختلاف مطلق و Z را با برچسبشان بخوانید.

۳. برای آزمون میانه، میانهٔ ادغام را از Frequencies بگیرید و در Transform → Compute Variable، above=(value>11.5) را برای فایل پایه بسازید. در Analyze → Descriptive Statistics → Crosstabs، گروه و above را بگذارید و جدول شمار ۲×۲ را بخوانید.

## اجرای فرمان و کنترل دقیق

[فایل SPSS](M31_module.sps) آزمون‌های منو و HL را از داده می‌سازد. فایل [محاسبهٔ دقیق](M31_exact.sps) ۳۴۳۲ تخصیص معتبر را می‌شمارد و سپس U، D، Pهای دقیق و HL را چاپ می‌کند. این مسیر برای ۱۴ مقدار متمایز و جدول میانهٔ پایه است. اگر PSPP دارید، [فایل منوی سازگار](M31_pspp.sps) جدول رتبه و شمار میانه، و فایل ماتریسی مقدارهای دقیق را می‌دهد. در هر فایل مسیر FILE را کامل و Run → All را بزنید. P تقریبی را با خروجی دقیق مقایسه کنید و نام روش را ثبت کنید.

## کنترل خروجی

پایه، U_A=۳۲ و P دقیق≈۰٫۳۸۲۸۶۷، D=۲/۷ و P دقیق≈۰٫۹۶۲۷۰۴، HL=۲ و P فیشر=۱. افزوده، U_A=۳۵۷ و P تقریبی بدون اصلاح پیوستگی≈۰٫۱۵۴۱۲۳، D≈۰٫۲۰۸۳۳۳ و P جایگشتیِ مشروط≈۰٫۵۷۸۴۰۲ است.

<details>
<summary>فیلم و مرجع نوشتاری</summary>

- [فیلم آموزشی](https://guides.lib.uoguelph.ca/c.php?g=525348&p=5374874). متوسط. بخش Video: Mann-Whitney U Test دانشگاه Guelph را برای تعیین گروه و خواندن جدول آزمون ببینید.
- [مرجع نوشتاری](https://www.ibm.com/docs/en/spss-statistics/32.0.0?topic=tests-two-independent-samples).

</details>

[بازگشت به درس](../lessons/README.md) · [پاسخ‌ها](../solutions/module.md)

</div>
