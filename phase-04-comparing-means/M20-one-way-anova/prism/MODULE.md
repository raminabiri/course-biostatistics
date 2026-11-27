<div dir="rtl">

# M20 در GraphPad Prism

[فایل practice.csv](../data/practice.csv) ۱۵ ردیف دارد. ردیف اول نام ستون‌هاست. group کد روش و value عدد مشاهده‌شده را نشان می‌دهد. پنج مشاهده به هر روش تعلق دارد.

## از داده تا Results

۱. File → New Project را بزنید. Column را انتخاب کنید و در سه ستون A، B و C مقدارهای خام هر گروه را وارد کنید. هر ستون باید دقیقاً پنج عدد داشته باشد. چون طرح مستقل است، ردیف‌های هم‌شماره با هم جفت نمی‌شوند.

۲. Analyze → One-way ANOVA را باز کنید. در Experimental Design گزینهٔ No matching را بگذارید. توزیع Normal و فرض انحراف استاندارد برابر را انتخاب کنید. پس از اجرای Ordinary one-way ANOVA، F و P کلی را در Results یادداشت کنید.

۳. برای اجرای Welch در گزینه‌های همان تحلیل، فرض برابری انحراف معیار گروه‌ها را بردارید. Prism هر دو تحلیل Welch و Brown–Forsythe را گزارش می‌کند. جدول واریانس‌ها را جدا از جدول برابری میانگین‌ها بخوانید. P≈۰٫۰۰۴۷۲ مربوط به براون–فورسایت میانگین‌ها در کارگاه است.

## پرسش پس از آزمون کلی

با تنظیم کلاسیک در Multiple Comparisons، Compare each mean with every other mean را انتخاب کنید و Tukey را بگذارید. در ردیف C و A، عنوان اختلاف، P تعدیل‌شده و فاصله را بخوانید. اگر A کنترل طرح است، گزینهٔ مقایسهٔ هر گروه با کنترل و روش Dunnett پرسش دیگری را اجرا می‌کند. برای نسخهٔ واریانس نابرابر از گزینهٔ Games–Howell برای جفت‌ها استفاده کنید و نام دقیق روش را در گزارش بیاورید. در Graphs یک نمودار نقطه‌ای از هر سه ستون ایجاد کنید تا پراکندگی را هم ببینید.

## عددهای کنترل

در مدل کلاسیک F≈۱۰٫۶۶۴ و P≈۰٫۰۰۲۱۸ است. در Welch، F≈۹٫۲۶۶ و P≈۰٫۰۰۹۵۵ است. برای C−A اختلاف ۸٫۸ واحد و در Tukey مقدار P تعدیل‌شده حدود ۰٫۰۰۱۶۹ است.

<details>
<summary>فیلم و مرجع نوشتاری</summary>

- [فیلم آموزشی](https://www.graphpad.com/series/key-analysis-anova). بخش How to Perform a One-way ANOVA in Prism را باز کنید.
- [مرجع نوشتاری](https://graphpad.com/guides/prism/latest/statistics/stat_choosing_test_one-way_anova.htm).

</details>

[بازگشت به درس](../lessons/README.md) · [پاسخ‌ها](../solutions/module.md)

</div>
