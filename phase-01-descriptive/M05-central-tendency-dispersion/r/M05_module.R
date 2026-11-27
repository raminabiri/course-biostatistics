d <- read.csv("data/M05_module.csv")
x <- d$wait
result <- c(average=mean(x), median=median(x), average_after=mean(d$replacement),
            median_after=median(d$replacement), range=diff(range(x)),
            variance=var(x), sd=sd(x), se=sd(x)/sqrt(length(x)))
stopifnot(max(abs(result-c(14,14,18,14,8,10,sqrt(10),sqrt(2))))<1e-10)
print(result)
