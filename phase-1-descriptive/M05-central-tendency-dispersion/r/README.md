<div dir="rtl">

# M05 در R — آمار توصیفی پایه

[← ماژول M05](../README.md) | [صفحهٔ مسیر R](../../../tracks/r.md)

**فایل:** [`M05_solutions.R`](M05_solutions.R) (با R 4.6 اجرا و کنترل شده). فقط R پایه.

## بخش آموزشی

| شاخص | تابع R | نکته |
|---|---|---|
| میانگین / میانه | `mean(x)` / `median(x)` | با گمشده: `na.rm = TRUE` |
| نما | `table(x)` و `names(which.max(table(x)))` | تابع آماده ندارد (`mode()` در R چیز دیگری است!) |
| SD / واریانس | `sd(x)` / `var(x)` | تقسیم بر n − 1 |
| کمینه، بیشینه، دامنه | `min`، `max`، `range(x)`، `diff(range(x))` | `range()` دو عدد می‌دهد، نه دامنه |
| چارک‌ها | `quantile(x, c(.25,.75))` | پیش‌فرض **type = 7**؛ برای روش SPSS/Prism: `type = 6` |
| IQR | `IQR(x)` | با type 7 |
| SEM | `sd(x) / sqrt(length(x))` | تابع آماده ندارد |
| همه با هم | `summary(x)` | کمینه، چارک‌ها (type 7)، میانه، میانگین، بیشینه |
| به تفکیک گروه | `aggregate(y ~ g, data, FUN)` یا `tapply(y, g, FUN)` | |

### یک تابع کمکی برای جدول

```r
desc <- function(x) c(n = sum(!is.na(x)), mean = mean(x, na.rm = TRUE),
                      sd = sd(x, na.rm = TRUE), median = median(x, na.rm = TRUE))
round(sapply(d[, c("sbp", "ldl", "hdl")], desc), 2)
```

## تمرین‌های عملی (ع۱ تا ع۷)

این تمرین‌ها در هر پنج مسیر **یکسان‌اند**. داده: `data/M05_lipid.csv`.

| شماره | سطح | تمرین | درس |
|---|---|---|---|
| ع۱ | ۱ | میانگین و میانهٔ `sbp`، `ldl` و `hscrp`؛ نمای `cigs`. | ۵.۱ |
| ع۲ | ۱ | SD، واریانس، کمینه، بیشینه و دامنهٔ `sbp` و `ldl`. | ۵.۲ |
| ع۳ | ۱ | ضریب تغییرات (CV) `sbp`، `ldl` و `hscrp`. کدام نسبتاً پراکنده‌تر است؟ | ۵.۲ |
| ع۴ | ۲ | SEM برای `ldl` و `sbp`. برای `ldl` دو بازه بسازید: میانگین ± ۲SD و میانگین ± ۲SEM. هر کدام دربارهٔ چه چیزی است؟ | ۵.۳ |
| ع۵ | ۲ | به تفکیک جنس: n، میانگین و SD برای `sbp`، `ldl`، `hdl`. | ۵.۴ |
| ع۶ | ۲ | برای `hscrp`: میانگین، میانه، میانگین هندسی، و چارک اول و سوم. نرم‌افزار شما چارک را با کدام روش حساب می‌کند؟ | ۵.۴ |
| ع۷ | ۳ | `cigs`: تعداد و درصد سیگاری‌ها (> ۰)؛ میانه و میانگین مصرف **در سیگاری‌ها**. یک جملهٔ گزارش بنویسید. | ۵.۱ |

<details>
<summary><b>جواب‌های نهایی (فقط برای کنترل، پس از حل)</b></summary>

