count_runs <- function(x) 1 + sum(diff(x) != 0)
combinations <- function(n, k) if (k < 0 || k > n) 0 else choose(n, k)
runs_test <- function(x) {
  n1 <- sum(x == 1)
  n0 <- sum(x == 0)
  stopifnot(n0 > 0, n1 > 0, n0+n1 == length(x))
  possibilities <- 2:length(x)
  counts <- vapply(possibilities, function(r) {
    k <- r %/% 2
    a <- combinations(n0-1, k-1)
    b <- combinations(n1-1, k-1)
    if (r %% 2 == 0) return(2*a*b)
    combinations(n0-1,k)*b + a*combinations(n1-1,k)
  }, numeric(1))
  observed <- count_runs(x)
  stopifnot(sum(counts) == choose(length(x),n1))
  c(runs=observed, p=min(1, 2*min(sum(counts[possibilities <= observed]),
                                  sum(counts[possibilities >= observed]))/sum(counts)))
}
report <- function(file, exact) {
  data <- read.csv(file)
  pairs <- subset(data, design == "paired")
  delta <- pairs$after - pairs$before
  nonzero <- delta[delta != 0]
  positive <- sum(nonzero > 0)
  cat(file, "\n")
  cat("L1: positive, negative, zero, left p, two-sided p:",
      positive, sum(nonzero < 0), sum(delta == 0),
      binom.test(positive, length(nonzero), alternative="less")$p.value,
      binom.test(positive, length(nonzero))$p.value, "\n")
  rank <- wilcox.test(nonzero, exact=exact, correct=FALSE)
  cat("L2: W+, two-sided p, exact:", rank$statistic,rank$p.value,exact,"\n")
  sequence <- subset(data, design == "runs")
  cat("L3:"); print(runs_test(sequence$before[order(sequence$id)]))
}
report("data/practice.csv", TRUE)
report("data/extended.csv", FALSE)
