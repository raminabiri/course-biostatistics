d <- read.csv("data/M09_screening.csv")
tab <- xtabs(count ~ reference + test, d)
tp <- tab["positive", "positive"]
cat("L1:", 1 - tab["negative", "negative"] / sum(tab), "\n")
cat("L2:", prop.table(tab, 1)["positive", "positive"],
    prop.table(tab, 2)["positive", "positive"], "\n")
p <- c(.01, .10)
s <- tp / sum(tab["positive", ])
c_specificity <- tab["negative", "negative"] / sum(tab["negative", ])
cat("L3:", s * p / (s * p + (1 - c_specificity) * (1 - p)), "\n")
