# پاسخ‌های مسیر r

<a id="answer-1"></a>

## پاسخ 1

```r
uti <- read.csv("../data/M01_uti.csv")
dim(uti)
```
```
[1] 30 12
```
**جواب: ۳۰ سطر، ۱۲ ستون.**

<a id="answer-2"></a>

## پاسخ 2

```r
uti$sex       <- factor(uti$sex, 1:2, c("Female", "Male"))
uti$ward      <- factor(uti$ward, 1:3, c("Internal", "Surgery", "ICU"))
uti$organism  <- factor(uti$organism)
uti$cipro_res <- factor(uti$cipro_res, 0:1, c("Susceptible", "Resistant"))
uti$severity  <- factor(uti$severity, 1:3, c("Mild", "Moderate", "Severe"),
                        ordered = TRUE)
sapply(uti, function(x) class(x)[1])
```
```
       id       age       sex      ward  organism      temp       crp       wbc 
"integer" "integer"  "factor"  "factor"  "factor" "numeric" "numeric" "numeric" 
     pain  severity       los cipro_res 
"integer" "ordered" "integer"  "factor" 
```

- `1:3` کوتاه‌شدهٔ `c(1, 2, 3)` است؛ آرگومان دوم و سوم `factor()` به ترتیب `levels` و `labels` هستند.
- `organism` از قبل متن است، پس فقط `factor()` لازم دارد (سطوح به ترتیب الفبا).
- `sapply` تابع داده‌شده را روی تک‌تک ستون‌ها اجرا می‌کند.
- `pain` را با خواست قبلی عددی نگه داشتیم (درس ۱.۲، دام ۲)؛ اگر بخواهید ترتیبی‌اش کنید: `factor(uti$pain, 0:10, ordered = TRUE)`.

<a id="answer-3"></a>

## پاسخ 3

```r
mean(uti$crp)                          # پیش از تبدیل
uti$crp[uti$crp == -99] <- NA
sum(!is.na(uti$crp))                   # تعداد معتبر
round(mean(uti$crp, na.rm = TRUE), 2)  # پس از تبدیل
sum(is.na(uti$wbc))
```
```
[1] 35.1
[1] 28
[1] 44.68
[1] 1
```

- `is.na()` برای هر مقدار TRUE/FALSE می‌دهد؛ `!` آن را برعکس می‌کند؛ `sum()` تعداد TRUE ها را می‌شمارد.
- **جواب:** میانگین از **35.10** (غلط) به **44.68** (درست) رسید. CRP **۲۸** و WBC **۲۹** مقدار معتبر دارند (۳۰ − ۱).

<a id="answer-4"></a>

## پاسخ 4

```r
mean(as.integer(uti$ward))   # کد زیرین factor
table(uti$ward)
table(uti$organism)
```
```
[1] 1.8

Internal  Surgery      ICU 
      12       12        6 

   E. coli Klebsiella    Proteus 
        17          9          4 
```
۱٫۸ «بخش» واقعی‌ای نیست؛ کدها برچسب‌اند (درس ۱.۲). درصدها: `prop.table(table(uti$ward)) * 100` ← 40، 40، 20.

<a id="answer-5"></a>

## پاسخ 5

```r
table(uti$sex, uti$cipro_res)
```
```
         Susceptible Resistant
  Female          13         7
  Male             6         4
```
**جواب: ۷.**

<a id="answer-6"></a>

## پاسخ 6

```r
wide <- read.csv("../data/M01_crp_wide.csv")
long <- reshape(wide, direction = "long",
                varying = c("crp_d0", "crp_d3", "crp_d7"),
                v.names = "crp", timevar = "day", times = c(0, 3, 7),
                idvar = "id")
nrow(long)
```
```
[1] 24
```
**جواب: ۲۴ سطر** (۸ × ۳). با `tidyr`:
```r
library(tidyr)
long2 <- pivot_longer(wide, crp_d0:crp_d7, names_to = "day",
                      names_prefix = "crp_d", values_to = "crp")
```

<a id="answer-7"></a>

## پاسخ 7

```r
saveRDS(uti, "M01_uti_labeled.rds")
str(readRDS("M01_uti_labeled.rds"))
```
در خروجی `sex : Factor w/ 2 levels "Female","Male"` و `severity : Ord.factor ...` و `crp : num ... NA ...` دیده می‌شود. **بله، همه‌چیز مانده است.**

