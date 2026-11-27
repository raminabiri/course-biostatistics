d <- read.csv("data/M49_calibration.csv")
d$expected <- d$n*d$mean_prediction
d$observed_rate <- d$observed/d$n
d$component <- (d$observed-d$expected)^2/(d$expected*(1-d$mean_prediction))
print(d)
print(sum(d$component))
stopifnot(abs(d$component[1]-50/51)<1e-10)
