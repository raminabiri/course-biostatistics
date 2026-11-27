data <- read.csv("data/practice.csv")
data$a <- factor(data$a)
data$b <- factor(data$b)
data$dy <- data$y-data$y0
data$dz <- data$z-data$z0
methods <- c("Pillai", "Wilks", "Hotelling-Lawley", "Roy")
print_effect <- function(title, fit, effect) {
  cat(title, "\n")
  for (method in methods) print(summary(fit, test = method)$stats[effect, ])
}
print_effect("L1: end by group", manova(cbind(y,z) ~ a, data=data), "a")
print_effect("L2: end interaction", manova(cbind(y,z) ~ a*b, data=data), "a:b")
print_effect("L3: change by group", manova(cbind(dy,dz) ~ a, data=data), "a")
print(aggregate(cbind(y,z,dy,dz) ~ a, data=data, FUN=mean))
