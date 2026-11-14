# روش کار پنج نرم‌افزار، به تفکیک درس

[بازگشت به ماژول](README.md)

**مخاطب:** همهٔ گروه‌ها. **سطح:** مقدماتی برای ورود داده؛ متوسط برای ساخت نوع و تبدیل؛ پیشرفته برای کنترل بازسازی و کلید. منوها انگلیسی‌اند. مسیرهای منویی باید روی نسخهٔ نصب‌شدهٔ کاربر بازبینی شوند؛ اجرای SPSS و Prism در این محیط انجام نشده است.

دو مجموعه داریم: نمونهٔ کوچک `M01_uti.csv` با ۳۰ بیمار برای شروع، و بانک بزرگ `M01_training_bank.xlsx` برای تمرین. کدهای زیر روی نمونهٔ کوچک‌اند. در بانک بزرگ نام شناسه `patient_id` است. نام ستون‌ها را پیش از انتقال کد بررسی کنید.

<a id="l1"></a>
## درس ۱ — خواندن داده و شناخت واحد

### SPSS

۱. `File > Import Data > CSV Data` را باز کنید و `data/M01_uti.csv` را برگزینید. اگر مسیر منو در نسخهٔ شما فرق دارد، از پنجرهٔ Open Data و نوع فایل CSV وارد شوید.
۲. سطر نخست را نام ستون‌ها و جداکننده را comma بگذارید. در پیش‌نمایش، هر بیمار باید یک سطر باشد.
۳. در `Data View` شمار سطرها و در `Variable View` شمار متغیرها را ببینید: ۳۰ سطر و ۱۲ ستون.
۴. برای اجرای تکرارپذیر، [Syntax کامل](spss/M01_walkthrough.sps) را باز کنید، خط `CD` را به پوشهٔ data روی رایانهٔ خود تغییر دهید و `Run > All` را بزنید. خروجی‌های SAV در همان پوشه ساخته می‌شوند.

```spss
DISPLAY DICTIONARY.
FREQUENCIES VARIABLES=id /FORMAT=NOTABLE.
```

فراوانی id به‌تنهایی آزمون استقلال نیست؛ یکتایی شناسه را همراه طرح پژوهش بررسی کنید.

### Excel

۱. از `Data > From Text/CSV` فایل کوچک را بخوانید؛ پیش از Load، نوع شناسه و جداکننده را ببینید.
۲. محدوده را با `Insert > Table` به Table تبدیل کنید و نام آن را در `Table Design` برابر `UTI` بگذارید.
۳. در سلول‌های بیرون Table بنویسید:

```excel
=ROWS(UTI[id])
=COLUMNS(UTI[#Headers])
```

پاسخ ۳۰ و ۱۲ است. برای بانک بزرگ، فایل آماده را باز کنید؛ نام Tableهای آن `Patients`، `Followup` و `Laboratory` است. فیلتر کردن با حذف سطر یکی نیست؛ `ROWS` شمار همهٔ سطرهای Table را می‌دهد.

### GraphPad Prism

Prism را برای خواندن مقدارهای یک کمیت و رسم نمودار به کار ببرید؛ نقش آن با پروندهٔ چندستونی بیمار یکسان نیست. `New Table & Graph > Column` را باز کنید، یک ستون CRP بسازید و شناسه‌ها را در `Row titles` نگه دارید. برای نمونهٔ کوچک، پیش از چسباندن داده، دو کد ‎-99 را به خانهٔ خالی تبدیل کنید. شمار ردیف داده برابر ۳۰ و شمار مقدار پر برابر ۲۸ است. شناسه را به‌عنوان سیگنال عددی تحلیل نکنید. مراحل بیشتر در [مسیر Prism](prism/README.md) آمده است.

### R

از پوشهٔ `r/` اجرا کنید:

```r
d <- read.csv("../data/M01_uti.csv")
dim(d)                    # 30 12
length(unique(d$id))      # 30
anyDuplicated(d$id)       # 0: no duplicate ID
```

