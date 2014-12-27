###################################################
### chunk number 1: 
###################################################
#line 483 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
options("digits"=4)
options("width"=70)
options("show.signif.stars" = FALSE)
set.seed(12345)


###################################################
### chunk number 2: 
###################################################
#line 492 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
require(Amelia)
data(freetrade)


###################################################
### chunk number 3: 
###################################################
#line 500 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
summary(freetrade)


###################################################
### chunk number 4: 
###################################################
#line 508 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
summary(lm(tariff ~ polity + pop + gdp.pc + year + country, 
          data = freetrade)) 


###################################################
### chunk number 5: 
###################################################
#line 546 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
a.out <- amelia(freetrade, m = 5, ts = "year", cs = "country")
a.out


###################################################
### chunk number 6: hist1plot
###################################################
#line 564 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
hist(a.out$imputations[[3]]$tariff, col="grey", border="white")


###################################################
### chunk number 7: 
###################################################
#line 570 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
options(SweaveHooks = list(fig = function() par(mfrow=c(1,1))))


###################################################
### chunk number 8: hist1
###################################################
#line 576 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
#line 564 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw#from line#576#"
hist(a.out$imputations[[3]]$tariff, col="grey", border="white")
#line 577 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"


###################################################
### chunk number 9: 
###################################################
#line 631 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
a.out.more <- amelia(freetrade, m = 10, ts = "year", cs = "country", p2s=0)
a.out.more


###################################################
### chunk number 10: 
###################################################
#line 637 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
a.out.more <- ameliabind(a.out, a.out.more)
a.out.more


###################################################
### chunk number 11: 
###################################################
#line 691 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
amelia(freetrade, m = 1, ts = "year", cs = "country", p2s = 2)


###################################################
### chunk number 12: 
###################################################
#line 750 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
table(a.out$imputations[[3]]$polity)


###################################################
### chunk number 13: 
###################################################
#line 767 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
a.out1 <- amelia(freetrade, m = 5, ts = "year", cs = "country", ords =
                 "polity", p2s = 0)
table(a.out1$imputations[[3]]$polity)


###################################################
### chunk number 14: 
###################################################
#line 787 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
table(a.out1$imputations[[3]]$signed)


###################################################
### chunk number 15: 
###################################################
#line 805 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
a.out2 <- amelia(freetrade, m = 5, ts = "year", cs = "country", noms =
                 "signed", p2s = 0)
table(a.out2$imputations[[3]]$signed)


###################################################
### chunk number 16: logshist
###################################################
#line 837 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
hist(freetrade$tariff, col="grey", border="white")
hist(log(freetrade$tariff), col="grey", border="white")


###################################################
### chunk number 17: 
###################################################
#line 842 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
options(SweaveHooks = list(fig = function() par(mfrow=c(1,2))))


###################################################
### chunk number 18: hist2
###################################################
#line 848 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
#line 837 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw#from line#848#"
hist(freetrade$tariff, col="grey", border="white")
hist(log(freetrade$tariff), col="grey", border="white")
#line 849 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"


###################################################
### chunk number 19: 
###################################################
#line 857 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
options(SweaveHooks = list(fig = function() par(mfrow=c(1,1))))


###################################################
### chunk number 20: 
###################################################
#line 893 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
amelia(freetrade, idvars = c("year", "country"))


###################################################
### chunk number 21: 
###################################################
#line 901 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
a.out2 <- amelia(freetrade, idvars = c("year"))


###################################################
### chunk number 22: 
###################################################
#line 938 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
a.out2 <- amelia(freetrade, ts = "year", cs = "country", polytime = 2)


###################################################
### chunk number 23: 
###################################################
#line 959 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
a.out.time <- amelia(freetrade, ts = "year", cs = "country", polytime = 2,
                 intercs = TRUE, p2s = 2)


###################################################
### chunk number 24: tcomp1
###################################################
#line 972 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
tscsPlot(a.out, cs = "Malaysia", main = "Malaysia (no time settings)", 
         var = "tariff", ylim = c(-10, 60))

tscsPlot(a.out.time, cs = "Malaysia", main = "Malaysia (with time settings)", 
         var = "tariff", ylim = c(-10, 60))


###################################################
### chunk number 25: 
###################################################
#line 981 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
options(SweaveHooks = list(fig = function() par(mfrow=c(1,2))))


###################################################
### chunk number 26: timecompare
###################################################
#line 986 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
#line 972 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw#from line#986#"
tscsPlot(a.out, cs = "Malaysia", main = "Malaysia (no time settings)", 
         var = "tariff", ylim = c(-10, 60))

tscsPlot(a.out.time, cs = "Malaysia", main = "Malaysia (with time settings)", 
         var = "tariff", ylim = c(-10, 60))
