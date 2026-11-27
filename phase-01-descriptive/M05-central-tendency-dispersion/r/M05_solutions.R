# =============================================================
# ماژول M05 — شاخص‌های مرکزی و پراکندگی | مسیر R | حل تمرین‌های عملی
# Working directory = پوشهٔ همین فایل
# =============================================================

d <- read.csv("../data/M05_lipid.csv")

# ---- ع۱: شاخص‌های مرکزی ----
sapply(d[, c("sbp", "ldl", "hscrp")], mean)     # 130.19 131.08 3.11
sapply(d[, c("sbp", "ldl", "hscrp")], median)   # 130.00 136.50 1.75
# R تابع آماده‌ای برای نما ندارد؛ با جدول فراوانی:
tab <- table(d$cigs)
tab
names(tab)[which.max(tab)]                       # "0"

# ---- ع۲: پراکندگی ----
for (v in c("sbp", "ldl")) {
  x <- d[[v]]
  cat(v, ": sd =", round(sd(x), 2), " var =", round(var(x), 2),
      " min =", min(x), " max =", max(x), " range =", diff(range(x)), "\n")
}
# sbp: sd 11.32, var 128.11, 99–155 (56) | ldl: sd 31.85, var 1014.42, 57–202 (145)

# ---- ع۳: ضریب تغییرات ----
cv <- function(x) 100 * sd(x) / mean(x)
round(sapply(d[, c("sbp", "ldl", "hscrp")], cv), 1)   # 8.7 24.3 143.9

# ---- ع۴: SEM و دو بازهٔ «± 2» ----
sem <- function(x) sd(x) / sqrt(length(x))
round(sem(d$ldl), 2); round(sem(d$sbp), 2)             # 4.60 1.63
round(mean(d$ldl) + c(-2, 2) * sd(d$ldl), 1)           # 67.4 194.8  (افراد)
round(mean(d$ldl) + c(-2, 2) * sem(d$ldl), 1)          # 121.9 140.3 (میانگین)

# ---- ع۵: خلاصه به تفکیک جنس ----
aggregate(cbind(sbp, ldl, hdl) ~ sex, data = d,
          FUN = function(x) c(n = length(x), mean = round(mean(x), 2), sd = round(sd(x), 2)))

# ---- ع۶: hsCRP چوله ----
x <- d$hscrp
round(c(mean = mean(x), median = median(x), geo = exp(mean(log(x)))), 2)  # 3.11 1.75 1.85
quantile(x, c(0.25, 0.75))            # پیش‌فرض R (type 7): 1.000 3.325
quantile(x, c(0.25, 0.75), type = 6)  # روش SPSS و Prism:  1.000 3.375

# ---- ع۷: دادهٔ پرصفر ----
smk <- d$cigs[d$cigs > 0]
c(n_smokers = length(smk), pct = round(100 * mean(d$cigs > 0), 1))   # 15, 31.2*
c(median = median(smk), mean = mean(smk))                             # 15, 16
# * R عدد 31.25 را به 31.2 گرد می‌کند (گرد کردن به نزدیک‌ترین زوج)؛ در گزارش 31.3٪ بنویسید.