`dim` دو عدد سطر و ستون را می‌دهد. `unique` شناسه‌های بی‌تکرار را نگه می‌دارد. یکتایی شناسه شرط لازم ساختار این جدول است و استقلال بیماران را ثابت نمی‌کند.

### Python

از پوشهٔ `python/` اجرا کنید:

```python
import pandas as pd
d = pd.read_csv("../data/M01_uti.csv")
print(d.shape)                 # (30, 12)
print(d["id"].nunique())        # 30
print(d["id"].duplicated().sum()) # 0
```

`shape` اندازهٔ جدول است؛ `nunique` خانه‌های خالی را در شمار شناسه‌های یکتا نمی‌آورد. خالی‌بودن شناسه را جدا با `isna` بررسی کنید.

<a id="l2"></a>
## درس ۲ — نوع ستون و مقیاس

### SPSS

در `Variable View`، ستون‌های `Name`، `Label`، `Values`، `Missing` و `Measure` را مرور کنید. `sex` و `ward` را Nominal، `severity` و `pain` را Ordinal، و سن و CRP را Scale بگذارید. Scale در SPSS فاصله‌ای و نسبی را جدا نمی‌کند؛ این تفاوت در فرهنگ داده نوشته شود.

```spss
VALUE LABELS severity 1 'Mild' 2 'Moderate' 3 'Severe'.
VARIABLE LEVEL sex ward organism cipro_res (NOMINAL)
 /severity pain (ORDINAL)
 /age temp crp wbc los (SCALE).
FREQUENCIES VARIABLES=ward severity.
```

تغییر Measure مقدارها را دگرگون نمی‌کند و جلوی همهٔ تحلیل‌های نامناسب را نمی‌گیرد.

### Excel

در برگه‌ای به نام Codebook، نام ستون، واحد، نوع، رده‌ها و معنای گمشده را بنویسید. برای severity از `Data > Data Validation > List` و فهرست `1,2,3` کمک بگیرید؛ این روش خطای ورود را کمتر می‌کند ولی ترتیب آماری را در فایل CSV نگه نمی‌دارد.

```excel
=COUNTIF(UTI[ward],1)
=COUNTIF(UTI[severity],3)
```

عدد نخست ۱۲ است. کد ۳ شدت شدید است و نباید به معنی سه برابر شدت خفیف خوانده شود. `Format Cells > Number` تنها نمایش عدد را تغییر می‌دهد؛ مقیاس آماری را تعیین نمی‌کند.

### GraphPad Prism

رده‌های شدت را به صورت عنوان گروه ثبت کنید؛ برای هر گروه ستون CRP جدا بسازید، به شرط نگه‌داشتن پیوند با شناسهٔ اصلی. ترتیب Mild، Moderate، Severe را خودتان نگه دارید. Prism فرهنگ متغیر و نوع ترتیبی مشابه factor در R ندارد؛ کدهای ۱ تا ۳ را برای میانگین شدت وارد تحلیل نکنید. فایل اصلی با همهٔ ستون‌ها در Excel یا CSV بماند.

### R

```r
d$ward <- factor(d$ward, levels=c(1,2,3),
                 labels=c("Internal","Surgery","ICU"))
d$severity <- factor(d$severity, levels=c(1,2,3),
                     labels=c("Mild","Moderate","Severe"), ordered=TRUE)
table(d$ward, useNA="ifany")
levels(d$severity)
is.ordered(d$severity)
```

`levels` کد و ترتیب را روشن می‌کند؛ کدی بیرون فهرست به NA تبدیل می‌شود، پس پیش و پس از تبدیل شمار رده‌ها را کنترل کنید.

### Python

```python
d["ward"] = pd.Categorical(d["ward"], categories=[1, 2, 3])
d["severity"] = pd.Categorical(d["severity"], categories=[1, 2, 3], ordered=True)
print(d["severity"].cat.ordered)  # True
print(d["ward"].value_counts(sort=False, dropna=False))
```

