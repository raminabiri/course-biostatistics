* =============================================================.
* ماژول M06 — شکل توزیع، دادهٔ پرت و تبدیل | مسیر SPSS | حل تمرین‌های عملی ع۱ تا ع۷.
* خط CD را به مسیر پوشهٔ data تغییر دهید.
* =============================================================.
CD 'C:\biostat\phase-1-descriptive\M06-distribution-shape-outliers\data'.

GET DATA /TYPE=TXT /FILE='M06_icu.csv' /ENCODING='UTF8'
  /DELIMITERS="," /ARRANGEMENT=DELIMITED /FIRSTCASE=2
  /VARIABLES= id F3.0 age F3.0 sodium F4.0 lactate F4.1 los F3.0 plt F4.0.
DATASET NAME icu WINDOW=FRONT.

* ---- ع۱، ع۲، ع۵: Explore همه را با هم می‌دهد ----.
EXAMINE VARIABLES=lactate sodium los age
  /PERCENTILES(25,50,75)=HAVERAGE
  /STATISTICS=DESCRIPTIVES EXTREME(5)
  /PLOT=BOXPLOT.
* جدول Descriptives: Mean، 5% Trimmed Mean، Median، Skewness (با Std. Error)، Kurtosis.
* انتظار: چولگی age -0.02، sodium 2.11، lactate 1.43، los 3.04؛ کشیدگی sodium 12.06، los 10.98.
* 5% Trimmed Mean: los 5.52، lactate 1.88.
* جدول Percentiles: ردیف Weighted Average (تعریف ۶): lactate Q1 1.025، Q3 2.700.
*   اگر ردیف Tukey's Hinges هم نمایش داده شد، آن روش «میانهٔ نیمه‌ها» است (درس ۶.۱).
* جدول Extreme Values: ۵ مقدار بزرگ‌تر و کوچک‌تر هر متغیر.
* نمودار جعبه‌ای: ○ = مقدار دور (۱٫۵ تا ۳ برابر طول جعبه)، * = بسیار دور (بیش از ۳ برابر).

* ---- ع۳: حصارهای توکی (از روی جدول Percentiles) ----.
* lactate: 2.7 + 1.5 × (2.7 − 1.025) = 5.21 ← مقادیر بالاتر: 5.5 و 6.5.
COUNT out_lac = lactate (5.2125 THRU HI).
COUNT out_los = los (13.0001 THRU HI).
FREQUENCIES VARIABLES=out_lac out_los.
* انتظار: 2 و 6.

* ---- ع۴: نمرهٔ z (DESCRIPTIVES /SAVE متغیر Zsodium می‌سازد) ----.
DESCRIPTIVES VARIABLES=sodium /SAVE.
TEMPORARY.
SELECT IF (ABS(Zsodium) > 3).
LIST id sodium Zsodium.
* انتظار: فقط سدیم 168 با z = 5.20؛ سدیم 124: z = -2.72.
TEMPORARY.
SELECT IF (sodium <> 168).
DESCRIPTIVES VARIABLES=sodium /STATISTICS=MEAN STDDEV SKEWNESS.
* انتظار (ع۷ هم): n 59، میانگین 138.64، SD 4.10، چولگی -0.53 ← z(124) = (124 − 138.64)/4.10 = -3.57.

* ---- ع۶: تبدیل لگاریتمی ----.
COMPUTE log_lac = LG10(lactate).
EXECUTE.
DESCRIPTIVES VARIABLES=log_lac /STATISTICS=MEAN STDDEV SKEWNESS.
MEANS TABLES=lactate /CELLS=GEOMETRIC.
* انتظار: چولگی 0.16، میانگین 0.2231، SD 0.2610؛ میانگین هندسی 1.67.
* SD هندسی = 10**0.261 = 1.82؛ بازه 1.67/1.82 تا 1.67×1.82 = 0.92 تا 3.05.
