# پاسخ‌های مسیر spss

<a id="answer-1"></a>

## پاسخ 1

`File > Import Data > CSV Data` (گام ۱). در Data View شمارهٔ آخرین سطر **30** است؛ در Variable View **12** سطر (متغیر) هست.
**جواب: ۳۰ سطر (بیمار) و ۱۲ ستون (متغیر).**

<a id="answer-2"></a>

## پاسخ 2

مراحل گام ۲. خلاصهٔ تنظیمات:

| متغیر | Values | Measure |
|---|---|---|
| sex | 1 Female، 2 Male | Nominal |
| ward | 1 Internal، 2 Surgery، 3 ICU | Nominal |
| organism | (متنی؛ برچسب لازم ندارد) | Nominal |
| cipro_res | 0 Susceptible، 1 Resistant | Nominal |
| severity | 1 Mild، 2 Moderate، 3 Severe | Ordinal |
| pain | — | Ordinal |
| age، temp، crp، wbc، los | — | Scale |

**کنترل:** `Utilities > Variables` یا دستور `DISPLAY DICTIONARY.` همهٔ تنظیمات را در خروجی نشان می‌دهد.

<a id="answer-3"></a>

## پاسخ 3

1. **پیش از تعریف:** `Analyze > Descriptive Statistics > Descriptives` ← `crp` ← N = **30**، Mean = **35.10** (Minimum = ‎-99.0 ← علامت خطر!).
2. Missing برای `crp` ← Discrete: `-99` (گام ۳).
3. **پس از تعریف:** همان تحلیل ← N = **28**، Mean = **44.68**.
4. Descriptives برای `wbc` ← N = **29** (خانهٔ خالی خودکار گمشده است).

تفسیر: دو کد ‎-99 میانگین را حدود ۱۰ واحد پایین آورده بود (درس ۱.۴).

<a id="answer-4"></a>

## پاسخ 4

1. Descriptives برای `ward` ← Mean = **1.80**. بی‌معناست، چون 1، 2، 3 فقط برچسب‌اند (درس ۱.۲، دام ۱). اگر Measure را Nominal گذاشته باشید، بعضی پنجره‌های SPSS هشدار می‌دهند یا اجازهٔ انتخاب نمی‌دهند؛ Descriptives بیشتر وقت‌ها می‌دهد.
2. `Analyze > Descriptive Statistics > Frequencies` ← `ward`، `organism`:

| ward | Frequency | Percent |
|---|---|---|
| Internal | 12 | 40.0 |
| Surgery | 12 | 40.0 |
| ICU | 6 | 20.0 |

| organism | Frequency | Percent |
|---|---|---|
| E. coli | 17 | 56.7 |
| Klebsiella | 9 | 30.0 |
| Proteus | 4 | 13.3 |

<a id="answer-5"></a>

## پاسخ 5

`Analyze > Descriptive Statistics > Crosstabs` ← Row(s): `sex`، Column(s): `cipro_res` ← OK.

| | Susceptible | Resistant | Total |
|---|---|---|---|
| Female | 13 | **7** | 20 |
| Male | 6 | 4 | 10 |

**جواب: ۷ بیمار زن مقاوم بودند.** (تحلیل این جدول در M07 و M35.)

<a id="answer-6"></a>

## پاسخ 6

`Data > Restructure` (گام ۶) یا Syntax:

```
VARSTOCASES /MAKE crp FROM crp_d0 crp_d3 crp_d7 /INDEX=visit(3) /KEEP=id.
RECODE visit (1=0) (2=3) (3=7) INTO day.
EXECUTE.
```

**جواب: ۲۴ سطر** (۸ بیمار × ۳ روز). سه سطر اول: id = 1 با day = 0، 3، 7 و crp = 94.8، 46.2، 12.1.

<a id="answer-7"></a>

## پاسخ 7

`File > Save As` ← `M01_uti_labeled.sav`. پس از بستن و باز کردن دوباره با `File > Open > Data`، در Variable View همهٔ Values، Missing و Measure سر جایشان هستند. **بله، می‌مانند.**
آزمون مقایسه: اگر همان داده را `File > Export > CSV` کنید و دوباره وارد کنید، همهٔ برچسب‌ها از بین می‌رود. به همین دلیل فایل کاری را `.sav` نگه دارید.

