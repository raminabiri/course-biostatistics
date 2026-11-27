<div dir="rtl">

# M24 در SPSS

[practice.csv](../data/practice.csv) ۲۴ مشاهده دارد. برای مرحلهٔ نخست فقط ۱۲ ردیف b=0 را بگیرید. x خط پایه منهای ۲۴ است. در تحلیل سوم، [جدول change.csv](../data/change.csv) را جدا باز کنید و ستون change را پاسخ بگذارید.

## مدل در B0 و برآورد در خط پایهٔ ۲۴

۱. از File → Import Data → CSV Data داده را با نام ستون در سطر اول و جداکنندهٔ Comma وارد کنید. در Variable View، a و b مقدار عددی و نقش Nominal دارند. baseline و value سنجهٔ عددی‌اند. از Transform → Compute Variable، متغیر x را با عبارت baseline−24 بسازید. در Data → Select Cases، b=0 را برای مدل نخست بگذارید.

۲. از Analyze → General Linear Model → Univariate، value را به Dependent Variable، a را به Fixed Factor و x را به Covariate ببرید. در Custom Model، اثرهای a و x را وارد کنید. در GUI ممکن است میانگین تعدیل‌شده به طور پیش‌فرض در میانگین x باشد. برای درخواست خط پایهٔ دقیق ۲۴، [فایل Syntax](M24_module.sps) گزینهٔ `EMMEANS=TABLES(a) WITH(x=0) COMPARE(a)` را دارد. در جدول Estimates پیش‌بینی‌ها و در Pairwise Comparisons جهت تفاضل و بازه را بخوانید.

## مدل‌های چندعاملی و تغییر

در فایل Syntax، `TEMPORARY` سبب می‌شود شرط b=0 فقط سر تحلیل بعدی برقرار باشد. گزینهٔ `DESIGN` در مدل مشترک a، b، a*b و x دارد. Tests of Between-Subjects Effects و ردیف a*b آزمون نخست را می‌دهد. برای بررسی شیب‌ها، مدل توسعه‌یافتهٔ همان فایل a*x، b*x و a*b*x را اضافه می‌کند. برای آزمون مشترک سه جمله، مجموع مربعات Error دو مدل را همراه اختلاف سه درجهٔ آزادی مطابق فرمول درس مقایسه کنید.

برای تحلیل تغییر، فایل change.csv وارد و همان x ساخته می‌شود. در تحلیل Univariate، change پاسخ، a عامل و x هم‌متغیر است. در خطِ `COMPARE(a)` گزینهٔ مقایسهٔ دو پیش‌بینی فعال می‌شود. در صورت نیاز مسیرهای FILE را کامل و Run → All را اجرا کنید. [نسخهٔ رگرسیون برای PSPP](M24_pspp.sps) آزمون‌های همان مدل‌های خطی را با ستون‌های عددیِ کدگذاری‌شده بازتولید می‌کند.

## کنترل نتیجه

در B0، پایان تعدیل‌شده برای A0 و A1 برابر ۴۸٫۹۴۳ و ۵۱٫۲۸۶ و فاصلهٔ ۹۵٪ اختلاف ۰٫۶۷۲ تا ۴٫۰۱۴ است. در همهٔ ردیف‌ها، F تعامل A×B≈۱٫۰۵۲ و P≈۰٫۳۱۸ هستند. برای تغییر، اختلاف ۱٫۴۴۳، بازهٔ ۹۵٪ از −۰٫۶۷۶ تا ۳٫۵۶۲ و P≈۰٫۱۵۷۸ است.

<details>
<summary>فیلم و مرجع نوشتاری</summary>

- [فیلم آموزشی](https://www.youtube.com/watch?v=ZYBpVgAFa24). متوسط. در فیلم بررسی رابطهٔ خطی و شیب‌ها از ۶:۰۵ معرفی می‌شود. در کارگاه خط پایه را صریح روی ۲۴ می‌گذاریم.
- [مرجع نوشتاری](https://www.ibm.com/docs/en/spss-statistics/32.0.0?topic=unianova-emmeans-subcommand-command).

</details>

[بازگشت به درس](../lessons/README.md) · [پاسخ‌ها](../solutions/module.md)

</div>
