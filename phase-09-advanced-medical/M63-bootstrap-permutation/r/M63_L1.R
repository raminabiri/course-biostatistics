waiting <- read.csv("data/M63_mini.csv")$waiting_minutes
resamples <- expand.grid(first = waiting, second = waiting, third = waiting)
averages <- rowMeans(resamples)
center <- mean(averages)
se <- sqrt(mean((averages - center)^2))
stopifnot(length(averages) == 27, center == 4, abs(se - sqrt(8/9)) < 1e-12)
print(c(samples = length(averages), center = center, SE = se))
