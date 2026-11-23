# این فایل را از پوشهٔ M09 اجرا کنید.
d <- read.csv("data/M09_individuals.csv")
stopifnot(nrow(d) == 11000, !anyDuplicated(d$id))
base <- subset(d, population == "baseline")
low <- subset(d, population == "low")

# برای هر ردیف یک نفر حساب می‌شود. سطر معیار مرجع و ستون نتیجهٔ آزمون است.
tab <- with(base, table(reference, test))
print(tab)
stopifnot(sum(tab) == 1000)
cat("L1: P(D or T) =", 1 - tab["negative", "negative"] / sum(tab), "\n")

# prop.table با ۱ روی سطر و با ۲ روی ستون شرط می‌گذارد.
cat("L2: P(T|D) =", prop.table(tab, 1)["positive", "positive"],
    "P(D|T) =", prop.table(tab, 2)["positive", "positive"], "\n")
sensitivity <- prop.table(tab, 1)["positive", "positive"]
specificity <- prop.table(tab, 1)["negative", "negative"]
for (pop in list(base, low)) {
  counts <- with(pop, table(reference, test))
  prevalence <- mean(pop$reference == "positive")
  actual <- prop.table(counts, 2)["positive", "positive"]
  tp <- prevalence * sensitivity
  fp <- (1 - prevalence) * (1 - specificity)
  predicted <- tp / (tp + fp)
  stopifnot(isTRUE(all.equal(unname(actual), unname(predicted))))
  cat("L3:", pop$population[1], "n =", sum(counts),
      "prevalence =", prevalence, "PPV =", actual, "\n")
}
