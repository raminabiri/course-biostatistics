# M01 در SPSS — ورود داده، تعریف متغیرها، دادهٔ گمشده و تغییر ساختار

> **اگر از صفر آغاز می‌کنید، [نخستین جدول را اینجا بسازید](START.md).** این صفحه برای کارهای پس از آشنایی نخست است.

[← ماژول M01](../README.md) | [صفحهٔ مسیر SPSS](../../../tracks/spss.md)

**پیش‌نیاز:** درس‌های نظری [۱.۱ تا ۱.۴](../README.md). اگر SPSS را هنوز نصب نکرده‌اید، [صفحهٔ مسیر SPSS](../../../tracks/spss.md) را ببینید.
**فایل‌ها:** [`M01_walkthrough.sps`](M01_walkthrough.sps) (آموزش گام‌به‌گام) و [`M01_solutions.sps`](M01_solutions.sps) (حل تمرین‌ها).
**نسخه:** SPSS Statistics 27 به بعد.

---

## بخش آموزشی

### گام ۱ — وارد کردن فایل CSV (درس ۱.۱)

**روش منویی:**

1. `File > Import Data > CSV Data...`
2. فایل `data/M01_uti.csv` را انتخاب کنید.
3. در پنجرهٔ Read CSV File:
   - تیک **First line contains variable names** فعال باشد.
   - Delimiter between values: **Comma**؛ Decimal symbol: **Period**.
4. **OK** (یا **Paste** برای دیدن Syntax).

(در نسخه‌های قدیمی‌تر: `File > Open > Data`، نوع فایل CSV، و پیمودن مراحل Text Import Wizard.)

**نتیجه:** پنجرهٔ **Data View**: هر سطر یک بیمار (یک رکورد)، هر ستون یک متغیر. پایین پنجره را ببینید: دو زبانه دارد، **Data View** و **Variable View**.

**روش Syntax:** بخش «گام ۱» در `M01_walkthrough.sps`. فقط خط `CD` را به مسیر پوشهٔ `data` روی رایانهٔ خودتان تغییر دهید.

### گام ۲ — تعریف متغیرها در Variable View (درس ۱.۲)

زبانهٔ **Variable View** را باز کنید. هر **سطر** این جدول یک **متغیر** است و ستون‌هایش ویژگی‌های آن متغیرند. همین جدول، کدبوک داخل فایل SPSS است:

| ستون Variable View | کاربرد | نمونه برای `ward` |
|---|---|---|
| Name | نام کوتاه متغیر | `ward` |
| Type | نوع ذخیره: Numeric یا String | Numeric |
| Label | برچسب کامل (در خروجی‌ها نمایش داده می‌شود) | Hospital ward |
| **Values** | **برچسب مقدار**: معنای هر کد | 1 = Internal، 2 = Surgery، 3 = ICU |
| **Missing** | **کد گمشده** | None |
| **Measure** | **سطح اندازه‌گیری**: Nominal، Ordinal یا Scale | Nominal |

**تعریف برچسب مقدار (Values):**
1. در سطر `ward`، روی خانهٔ ستون **Values** کلیک و دکمهٔ `...` را بزنید.
2. Value: `1`، Label: `Internal` ← **Add**. همین را برای 2 و 3 تکرار کنید ← **OK**.
3. همین کار را برای `sex`، `severity` و `cipro_res` انجام دهید (کدبوک را ببینید).

**تعیین Measure:** روی خانهٔ ستون **Measure** هر متغیر کلیک و یکی از سه گزینه را انتخاب کنید:

| Measure | متغیرها |
|---|---|
| Nominal (🟢 سه دایرهٔ رنگی) | sex، ward، organism، cipro_res |
| Ordinal (📶 میله‌های پلکانی) | severity، pain |
| Scale (📏 خط‌کش) | age، temp، crp، wbc، los |

**نکته:** SPSS برای فاصله‌ای و نسبی فقط یک گزینه دارد: **Scale**.

**دیدن برچسب‌ها:** به Data View برگردید و `View > Value Labels` را بزنید (یا دکمهٔ برچسب در نوار ابزار). به‌جای 1 و 2 واژه‌های Female و Male را می‌بینید. داده تغییر نکرده؛ فقط نمایش عوض شده است.

### گام ۳ — تعریف کد گمشده (درس ۱.۴)

1. Variable View، سطر `crp`، ستون **Missing** ← `...`
2. **Discrete missing values** ← در خانهٔ اول `-99` ← **OK**.

حالا ‎-99 هنوز در Data View دیده می‌شود ولی در بسیاری از روش‌های آماری با تنظیم پیش‌فرض کنار گذاشته می‌شود؛ رفتار دستور و گزینهٔ MISSING را بررسی کنید (User-missing). خانهٔ خالی `wbc` (بیمار ۱۲) را SPSS خودش با نقطه (`.`) نشان می‌دهد (System-missing).

