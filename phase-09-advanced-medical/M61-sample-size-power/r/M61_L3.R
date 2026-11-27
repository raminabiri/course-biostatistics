events <- (qnorm(.975)+qnorm(.8))^2/(.25*log(.75)^2)
total <- ceiling(ceiling(events)/.4)
equiv <- 2*(10/3)^2*(qnorm(.95)+qnorm(.9))^2
print(c(events=events,total=total,equivalence=equiv))
stopifnot(ceiling(events)==380,total==950,ceiling(equiv)==191)