`ordered=True` ترتیب را ثبت می‌کند. این کد فقط نمونهٔ کوچک را پوشش می‌دهد؛ در بانک نیز دامنهٔ کدها را پیش از تبدیل بسنجید. متن‌شدن ستون معادل تعریف نوع ترتیبی نیست.

<a id="l3"></a>
## درس ۳ — پهن و بلند

### SPSS

فایل `M01_crp_wide.csv` را با چهار ستون `id`، `crp_d0`، `crp_d3` و `crp_d7` وارد کنید. مسیر منویی `Data > Restructure` است؛ تبدیل چند ستون به یک ستون و نگه‌داشتن id را برگزینید. Syntax روشن‌تر است:

```spss
VARSTOCASES /MAKE crp FROM crp_d0 crp_d3 crp_d7
 /INDEX=visit(3) /KEEP=id /NULL=KEEP.
RECODE visit (1=0) (2=3) (3=7) INTO day.
EXECUTE.
```

۸ فرد و ۲۴ سطر داریم؛ روزهای ۰،۳،۷ را با کد نوبت ۱،۲،۳ یکی نگیرید. `/NULL=KEEP` سطر سنجش خالی را نگه می‌دارد.

### Excel

۱. فایل پهن را به Table تبدیل کنید.
۲. `Data > From Table/Range` را باز کنید.
۳. id را برگزینید و در Power Query، `Transform > Unpivot Other Columns` را بزنید.
۴. Attribute را day و Value را crp بنامید؛ بخش `crp_d` را از day بردارید و نوع day را Whole Number بگذارید.
۵. `Close & Load` و سپس شمار سطرها را کنترل کنید: ۲۴.

Power Query در تبدیل، خانه‌های null را کنار می‌گذارد؛ اگر سنجش خالی دارید، برنامهٔ همهٔ نوبت‌ها را جدا نگه دارید و با Left Join به خروجی پیوند دهید. بانک بزرگ از آغاز جدول بلند با سطرهای خالی نگه‌داشته‌شده دارد.

### GraphPad Prism

برای نمایش روند، `New Table & Graph > XY` را بسازید؛ X برابر ۰،۳،۷ و هر بیمار یک Data set جدا باشد. مقدارها را از فایل پهن با جابه‌جایی جهت جدول منتقل کنید. شناسهٔ بیمار را در عنوان مجموعه نگه دارید. این آرایش نمایشی جای جدول بلند پژوهش را نمی‌گیرد. برای تبدیل ساختاری، مسیر Excel، R یا Python را دنبال کنید.

### R

```r
w <- read.csv("../data/M01_crp_wide.csv")
l <- reshape(w, direction="long", varying=c("crp_d0","crp_d3","crp_d7"),
             v.names="crp", timevar="day", times=c(0,3,7), idvar="id")
l <- l[order(l$id, l$day), ]
stopifnot(nrow(l)==24, !anyDuplicated(l[c("id","day")]))
```

`idvar` فرد و `times` زمان واقعی را معرفی می‌کند. پیش از تبدیل، id در جدول پهن باید یکتا باشد.

### Python

```python
w = pd.read_csv("../data/M01_crp_wide.csv")
l = w.melt(id_vars="id", var_name="day", value_name="crp")
l["day"] = l["day"].str.replace("crp_d", "", regex=False).astype(int)
assert l.shape == (24, 3)
assert not l.duplicated(["id", "day"]).any()
back = l.pivot(index="id", columns="day", values="crp")
```

`melt` خانه‌های خالی را هم نگه می‌دارد. `pivot` برای کلید تکراری خطا می‌دهد؛ آن را با میانگین‌گیری بی‌دلیل پنهان نکنید.

<a id="l4"></a>
## درس ۴ — گمشدگی و کنترل سنجش

### SPSS

