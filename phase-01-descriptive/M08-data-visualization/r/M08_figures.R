d <- read.csv("data/M08_followup.csv")
groups <- split(d, d$group)
days <- c(0, 7, 14)
visits <- c("day0", "day7", "day14")
colors <- c(A = "#126078", B = "#9c401a")

png("figures/baseline-points.png", width = 1000, height = 500, res = 120)
stripchart(day0 ~ group, data = d, method = "stack", pch = 19,
           col = colors, xlab = "Baseline systolic BP (mmHg)", ylab = "Group")
dev.off()

png("figures/age-pressure.png", width = 1000, height = 620, res = 120)
plot(d$age, d$day0, col = colors[d$group], pch = ifelse(d$group == "A", 19, 17),
     xlab = "Age (years)", ylab = "Baseline systolic BP (mmHg)")
legend("topleft", legend = names(colors), col = colors, pch = c(19, 17), bty = "n")
dev.off()

png("figures/followup.png", width = 1140, height = 560, res = 120)
par(mfrow = c(1, 2))
for (group in names(groups)) {
  values <- as.matrix(groups[[group]][visits])
  matplot(days, t(values), type = "b", lty = 1, pch = 19, cex = 0.6,
          col = colors[group], xaxt = "n", ylim = range(d[visits], na.rm = TRUE),
          xlab = "Day", ylab = "Systolic BP (mmHg)", main = paste("Group", group))
  axis(1, at = days)
}
dev.off()

for (group in names(groups)) {
  g <- groups[[group]]
  print(group)
  print(sapply(g[c("age", "day0")], function(x) c(mean = mean(x), sd = sd(x))))
  print(colSums(!is.na(g[visits])))
  print(mean(g$day14 - g$day0, na.rm = TRUE))
}

png("figures/distribution-comparison.png", width = 1440, height = 520, res = 120)
par(mfrow = c(1, 3), mar = c(4.4, 4.1, 2.1, .8))
hist(d$day0, breaks = seq(110, 170, by = 10), right = FALSE,
     col = "#126078", xlab = "Baseline systolic BP (mmHg)", main = "Histogram")
boxplot(day0 ~ group, data = d, col = colors, outline = FALSE,
        xlab = "Group", ylab = "Baseline systolic BP (mmHg)", main = "Box and points")
stripchart(day0 ~ group, data = d, vertical = TRUE, add = TRUE,
           method = "stack", pch = 21, bg = "white")
plot(NULL, xlim = c(.5, 2.5), ylim = range(d$day0), xaxt = "n",
     xlab = "Group", ylab = "Baseline systolic BP (mmHg)", main = "Violin and points")
axis(1, at = 1:2, labels = names(groups))
for (i in seq_along(groups)) {
  values <- groups[[i]]$day0
  curve <- density(values, bw = 5, from = min(values), to = max(values))
  width <- curve$y * 6
  polygon(c(i - width, rev(i + width)), c(curve$x, rev(curve$x)),
          col = colors[i], border = NA)
  points(rep(i, length(values)), values, pch = 21, bg = "white")
}
dev.off()

png("figures/mean-and-se.png", width = 960, height = 650, res = 120)
means <- vapply(groups, function(g) mean(g$day0), numeric(1))
se <- vapply(groups, function(g) sd(g$day0) / sqrt(nrow(g)), numeric(1))
centers <- barplot(means, col = colors, ylim = c(0, 155),
                   xlab = "Group", ylab = "Mean baseline systolic BP (mmHg)")
arrows(centers, means - se, centers, means + se, angle = 90, code = 3, length = .06)
dev.off()
