data <- read.csv("data/practice.csv")
data$x <- data$baseline - 24
b0 <- subset(data, b == 0)
fit <- lm(value ~ a + x, data = b0)
cat("L1: adjusted means at baseline 24\n")
print(predict(fit, newdata = data.frame(a = 0:1, x = 0)))
print(confint(fit)["a", ])
print(anova(fit, lm(value ~ a * x, data = b0)))

small <- lm(value ~ a + b + x, data = data)
common <- lm(value ~ a * b + x, data = data)
varying <- lm(value ~ a * b * x, data = data)
cat("L2: A by B, then comparison of slopes\n")
print(anova(small, common))
print(anova(common, varying))

change <- read.csv("data/change.csv")
change$x <- change$baseline - 24
change_model <- lm(change ~ x + a, data = change)
cat("L3: difference in change adjusted at baseline 24\n")
print(anova(lm(change ~ x, data = change), change_model))
print(coef(change_model)["a"])
print(confint(change_model)["a", ])
