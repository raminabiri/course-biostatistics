set.seed(120)
sizes <- c(1, 5, 30)
simulations <- lapply(sizes, function(n) {
  replicate(5000, mean(rexp(n, rate = 0.1)))
})

breaks <- seq(0, ceiling(max(unlist(simulations)) / 2) * 2, by = 2)
histograms <- lapply(simulations, hist, breaks = breaks, plot = FALSE)
max_density <- max(vapply(histograms, function(h) max(h$density), numeric(1)))

png("figures/sampling-means.png", width = 1560, height = 560, res = 120)
par(mfrow = c(1, 3), mar = c(4.5, 4.2, 2.5, 0.8))
for (i in seq_along(sizes)) {
  plot(histograms[[i]], freq = FALSE, col = "#126078", border = "white",
       main = paste("n =", sizes[i]), xlim = c(0, 40), ylim = c(0, max_density),
       xlab = "Sample mean (minutes)", ylab = "Density")
  abline(v = 10, lty = 2, lwd = 2)
}
dev.off()

result <- data.frame(
  n = sizes,
  mean = vapply(simulations, mean, numeric(1)),
  simulated_se = vapply(simulations, sd, numeric(1)),
  theoretical_se = 10 / sqrt(sizes)
)
cat("L1: for n=5, individual measurements =", 5000 * 5, "and means =", 5000, "\n")
cat("L2: theoretical SE for n=25 =", 10 / sqrt(25), "\n")
print(result)
stopifnot(all(abs(result$mean - 10) < 0.4),
          all(abs(result$simulated_se / result$theoretical_se - 1) < 0.08))