روی فایل UTI کار کنید. در `Variable View > Missing` کد CRP را ‎-99 تعریف کنید؛ خانهٔ خالی WBC گمشدهٔ سیستمی است.

```spss
MISSING VALUES crp (-99).
FREQUENCIES VARIABLES=crp wbc /FORMAT=NOTABLE
 /STATISTICS=MEAN MINIMUM MAXIMUM.
```

CRP دارای ۲ گمشده و ۲۸ مقدار معتبر، WBC دارای ۱ گمشده و ۲۹ مقدار معتبر است. تعریف گمشده کد خام را پاک نمی‌کند.

### Excel

ستون تازه‌ای با نام crp_clean به UTI بیفزایید. ستون خام را نگه دارید.

```excel
=IF([@crp]=-99,"",[@crp])
=COUNT(UTI[crp_clean])
=COUNTBLANK(UTI[crp_clean])
=AVERAGE(UTI[crp_clean])
```

پاسخ‌ها ۲۸، ۲ و نزدیک به ۴۴٫۶۸ است. رشتهٔ خالی فرمول خانهٔ پاک‌شدهٔ واقعی نیست، ولی COUNTBLANK آن را می‌شمارد و AVERAGE متن را کنار می‌گذارد. برای خروجی CSV رفتار خانه‌ها را پس از بازخوانی بررسی کنید. جداکنندهٔ تابع در برخی تنظیم‌های منطقه‌ای `;` است.

### GraphPad Prism

برای گمشده خانه را خالی بگذارید؛ صفر یا ‎-99 را به‌جای آن وارد نکنید. ستون CRP پاک‌شده را وارد جدول Column کنید؛ در `Analyze > Column statistics` شمار مقدارها و میانگین را ببینید. شمار مقدارها باید ۲۸ باشد. [راهنمای رسمی گمشده در Prism](https://www.graphpad.com/guides/prism/latest/user-guide/missing_values.htm) همین رفتار خانهٔ خالی را توضیح می‌دهد. شمارش گمشده را با ۳۰ فرد فایل مادر بسنجید؛ نمودار به‌تنهایی شمار افراد کنارگذاشته‌شده را نشان نمی‌دهد.

### R

```r
d <- read.csv("../data/M01_uti.csv")
raw_mean <- mean(d$crp)
d$crp[d$crp == -99] <- NA
c(raw_mean=raw_mean, valid=sum(!is.na(d$crp)), missing=sum(is.na(d$crp)),
  clean_mean=mean(d$crp, na.rm=TRUE))
```

میانگین خام ۳۵٫۱ و میانگین پاک‌شده ۴۴٫۶۷۸۵۷ است. `na.rm=TRUE` خانهٔ گمشده را از محاسبه کنار می‌گذارد؛ این گزینه راه درمان سوگیری گمشدگی نیست.

### Python

```python
d = pd.read_csv("../data/M01_uti.csv")
raw_mean = d["crp"].mean()
d["crp"] = d["crp"].mask(d["crp"].eq(-99))
print(raw_mean, d["crp"].count(), d["crp"].isna().sum(), d["crp"].mean())
```

میانگین در pandas به‌طور پیش‌فرض گمشده‌ها را کنار می‌گذارد؛ شمار معتبر و گمشده را خودتان بنویسید. نوع نشانهٔ گمشده با نوع ستون فرق دارد؛ NA، NaN و NaT همه در یک نقش و نوع نیستند.

## بررسی پیش از تحویل

[روش کار بانک در Python](python/M01_bank_check.py) و [روش کار بانک در R](r/M01_bank_check.R) شمارها، کلیدها و گمشدگی را کنترل می‌کنند. فایل‌های قدیمی walkthrough و solutions روی نمونهٔ کوچک باقی مانده‌اند. در گزارش هر مسیر، نسخهٔ نرم‌افزار، دادهٔ ورودی، شمار سطر و شمار مقدار معتبر را بنویسید.
