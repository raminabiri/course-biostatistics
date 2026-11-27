d <- read.csv("data/M73_L3.csv")
d$delta <- d$target-d$reference
by_group <- tapply(d$delta,d$group,mean)
contrast <- by_group[["comparison"]]-by_group[["control"]]
ratio <- 2^(-contrast)
stopifnot(contrast == -2, ratio == 4)
print(by_group)
print(c(delta_delta=contrast, ratio=ratio))