#line 987 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"


###################################################
### chunk number 27: 
###################################################
#line 1014 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
a.out2 <- amelia(freetrade, ts = "year", cs = "country", lags = "tariff",
                 leads = "tariff")


###################################################
### chunk number 28: 
###################################################
#line 1043 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
a.out.time


###################################################
### chunk number 29: 
###################################################
#line 1067 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
a.out.time2 <- amelia(freetrade, ts = "year", cs = "country", polytime = 2,
                 intercs = TRUE, p2s = 0, empri = .01*nrow(freetrade))
a.out.time2


###################################################
### chunk number 30: tcomp2
###################################################
#line 1075 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
tscsPlot(a.out.time, cs = "Malaysia", main = "Malaysia (no ridge prior)", 
         var = "tariff", ylim = c(-10, 60))

tscsPlot(a.out.time2, cs = "Malaysia", main = "Malaysia (with ridge prior)", 
         var = "tariff", ylim = c(-10, 60))


###################################################
### chunk number 31: 
###################################################
#line 1083 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
options(SweaveHooks = list(fig = function() par(mfrow=c(1,2))))


###################################################
### chunk number 32: timecomp2
###################################################
#line 1089 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
#line 1075 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw#from line#1089#"
tscsPlot(a.out.time, cs = "Malaysia", main = "Malaysia (no ridge prior)", 
         var = "tariff", ylim = c(-10, 60))

tscsPlot(a.out.time2, cs = "Malaysia", main = "Malaysia (with ridge prior)", 
         var = "tariff", ylim = c(-10, 60))
#line 1090 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"


###################################################
### chunk number 33: 
###################################################
#line 1138 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
freetrade[freetrade$country == "Thailand", c("year","country","tariff")]


###################################################
### chunk number 34:  eval=FALSE
###################################################
## #line 1143 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
## #$


###################################################
### chunk number 35: 
###################################################
#line 1152 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
pr <- matrix(c(158,159,160,3,3,3,40,40,40,3,3,3), nrow=3, ncol=4) 
pr


###################################################
### chunk number 36: 
###################################################
#line 1161 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
a.out.pr <- amelia(freetrade, ts = "year", cs = "country", priors = pr)


###################################################
### chunk number 37: 
###################################################
#line 1171 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
pr.2 <- matrix(c(158,159,160,3,3,3,34,34,34,46,46,46,.95,.95,.95), nrow=3, ncol=5)
pr.2


###################################################
### chunk number 38: 
###################################################
#line 1184 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
pr.3 <- matrix(c(158,159,160,0,3,3,3,3,40,40,40,20,3,3,3,5), nrow=4, ncol=4)
pr.3


###################################################
### chunk number 39: 
###################################################
#line 1230 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
bds <- matrix(c(3, 30, 40), nrow = 1, ncol = 3)
bds


###################################################
### chunk number 40: 
###################################################
#line 1237 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
a.out.bds <- amelia(freetrade, ts = "year", cs = "country", bounds = bds,
                    max.resample = 1000)


###################################################
### chunk number 41: bounds
###################################################
#line 1248 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
tscsPlot(a.out, cs = "Malaysia", main = "No logical bounds", var =
         "tariff", ylim = c(-10,60))

tscsPlot(a.out.bds, cs = "Malaysia", main = "Bounded between 30 and 40", var =
         "tariff", ylim = c(-10,60))


###################################################
### chunk number 42: 
###################################################
#line 1262 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
options(SweaveHooks = list(fig = function() par(mfrow=c(1,2))))


###################################################
### chunk number 43: boundscomp
###################################################
#line 1268 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
#line 1248 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw#from line#1268#"
tscsPlot(a.out, cs = "Malaysia", main = "No logical bounds", var =
         "tariff", ylim = c(-10,60))

tscsPlot(a.out.bds, cs = "Malaysia", main = "Bounded between 30 and 40", var =
         "tariff", ylim = c(-10,60))
#line 1269 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"


###################################################
### chunk number 44: plotmeth
###################################################
#line 1299 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
plot(a.out, which.vars = 3:6)


###################################################
### chunk number 45: plot1
###################################################
#line 1307 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
#line 1299 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw#from line#1307#"
plot(a.out, which.vars = 3:6)
#line 1308 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"


###################################################
### chunk number 46: 
###################################################
#line 1337 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
compare.density(a.out, var = "signed")


###################################################
### chunk number 47: 
###################################################
#line 1341 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
options(SweaveHooks = list(fig = function() par(mfrow=c(1,1))))


###################################################
### chunk number 48: overimp
###################################################
#line 1371 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
overimpute(a.out, var = "tariff")


