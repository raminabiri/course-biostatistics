data <- read.csv("data/M11_measurements.csv")
x <- data$value
stopifnot(length(x) == 16L, all(is.finite(x)))

png("figures/normal-qq.png", width = 960, height = 640, res = 120)
qqnorm(x, pch = 19, col = "#126078",
       xlab = "Theoretical normal quantile", ylab = "Reported measurement",
       main = "Normal Q-Q plot")
qqline(x, col = "#9c401a", lwd = 2)
dev.off()
