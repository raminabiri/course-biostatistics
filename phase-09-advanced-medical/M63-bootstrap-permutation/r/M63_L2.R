d <- read.csv("data/M63_permutation.csv")
observed <- mean(d$score[d$group == "B"]) - mean(d$score[d$group == "A"])
sums <- combn(d$score, 3, sum)
diffs <- (sum(d$score) - 2 * sums) / 3
p <- mean(abs(diffs) >= abs(observed))
stopifnot(observed == 4, length(diffs) == 20, p == 0.1)
print(c(observed = observed, allocations = length(diffs), p = p))