###################################################
### chunk number 49: 
###################################################
#line 1375 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
options(SweaveHooks = list(fig = function() par(mfrow=c(1,1))))


###################################################
### chunk number 50: oi2
###################################################
#line 1381 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
#line 1371 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw#from line#1381#"
overimpute(a.out, var = "tariff")
#line 1382 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"


###################################################
### chunk number 51: overimp-bad
###################################################
#line 1408 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
dd <- Amelia:::rmvnorm(50, mu = c(0.5,0.5), vcv =
                       matrix(c(0.25^2,.06, .06,0.25^2),2,2))
ddmiss <- sample(1:50, replace = FALSE, size = 10)
is.na(dd) <- ddmiss
aa.out <- amelia(dd, m= 5)
overimpute(aa.out, var = 2, main = "Observed versus Imputed Values")


###################################################
### chunk number 52: oi
###################################################
#line 1419 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
#line 1408 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw#from line#1419#"
dd <- Amelia:::rmvnorm(50, mu = c(0.5,0.5), vcv =
                       matrix(c(0.25^2,.06, .06,0.25^2),2,2))
ddmiss <- sample(1:50, replace = FALSE, size = 10)
is.na(dd) <- ddmiss
aa.out <- amelia(dd, m= 5)
overimpute(aa.out, var = 2, main = "Observed versus Imputed Values")
#line 1420 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"


###################################################
### chunk number 53: disp1d
###################################################
#line 1492 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
disperse(a.out, dims = 1, m = 5)
disperse(a.out, dims = 2, m = 5)


###################################################
### chunk number 54: 
###################################################
#line 1501 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
options(SweaveHooks = list(fig = function() par(mfrow=c(1,2))))


###################################################
### chunk number 55: disp1dfig
###################################################
#line 1506 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
#line 1492 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw#from line#1506#"
disperse(a.out, dims = 1, m = 5)
disperse(a.out, dims = 2, m = 5)
#line 1507 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"


###################################################
### chunk number 56: 
###################################################
#line 1537 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
set.seed(02138)


###################################################
### chunk number 57: 
###################################################
#line 1540 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
freetrade2 <- freetrade
freetrade2$tariff2 <- freetrade2$tariff*2+3


###################################################
### chunk number 58: 
###################################################
#line 1544 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
## We add a little bit of noise here to avoid numeric problems
freetrade2$tariff2 <- freetrade2$tariff*2+3 +
  rnorm(nrow(freetrade), 0, 0.000001)


###################################################
### chunk number 59: 
###################################################
#line 1553 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
a.out.bad <- amelia(freetrade2, ts = "year", cs = "country")
a.out.bad


###################################################
### chunk number 60: dispbad
###################################################
#line 1561 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
disperse(a.out.bad, dims = 1, m = 10)


###################################################
### chunk number 61: 
###################################################
#line 1572 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
options(SweaveHooks = list(fig = function() par(mfrow=c(1,1))))


###################################################
### chunk number 62: dispbadfig
###################################################
#line 1577 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
#line 1561 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw#from line#1577#"
disperse(a.out.bad, dims = 1, m = 10)
#line 1578 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"


###################################################
### chunk number 63: tsplot1
###################################################
#line 1602 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
tscsPlot(a.out.time, cs = "Malaysia", main = "Malaysia (with time settings)", 
         var = "tariff", ylim = c(-10, 60))


###################################################
### chunk number 64: tsplot2
###################################################
#line 1614 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
#line 1602 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw#from line#1614#"
tscsPlot(a.out.time, cs = "Malaysia", main = "Malaysia (with time settings)", 
         var = "tariff", ylim = c(-10, 60))
#line 1615 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"


###################################################
### chunk number 65: mmap1
###################################################
#line 1669 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
missmap(a.out) 


###################################################
### chunk number 66: mmap2
###################################################
#line 1681 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
#line 1669 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw#from line#1681#"
missmap(a.out) 
#line 1682 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"


###################################################
### chunk number 67: 
###################################################
#line 1716 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
require(Zelig)
z.out <- zelig(tariff ~ polity + pop + gdp.pc + year +country, data = freetrade, model = "ls")


###################################################
### chunk number 68: 
###################################################
#line 1721 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
summary(z.out)


###################################################
### chunk number 69: 
###################################################
#line 1730 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
z.out.imp <- zelig(tariff ~ polity + pop + gdp.pc + year +country, data =
                   a.out$imputations, model = "ls")


###################################################
### chunk number 70: 
###################################################
#line 1735 "d:/Rcompile/CRANpkg/local/2.12/Amelia/inst/doc/amelia.Rnw"
summary(z.out.imp)


