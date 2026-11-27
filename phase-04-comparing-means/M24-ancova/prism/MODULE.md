<div dir="rtl">

# M24 در GraphPad Prism

[practice.csv](../data/practice.csv) ۲۴ مشاهده دارد. برای مرحلهٔ نخست فقط ۱۲ ردیف b=0 را بگیرید. x خط پایه منهای ۲۴ است. در تحلیل سوم، [جدول change.csv](../data/change.csv) را جدا باز کنید و ستون change را پاسخ بگذارید.

## دیدن مدل در نمودار XY

۱. در File → New Project نوع XY را بگیرید. از فایل نخست ردیف‌های b=0 را جدا کنید. در X مقدار x=baseline−24 و در دو مجموعهٔ Y مقدارهای A0 و A1 را بگذارید. اگر برای یک X در هر دو گروه مشاهده دارید، هر Y را در ستون گروه خودش بنویسید. برای خانه‌ای که در آن گروه مشاهده ندارید، خانه را خالی بگذارید.

۲. از Analyze → Simple Linear Regression، گزینهٔ Test whether slopes and intercepts are significantly different را فعال کنید. در برگهٔ Are lines different? آزمون تغییر شیب را بخوانید. x صفر خط پایهٔ ۲۴ است. برای گرفتن پیش‌بینی با شیب مشترک، مدل رگرسیون چندمتغیرهٔ گام بعد را به کار ببرید.

## برآورد عددی با Multiple Variables

۳. در پروژهٔ تازه نوع جدول Multiple Variables را باز کنید. برای هر مشاهده یک سطر و ستون‌های value، a و x را وارد کنید. از Analyze → Multiple linear regression، value را پاسخ و a و x را پیش‌بین بگذارید. با کد عددی صفر و یک برای a، پیش‌بینی A1 در x=0 برابر جمع Intercept و ضریب a و پیش‌بینی A0 همان Intercept است. فاصلهٔ اطمینان ضریب a را در جدول برآوردها بخوانید.

۴. برای طرح دو عاملی، از برگهٔ All [کاربرگ آماده](../excel/M24_module.xlsx) ستون‌های value، a، b، x و a×b را به جدول Multiple Variables ببرید. مدل را از این چهار پیش‌بین بسازید. آزمون t ضریب a×b و فاصلهٔ آن در جدول پارامترهاست. مربع همین t آزمون F با یک درجهٔ آزادی صورت است. برای مقایسهٔ شیب‌ها، سه ستون a×x، b×x و a×b×x را در مدل دوم اضافه کنید. با SS مانده‌ها و df از دو مدل، F درس را بسازید.

۵. برای change.csv، پاسخ change را جای value بگذارید و a و x را پیش‌بین کنید. ضریب a و فاصلهٔ آن را بخوانید. اگر نسخهٔ شما جدول Multiple Variables ندارد، بررسی تصویری و آزمون دو شیب با XY انجام می‌شود و مقدارهای کامل رگرسیون در R، Python یا کاربرگ قابل بازتولیدند.

## کنترل نتیجه

در B0، پایان تعدیل‌شده برای A0 و A1 برابر ۴۸٫۹۴۳ و ۵۱٫۲۸۶ و فاصلهٔ ۹۵٪ اختلاف ۰٫۶۷۲ تا ۴٫۰۱۴ است. در همهٔ ردیف‌ها، F تعامل A×B≈۱٫۰۵۲ و P≈۰٫۳۱۸ هستند. برای تغییر، اختلاف ۱٫۴۴۳، بازهٔ ۹۵٪ از −۰٫۶۷۶ تا ۳٫۵۶۲ و P≈۰٫۱۵۷۸ است.

<details>
<summary>فیلم و مرجع نوشتاری</summary>

- [فیلم آموزشی](https://www.graphpad.com/series/how-to-perform-linear-regression-analysis). متوسط. پس از شناخت جدول XY، ساخت خط رگرسیون را ببینید. برای تعدیل و اختلاف در ۲۴، بخش رگرسیون چندمتغیرهٔ متن را انجام دهید.
- [مرجع نوشتاری](https://www.graphpad.com/guides/prism/latest/curve-fitting/reg_comparingslopesandintercepts.htm).
- [مجموعهٔ آموزش رگرسیون چندمتغیرهٔ ناشر](https://www.graphpad.com/series/data-analysis). بخش Multiple linear regression را برای خواندن ضریب و جدول ANOVA ببینید.

</details>

[بازگشت به درس](../lessons/README.md) · [پاسخ‌ها](../solutions/module.md)

</div>
