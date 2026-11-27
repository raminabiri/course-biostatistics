<div dir="rtl">

# M20 در SPSS

[فایل practice.csv](../data/practice.csv) ۱۵ ردیف دارد. ردیف اول نام ستون‌هاست. group کد روش و value عدد مشاهده‌شده را نشان می‌دهد. پنج مشاهده به هر روش تعلق دارد.

## آماده‌سازی و آزمون کلاسیک

۱. از File → Import Data → CSV Data فایل داده را باز کنید. عنوان‌های سطر اول و جداکنندهٔ Comma را انتخاب کنید. در Variable View بررسی کنید value عددی است. برای عاملِ عددی، از Transform → Recode into Different Variables، کدهای A، B و C را به ۱، ۲ و ۳ ببرید و نام متغیر جدید را method بگذارید.

۲. از Analyze → Compare Means → One-Way ANOVA، value را در Dependent List و method را در Factor بگذارید. گزینهٔ Descriptive تعداد و میانگین هر گروه را در خروجی می‌آورد. جدول ANOVA را بخوانید و درجهٔ آزادی‌های ۲ و ۱۲ را با داده تطبیق دهید.

۳. در Options، Welch و Brown–Forsythe را فعال کنید. در Robust Tests of Equality of Means نام آزمون را کنار مقدار P ثبت کنید. برای هر سه جفت همراه فرض واریانس مشترک، از Post Hoc گزینهٔ Tukey را انتخاب کنید. برای مقایسهٔ C−A در Contrasts به ترتیب کدها −۱، ۰ و ۱ را وارد کنید. ستون Mean Difference ممکن است A−C را نشان دهد. برچسب جفت را پیش از گزارش جهت بخوانید.

## اجرا از فایل فرمان

[فایل Syntax](M20_module.sps) را باز کنید. اگر SPSS خارج از پوشهٔ ماژول آغاز شده، متن بین گیومه‌های FILE را با مسیر کامل CSV عوض کنید. Run → All را بزنید. GET DATA داده را می‌خواند، RECODE گروه‌ها را عددی می‌کند و ONEWAY جدول را می‌سازد. پس از اجرای فایل اصلی، [فایل Welch و براون–فورسایت](M20_robust.sps) را با همان مجموعهٔ فعال اجرا کنید.

## عددهای کنترل

در مدل کلاسیک F≈۱۰٫۶۶۴ و P≈۰٫۰۰۲۱۸ است. در Welch، F≈۹٫۲۶۶ و P≈۰٫۰۰۹۵۵ است. برای C−A اختلاف ۸٫۸ واحد و در Tukey مقدار P تعدیل‌شده حدود ۰٫۰۰۱۶۹ است.

<details>
<summary>فیلم و مرجع نوشتاری</summary>

- [فیلم آموزشی](https://www.youtube.com/watch?v=OEOeXpxSjf8). در فیلم مسیر One-Way ANOVA و خروجی Tukey را پیدا کنید.
- [مرجع نوشتاری](https://www.ibm.com/docs/en/spss-statistics/32.0.0?topic=oneway-statistics-subcommand-command).

</details>

[بازگشت به درس](../lessons/README.md) · [پاسخ‌ها](../solutions/module.md)

</div>
