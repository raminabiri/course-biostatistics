# =============================================================
# ماژول M07 — جدول فراوانی و جدول توافقی | مسیر R | حل تمرین‌های عملی
# Working directory = پوشهٔ همین فایل. فقط R پایه.
# =============================================================

d <- read.csv("../data/M07_survey.csv", na.strings = "")
d$smoking   <- factor(d$smoking, levels = c("never", "former", "current"))
d$age_group <- factor(d$age_group, 1:3, c("18-39", "40-59", "60+"))
d$education <- factor(d$education, 1:3, c("primary", "secondary", "university"), ordered = TRUE)

# ---- ع۱: جدول فراوانی سیگار ----
t1 <- table(d$smoking)
cbind(n = t1, pct = round(100 * prop.table(t1), 1))      # 119/59.5  36/18.0  45/22.5

# ---- ع۲: تحصیلات با درصد تجمعی ----
t2 <- table(d$education)
cbind(n = t2, pct = round(100 * prop.table(t2), 1),
      cum = round(100 * cumsum(prop.table(t2)), 1))      # 25.5/25.5  46.0/71.5  28.5/100

# ---- ع۳: درصد و درصد معتبر (واکسن) ----
t3 <- table(d$flu_vacc, useNA = "ifany")
cbind(n = t3, pct = round(100 * t3 / nrow(d), 1))         # no 138/69.0  yes 54/27.0  NA 8/4.0
round(100 * prop.table(table(d$flu_vacc)), 1)            # معتبر: no 71.9  yes 28.1

# ---- ع۴: جنس × سیگار ----
t4 <- table(d$sex, d$smoking)
addmargins(t4)
round(100 * prop.table(t4, margin = 1), 1)               # درصد سطری: مرد فعلی 34.6، زن 8.6

# ---- ع۵: گروه سنی × واکسن ----
t5 <- table(d$age_group, d$flu_vacc)                      # NA خودکار کنار می‌رود
t5
round(100 * prop.table(t5, 1)[, "yes"], 1)               # 17.1  24.2  54.5  (سطری)
round(100 * prop.table(t5, 2)[, "yes"], 1)               # 25.9  29.6  44.4  (ستونی)

# ---- ع۶: سلامت ضعیف (۴–۵) ----
d$poor_health <- ifelse(d$self_health >= 4, 1, 0)         # NA ها NA می‌مانند
table(d$poor_health)                                      # 0: 143  1: 52
round(100 * mean(d$poor_health, na.rm = TRUE), 1)         # 26.7
t6 <- table(d$region, d$poor_health)
t6
round(100 * prop.table(t6, 1)[, "1"], 1)                  # rural 24.7  urban 28.0

# ---- ع۷: مقایسهٔ سیگار فعلی در دو جنس ----
p <- tapply(d$smoking == "current", d$sex, mean)
round(100 * p, 1)                                         # F 8.6  M 34.6
round(100 * (p["M"] - p["F"]), 1)                         # 26.0 واحد درصد
round(p["M"] / p["F"], 2)                                 # 4.02
odds <- p / (1 - p); round(odds["M"] / odds["F"], 2)      # نسبت شانس 5.62
