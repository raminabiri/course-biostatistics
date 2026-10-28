# M05 در SPSS — Frequencies، Descriptives، Means و Explore

[← ماژول M05](../README.md) | [صفحهٔ مسیر SPSS](../../../tracks/spss.md)

**فایل:** [`M05_solutions.sps`](M05_solutions.sps). خط `CD` را تغییر دهید.

## بخش آموزشی

SPSS چهار پنجرهٔ اصلی برای آمار توصیفی دارد:

| منو | چه می‌دهد؟ | کی؟ |
|---|---|---|
| `Analyze > Descriptive Statistics > Frequencies` ← **Statistics** | میانگین، میانه، نما، SD، واریانس، دامنه، SEM، چارک‌ها؛ (تیک **Display frequency tables** را برای متغیرهای کمّی بردارید) | بهترین برای یک متغیر و همهٔ شاخص‌ها |
| `Analyze > Descriptive Statistics > Descriptives` ← **Options** | میانگین، SD، کمینه، بیشینه، SEM؛ **میانه ندارد** | جدول سریع چند متغیر |
| `Analyze > Compare Means > Means` ← **Options** | هر شاخص به تفکیک **گروه** (از جمله میانه و میانگین هندسی) | خلاصه به تفکیک جنس و … |
| `Analyze > Descriptive Statistics > Explore` | میانگین، میانه، SD، IQR، چارک‌ها، نمودار جعبه‌ای | بررسی شکل توزیع (M06) |

**نکته‌ها:**
- **CV** را SPSS مستقیم گزارش نمی‌کند؛ از SD و میانگین حساب کنید (یا با `AGGREGATE` در Syntax).
- اگر یک متغیر **چند نما** داشته باشد، SPSS کوچک‌ترین را نشان می‌دهد و زیرنویس «Multiple modes exist» می‌گذارد.
- چارک‌ها در Frequencies و Explore با روش **Weighted Average (HAVERAGE)** = تعریف ۶ حساب می‌شوند (M06).

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

Syntax کامل: [`M05_solutions.sps`](M05_solutions.sps). روش منویی:

<details>
<summary><b>حل ع۱ و ع۲</b></summary>

`Frequencies` ← متغیرها: `sbp ldl hscrp cigs` ← تیک Display frequency tables را بردارید ← **Statistics**: Mean، Median، Mode، Std. deviation، Variance، Range، Minimum، Maximum، S.E. mean ← OK.
خروجی: جدول Statistics با همهٔ اعداد جواب‌ها.

</details>

<details>
<summary><b>حل ع۳</b></summary>

از خروجی ع۱: CV = SD ÷ میانگین × ۱۰۰ ← sbp: 11.32/130.19 = **8.7٪**؛ ldl: **24.3٪**؛ hscrp: 4.47/3.11 = **143.9٪**. (Syntax فایل حل همین را با `AGGREGATE` می‌سازد.)

</details>

<details>
<summary><b>حل ع۴</b></summary>

`Descriptives` ← `sbp ldl` ← Options: Mean، Std. deviation، S.E. mean ← SEM ldl **4.60**، sbp **1.63**. بازه‌ها را با ماشین‌حساب از خروجی بسازید.

</details>

<details>
<summary><b>حل ع۵</b></summary>

`Analyze > Compare Means > Means` ← Dependent List: `sbp ldl hdl`؛ Independent List: `sex` ← Options: Number of Cases، Mean، Standard Deviation ← OK.

</details>

<details>
<summary><b>حل ع۶</b></summary>

1. `Means` ← Dependent: `hscrp` ← Options: Mean، Median، **Geometric Mean** ← 3.11، 1.75، 1.85.
2. `Explore` ← Dependent: `hscrp` ← Statistics: **Percentiles** ← جدول Percentiles، ردیف Weighted Average: Q1 = **1.000**، Q3 = **3.375**.

</details>

<details>
<summary><b>حل ع۷</b></summary>

1. `Compute` ← `smoker = cigs > 0` ← `Frequencies` ← ۱۵ (۳۱٫۳٪).
2. `Data > Select Cases` ← If `cigs > 0` ← Filter ← `Frequencies` روی `cigs` با Median و Mean ← **15** و **16**. سپس Select Cases را به All cases برگردانید.

</details>

## خطاهای رایج

| مشکل | علت | راه‌حل |
|---|---|---|
| میانه در Descriptives نیست | این پنجره میانه ندارد | Frequencies یا Explore |
| Frequencies جدول بسیار بلندی داد | جدول فراوانی برای متغیر کمّی | تیک Display frequency tables را بردارید |
| پس از Select Cases همهٔ تحلیل‌ها روی زیرمجموعه است | فیلتر فعال مانده | Select Cases ← All cases |
