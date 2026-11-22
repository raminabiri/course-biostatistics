# PROGRESS

## Done
- 2026-10-21: Reviewed chatgpt.odt + gemini.odt. Decided: Persian, GitHub, RTL, Persian terms, step-by-step exercises + solutions.
- 2026-10-26: Architecture final: 13 phases (0–12), M01–M82 + P01–P05; 7 folders per module (lessons, data, spss, prism, r, python, excel). Course is GENERAL biostat/medical (not microbiology-only). See SYLLABUS.md.
- 2026-10-26: **Phase 0 (M01–M04) COMPLETE.** Writing rules in memory (course-writing-standards): no proofs, many graded exercises (levels 1–3) with hidden solutions, verified references incl. Persian/English videos.
  - Totals: 18 lessons, 60 worked examples, 207 lesson exercises, 33 review questions, 7 shared practice exercises per module in all 5 tracks (+ R/Python bonus in M03).
  - Each module: README, lessons/, data/ (+codebook), 5 track READMEs, R + Python scripts, SPSS .sps, Excel practice + solutions .xlsx, review.md, references.md.
  - M01: upgraded (graded exercises, refs, Excel). M02 math prerequisites. M03 sampling & study design (frame with ready random column `u` so all tools give identical answers). M04 cleaning (messy registry, protocol P1–P11, cleaning log, merge/append/aggregate).
  - Verification: all R and Python scripts run (R 4.6.1, pandas 2.3.3), answers identical across both. All Excel solution workbooks recalculated in LibreOffice headless and checked against expected values (0 mismatches). No broken internal links.
  - Glossary extended (M01–M04). Root README, tracks/*.md and SYLLABUS status updated. Prism coverage for M03 set to ◐.

## Next steps
- User: run SPSS .sps files (M01–M04) on real SPSS; check Prism 10/11 menu names; watch Persian Aparat videos before recommending (content not verifiable by me).
- Phase 1 (M05–M08: descriptive statistics & visualization) when the user asks. Keep: same module template, same 5 tracks, graded exercises, verified references, varied medical domains.
- Decide license (proposed CC BY-SA 4.0 content + MIT code).
- Optional: translate PROGRESS.md to Persian (offered, no answer yet).

## Bugs / issues / caveats
- SPSS syntax is UNTESTED (no SPSS/PSPP here; PSPP install needs sudo).
- Prism steps written from knowledge of Prism 9/10 and the Prism 11 online guide; not run in the app.
- Excel: use RANK (not RANK.EQ) and avoid newer functions without _xlfn prefix when generating xlsx with openpyxl (they show #NAME?).
- Excel COUNTIF/PivotTable are case-insensitive (M04 ع۱ shows 7 sex spellings in Excel vs 11 in R/Python/SPSS); documented in the Excel guide.
- pandas 3 is current (docs 3.1); scripts tested on 2.3 — only cosmetic difference noted (str vs object dtype).
- Build scripts for xlsx were in the session scratchpad (not in repo); to regenerate, rewrite from the solutions sheets.

## 2026-11-14 — M01 نمونهٔ تازه برای بازبینی نویسنده

- روش نگارش در WRITING_STYLE.md ثبت شد. M01 چهار درس سه‌سطحی و ۱۲۰ تمرین با چینش ۵/۱۰/۱۵ برای هر درس دارد؛ پاسخ‌های متن و مسیرها به solutions منتقل شدند.
- بانک Excel و CSV با ۱۰۰۰ فرد، ۳۰۰۰ نوبت و ۱۰۰ نمونهٔ آزمایشگاهی با ۲۰۰ خوانش، همراه کد بازسازی و بررسی R/Python افزوده شد.
- روش کار پنج نرم‌افزار به تفکیک درس، منابع و فیلم‌های هر درس و دادهٔ توصیفی module.json نوشته شد.
- اجرای R و Python و برابری Excel/CSV بررسی شد. اجرای واقعی SPSS، Prism و Excel و بازبینی مستقل علمی مانده است؛ جزئیات در M01/VALIDATION.md.
- این گام ساخت داشبورد یا اتصال چت را در بر ندارد. فایل‌های M07 که پیش از این گام در محیط بودند دست‌نخورده ماندند.

## 2026-11-14 — آغاز ساده‌تر M01

- صفحهٔ نخست دوره و M01 با یک مسیر روشن برای آغاز بازنویسی شد؛ راهنمای START و پنج راهنمای نرم‌افزار از صفر، با جدول سه‌نفری افزوده شد.
- پاسخ هر یک از ۱۲۰ تمرین و پاسخ‌های نرم‌افزاری در یک صفحهٔ جدا قرار گرفت؛ پیوند بازگشت به پرسش در پاسخ‌های درسی هست.
- سه شماتیک SVG برای Excel، SPSS و Prism همراه کد سازنده افزوده شد.
- کدهای آغاز R و Python، پیوندهای محلی و بانک داده بررسی شدند. جزئیات و کارهای مانده در VALIDATION ماژول ثبت است.

## 2026-11-14 — پیوند کمتر و تصویرهای درون متن

- صفحه‌های آغاز کوتاه‌تر شدند. منابع با سطح و بخش پیشنهادی در پایان درس آمده‌اند و فیلم یوتیوب پیوند مستقیم دارد.
- روش کار پنج نرم‌افزار در بخش‌های بازشدنی همان درس قرار گرفت؛ پایان درس تنها راه رفتن به درس پیش و بعد را همراه دارد.
- سه شماتیک به PNG تبدیل و دیداری بررسی شد. توضیح کوتاه کدهای R و Python افزوده و کدهای آغازین دوباره اجرا شد.

## 2026-11-14 — فیلم کار با نرم‌افزار در همان سطح درس

- برای چهار درس M01، بیست انتخاب فیلم در پنج مسیر، همراه سطح و دامنهٔ دیدن، در بخش بازشدنی همان نرم‌افزار قرار گرفت. فیلم‌های تکراری با تکلیف دیدن متفاوت شمرده شده‌اند.
- پنج راهنمای آغاز هم فیلم ورود داده دارند. تفاوت ابزار فیلم R در درس ۳ و نوع جدول Prism در درس ۴ روشن نوشته شده است.
- روش گزینش فیلم در WRITING_STYLE.md و جزئیات بررسی در VALIDATION.md ثبت شد.

## 2026-11-15 — لحن آموزشی و یادگیری گام‌به‌گام M01

- چهار درس، صفحهٔ شروع و پنج راهنمای نرم‌افزاری با زمینهٔ درمانگاه، معرفی معنا پیش از اصطلاح و توضیح نتیجهٔ هر کار بازنویسی شدند.
- بیست تمرین ساده و پاسخشان با نمونه‌های تازه هماهنگ شدند؛ شمار کل و چینش سه‌سطحی همان است.
- کدهای راهنمای آغاز و چهار درس در R و Python به‌ترتیب اجرا و بررسی شدند. مسیرهای منویی هنوز نیاز به بررسی روی نرم‌افزار نصب‌شده دارند.
- روش لحن آموزشی در WRITING_STYLE.md و گزارش بررسی در VALIDATION ماژول ثبت شد.
