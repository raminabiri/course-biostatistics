d <- read.csv("data/M01_module.csv")
stopifnot(!anyDuplicated(d[c("patient_id", "day")]))
daily <- lapply(split(d$temperature, d$day), function(x) {
  c(rows = length(x), valid = sum(!is.na(x)), mean = mean(x, na.rm = TRUE))
})
pairs <- reshape(d[c("patient_id", "day", "temperature")],
                idvar = "patient_id", timevar = "day", direction = "wide")
change <- mean(pairs$temperature.3 - pairs$temperature.0, na.rm = TRUE)
stopifnot(length(unique(d$patient_id)) == 3L, sum(d$day == 0 & d$ward == "internal") == 2L,
          daily[["3"]][["valid"]] == 2L, abs(daily[["0"]][["mean"]] - 37.3666666667) < 1e-9,
          abs(daily[["3"]][["mean"]] - 37.2) < 1e-9, abs(change + .25) < 1e-9)
print(do.call(rbind, daily))
print(c(paired_mean_change = change))