**بررسی:** `Analyze > Descriptive Statistics > Descriptives` ← `crp` و `wbc` را به لیست Variable(s) ببرید ← **OK**. ستون **N** باید ۲۸ و ۲۹ باشد.

### گام ۴ — کد عددی ≠ عدد (درس ۱.۲)

1. `Analyze > Descriptive Statistics > Descriptives` ← `ward` ← OK. میانگین = **1.80**. SPSS بدون اعتراض حساب می‌کند؛ تشخیص بی‌معنا بودن آن با شماست.
2. `Analyze > Descriptive Statistics > Frequencies` ← `ward` و `severity` ← OK. این خلاصهٔ درست است.

### گام ۵ — ذخیره

`File > Save As` ← نوع **SPSS Statistics (*.sav)** ← نام `M01_uti_labeled.sav`. فایل `.sav` همهٔ برچسب‌ها، کدهای گمشده و سطح‌های اندازه‌گیری را نگه می‌دارد؛ CSV هیچ‌کدام را نگه نمی‌دارد.

### گام ۶ — تبدیل قالب پهن به بلند (درس ۱.۳)

1. فایل `data/M01_crp_wide.csv` را مثل گام ۱ باز کنید (۸ سطر، ۴ ستون).
2. `Data > Restructure...` ← **Restructure selected variables into cases** ← Next.
3. Number of Variable Groups: **One** ← Next.
4. Case Group Identification: **Use selected variable** ← `id`.
   Variables to be Transposed: Target Variable را `crp` بنامید و `crp_d0`، `crp_d3`، `crp_d7` را (به همین ترتیب) به آن ببرید ← Next.
5. Number of Index Variables: **One** ← Next ← Index type: **Sequential numbers**، نام Index را `visit` بگذارید ← **Finish**.
6. حالا ۲۴ سطر دارید. برای تبدیل `visit` (1، 2، 3) به روز واقعی (0، 3، 7):
   `Transform > Recode into Different Variables` ← `visit` ← Output Variable Name: `day` ← Change ← **Old and New Values**: 1→0، 2→3، 3→7 ← Continue ← OK.

معادل Syntax: دستور `VARSTOCASES` در گام ۶ فایل walkthrough.

---

## تمرین‌های عملی (ع۱ تا ع۷)

این تمرین‌ها در هر پنج مسیر نرم‌افزاری **یکسان‌اند**. اول با منوها حل کنید، بعد با Syntax.

| شماره | تمرین |
|---|---|
| ع۱ | `M01_uti.csv` را وارد کنید. داده چند سطر و چند ستون دارد؟ |
| ع۲ | برای `sex`، `ward`، `severity`، `cipro_res` برچسب مقدار بگذارید و Measure همهٔ متغیرها را طبق تمرین ۱.۲.۲ تنظیم کنید. |
| ع۳ | میانگین CRP را **پیش** و **پس** از تعریف ‎-99 به‌عنوان گمشده حساب کنید. پس از تعریف، CRP و WBC هر کدام چند مقدار معتبر دارند؟ |
| ع۴ | میانگین کد `ward` را حساب کنید و توضیح دهید چرا بی‌معناست. سپس جدول فراوانی `ward` و `organism` را بسازید. |
| ع۵ | چند بیمار **زن** به سیپروفلوکساسین **مقاوم** بودند؟ (راهنما: جدول توافقی) |
| ع۶ | `M01_crp_wide.csv` را به قالب بلند تبدیل کنید. چند سطر به دست می‌آید؟ |
| ع۷ | دادهٔ برچسب‌دار را ذخیره کنید، فایل را ببندید و دوباره باز کنید. آیا برچسب‌ها مانده‌اند؟ |

### حل تمرین‌ها

[پاسخ 1](../solutions/spss-P01.md)

[پاسخ 2](../solutions/spss-P02.md)

[پاسخ 3](../solutions/spss-P03.md)

[پاسخ 4](../solutions/spss-P04.md)

[پاسخ 5](../solutions/spss-P05.md)

[پاسخ 6](../solutions/spss-P06.md)

[پاسخ 7](../solutions/spss-P07.md)

---

## خطاهای جاری در SPSS

| مشکل | علت | راه‌حل |
|---|---|---|
| حروف فارسی در خروجی به شکل `???` | SPSS در حالت Locale است | `Edit > Options > Language` ← Unicode (هیچ فایلی نباید باز باشد) |
| ستون عددی با Type = String وارد شده | یک خانه حاوی متن یا علامت (برای نمونه `؟` یا `<5`) بوده | فایل منبع را درست کردن کنید یا `Transform > Automatic Recode` / تغییر Type |
| کد گمشده اثری ندارد | Missing تعریف نشده یا در متغیر اشتباه تعریف شده | Variable View ← Missing |
| خطای Syntax «file not found» | مسیر `CD` اشتباه است | مسیر کامل پوشهٔ `data` را بنویسید |
