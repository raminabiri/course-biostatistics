p <- as.matrix(read.csv("data/M58_transitions.csv")[,-1])
stopifnot(max(abs(rowSums(p)-1))<1e-12)
out <- c(1,0,0) %*% p %*% p
print(out)
stopifnot(max(abs(out-c(.49,.26,.25)))<1e-12)
