d <- read.csv("data/M49_separation.csv")
p <- (d$completed + .5)/(d$completed + d$not_completed + 1)
odds <- (d$completed + .5)/(d$not_completed + .5)
ratio <- odds[2]/odds[1]
print(c(p, ratio))
stopifnot(abs(ratio-441)<1e-10)
