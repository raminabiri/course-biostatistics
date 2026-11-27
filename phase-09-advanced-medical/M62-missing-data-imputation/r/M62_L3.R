d <- read.csv("data/M62_missing.csv")
missing <- is.na(d$y)
base <- d$y
base[missing] <- ave(base, d$group, FUN = function(x) mean(x, na.rm = TRUE))[missing]
target <- missing & d$group == "B"
delta <- c(0, -3, -6, -4.5)
overall <- vapply(delta, function(shift) mean(base + shift * target), numeric(1))
stopifnot(isTRUE(all.equal(overall, c(17, 16, 15, 15.5))))
print(data.frame(delta, overall))
