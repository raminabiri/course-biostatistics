d <- read.csv("data/M70_L2.csv")
train <- d$requests[1:8]
test <- d$requests[9:12]
baseline <- train[5:8]
growth <- mean(train[5:8]-train[1:4])
errors <- c(base=mean(abs(test-baseline)), trend=mean(abs(test-baseline-growth)))
drift <- mean(diff(train))
forecast <- tail(train,1)+seq_along(test)*drift
stopifnot(all(errors==c(4,0)),abs(forecast[1]-110/7)<1e-12)
print(errors)
print(forecast)
