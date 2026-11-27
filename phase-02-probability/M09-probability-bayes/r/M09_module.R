d <- read.csv("data/M09_individuals.csv")
t <- table(d$population,d$joint_code)
baseline <- t["baseline",]
low <- t["low",]
result <- c(union=1-baseline[4]/sum(baseline),
            sensitivity=baseline[1]/sum(baseline[1:2]),
            ppv_base=baseline[1]/sum(baseline[c(1,3)]),
            ppv_low=low[1]/sum(low[c(1,3)]))
stopifnot(nrow(d)==11000,max(abs(result-c(.19,.9,.5,1/12)))<1e-10)
print(t)
print(result)