| | جواب |
|---|---|
| ع۱ | sbp: **130.19** / **130.00**؛ ldl: **131.08** / **136.50**؛ hscrp: **3.11** / **1.75**؛ نمای cigs: **0** |
| ع۲ | sbp: SD **11.32**، واریانس **128.11**، **99** تا **155** (دامنه **56**)؛ ldl: SD **31.85**، واریانس **1014.42**، **57** تا **202** (دامنه **145**) |
| ع۳ | sbp **8.7٪**، ldl **24.3٪**، hscrp **143.9٪** ← hsCRP بسیار پراکنده‌تر |
| ع۴ | SEM: ldl **4.60**، sbp **1.63**؛ ldl ± 2SD: **67.4 تا 194.8** (افراد)؛ ldl ± 2SEM: **121.9 تا 140.3** (میانگین) |
| ع۵ | زنان (n = **16**): sbp **127.94** (9.28)، ldl **140.75** (30.29)، hdl **57.44** (10.81)؛ مردان (n = **32**): sbp **131.31** (12.19)، ldl **126.25** (31.96)، hdl **45.84** (8.98) |
| ع۶ | میانگین **3.11**، میانه **1.75**، هندسی **1.85**؛ Q1 = **1.00**؛ Q3 = **3.375** (SPSS، Prism، Excel `QUARTILE.EXC`) یا **3.325** (پیش‌فرض R و Python، Excel `QUARTILE.INC`) |
| ع۷ | **15** سیگاری (**31.3٪**)؛ در سیگاری‌ها میانه **15** و میانگین **16** نخ در روز ← «۱۵ بیمار (۳۱٫۳٪) سیگاری بودند و میانهٔ مصرف آن‌ها ۱۵ نخ در روز بود.» |

</details>

### حل تمرین‌ها

کد کامل: [`M05_solutions.R`](M05_solutions.R).

<details>
<summary><b>حل ع۱ تا ع۳</b></summary>

```r
d <- read.csv("../data/M05_lipid.csv")
sapply(d[, c("sbp", "ldl", "hscrp")], mean)
sapply(d[, c("sbp", "ldl", "hscrp")], median)
names(which.max(table(d$cigs)))                    # "0"
sd(d$sbp); var(d$sbp); range(d$sbp); diff(range(d$sbp))
cv <- function(x) 100 * sd(x) / mean(x)
round(sapply(d[, c("sbp", "ldl", "hscrp")], cv), 1)
```

</details>

<details>
<summary><b>حل ع۴</b></summary>

```r
sem <- function(x) sd(x) / sqrt(length(x))
sem(d$ldl)                                         # 4.60
mean(d$ldl) + c(-2, 2) * sd(d$ldl)                 # 67.4 194.8
mean(d$ldl) + c(-2, 2) * sem(d$ldl)                # 121.9 140.3
```
اولی بازهٔ تقریبی ۹۵٪ **بیماران** است؛ دومی بازهٔ تقریبی ۹۵٪ برای **میانگین** جامعه (درس ۵.۳).

</details>

<details>
<summary><b>حل ع۵</b></summary>

```r
aggregate(cbind(sbp, ldl, hdl) ~ sex, data = d,
          FUN = function(x) c(n = length(x), mean = mean(x), sd = sd(x)))
```

</details>

<details>
<summary><b>حل ع۶</b></summary>

```r
x <- d$hscrp
mean(x); median(x); exp(mean(log(x)))              # 3.11 1.75 1.85
quantile(x, c(.25, .75))                           # 1.000 3.325 (type 7)
quantile(x, c(.25, .75), type = 6)                 # 1.000 3.375 (مثل SPSS/Prism)
```

</details>

<details>
<summary><b>حل ع۷</b></summary>

```r
smk <- d$cigs[d$cigs > 0]
length(smk); 100 * mean(d$cigs > 0)                # 15, 31.25
median(smk); mean(smk)                             # 15, 16
```

</details>

## خطاهای رایج

| مشکل | علت | راه‌حل |
|---|---|---|
| `mean()` جواب `NA` داد | گمشده | `na.rm = TRUE` |
| `mode(x)` جواب «numeric» داد | `mode()` نوع داده را می‌گوید، نه نما | `table()` |
| چارک‌ها با SPSS فرق دارد | روش متفاوت | `type = 6` (M06) |
| `round(31.25, 1)` جواب 31.2 داد | گرد کردن نمایش اعداد اعشاری مرزی | در گزارش 31.3 بنویسید |

## درس‌های عملی جداگانه

- [1 — مرکز داده](L01.md)
- [2 — پراکندگی](L02.md)
- [3 — SD در برابر SE](L03.md)
- [4 — انتخاب خلاصه و گزارش](L04.md)

</div>
