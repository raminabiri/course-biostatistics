# =============================================================
# ماژول M06 — شکل توزیع، دادهٔ پرت و تبدیل | مسیر R | حل تمرین‌های عملی
# Working directory = پوشهٔ همین فایل. فقط R پایه.
# =============================================================

d <- read.csv("../data/M06_icu.csv")

# چولگی و کشیدگی G1 و G2 (همان فرمول SPSS، Prism، Excel و pandas)
G1 <- function(x) {
  n <- length(x); m <- mean(x)
  g1 <- mean((x - m)^3) / mean((x - m)^2)^1.5
  sqrt(n * (n - 1)) / (n - 2) * g1
}
G2 <- function(x) {
  n <- length(x); m <- mean(x)
  g2 <- mean((x - m)^4) / mean((x - m)^2)^2 - 3
  ((n + 1) * g2 + 6) * (n - 1) / ((n - 2) * (n - 3))
}

# ---- ع۱: خلاصهٔ پنج‌عددی ----
five <- function(x, type) c(min = min(x), quantile(x, c(.25, .5, .75), type = type), max = max(x))
five(d$lactate, 6)   # 0.5  1.025  1.6  2.7  6.5   (روش SPSS/Prism)
five(d$lactate, 7)   # 0.5  1.075  1.6  2.7  6.5   (پیش‌فرض R)
five(d$sodium, 6)    # 124  136  139  142  168

# ---- ع۲: چولگی و کشیدگی ----
v <- c("age", "sodium", "lactate", "los")
round(rbind(skew = sapply(d[v], G1), kurt = sapply(d[v], G2)), 2)
#        age sodium lactate   los
# skew -0.02   2.11    1.43  3.04
# kurt -0.32  12.06    2.10 10.98

# ---- ع۳: حصارهای توکی ----
tukey <- function(x, type = 6) {
  q <- unname(quantile(x, c(.25, .75), type = type)); iqr <- q[2] - q[1]
  c(lower = q[1] - 1.5 * iqr, upper = q[2] + 1.5 * iqr)
}
f <- tukey(d$lactate); f                          # -1.49  5.21
sort(d$lactate[d$lactate > f["upper"]])           # 5.5 6.5
f2 <- tukey(d$los); f2                            # -3  13
sort(d$los[d$los > f2["upper"]])                  # 17 17 20 23 28 41

# ---- ع۴: نمرهٔ z و پوشاندن ----
s <- d$sodium
z <- (s - mean(s)) / sd(s)                        # یا: as.vector(scale(s))
round(z[s %in% c(168, 124)], 2)                   # 5.20 (168)  -2.72 (124)
sum(abs(z) > 3)                                   # 1
s2 <- s[s != 168]
round((124 - mean(s2)) / sd(s2), 2)               # -3.57

# ---- ع۵: میانگین ۵٪ پیراسته ----
round(c(mean = mean(d$los), median = median(d$los), trim5 = mean(d$los, trim = 0.05)), 2)  # 6.55 4 5.52
round(c(mean = mean(d$lactate), trim5 = mean(d$lactate, trim = 0.05)), 2)                  # 2.00 1.88

# ---- ع۶: تبدیل لگاریتمی لاکتات ----
lx <- log10(d$lactate)
round(c(skew_log = G1(lx), mean_log = mean(lx), sd_log = sd(lx)), 4)   # 0.16 0.2231 0.2610
round(c(geo_mean = 10^mean(lx), geo_sd = 10^sd(lx)), 2)                # 1.67 1.82
round(10^(mean(lx) + c(-1, 1) * sd(lx)), 2)                            # 0.92 3.05

# ---- ع۷: تحلیل حساسیت سدیم ----
sens <- function(x) round(c(n = length(x), mean = mean(x), sd = sd(x), skew = G1(x)), 2)
rbind(all = sens(s), without_168 = sens(s2))
#               n   mean   sd  skew
# all          60 139.13 5.56  2.11
# without_168  59 138.64 4.10 -0.53
