d <- read.csv("data/M54_cv.csv")
errors <- lapply(sort(unique(d$fold)),function(f) {
  train <- d[d$fold!=f,]
  test <- d[d$fold==f,]
  fit <- lm(y~x,train)
  cbind(mean=(test$y-mean(train$y))^2,linear=(test$y-predict(fit,test))^2)
})
out <- sqrt(colMeans(do.call(rbind,errors)))
print(out)
stopifnot(out["linear"]<out["mean"])
