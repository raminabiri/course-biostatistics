long <- read.csv("data/practice.csv")
long$id <- factor(long$id)
long$time <- factor(long$time)
long$group <- factor(long$group)
long$condition <- factor(long$condition)
stopifnot(!anyNA(long$value), all(xtabs(~ id + time + condition, long) == 1))

both <- aov(value ~ time * condition + Error(id / (time * condition)), data = long)
cat("L1: time by condition\n")
print(summary(both)[["Error: id:time:condition"]])

wide <- read.csv("data/wide.csv")
stopifnot(!anyDuplicated(wide$id), !anyNA(wide))
wide$change <- wide$t2c0 - wide$t0c0
change <- t.test(wide$change[wide$group == 1], wide$change[wide$group == 0], var.equal = TRUE)
cat("L2: group 1 minus group 0 change\n")
print(change)

zero <- subset(long, condition == 0)
mixed <- aov(value ~ group * time + Error(id / time), data = zero)
cat("L3: time by group in condition 0\n")
print(summary(mixed)[["Error: id:time"]])
