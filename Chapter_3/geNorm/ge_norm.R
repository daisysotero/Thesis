#install.packages("ReadqPCR")
#install.packages("NormqPCR")

#Call the directory named "library" from the desired package
library(ReadqPCR)
library(NormqPCR)

######NORMPCR#######

#Place the dataset archive (.txt) in the normqPCR directory
#normqPCR directory: "C:/Users/daisy/AppData/Local/R/win-library/4.2/NormqPCR/exData"
#Realized two analyses: leaves vs. seeds ("dataset_geNorm.txt") and Acari vs. JS ("geNorm2.txt")


###################################################
### geNorm - First analyse: leaves vs. seeds 
###################################################

path <- system.file("exData", package = "NormqPCR")
qPCR.example.techReps <- file.path(path, "dataset_geNorm.txt")
qPCRBatch.qPCR.techReps <- read.qPCR(qPCR.example.techReps)

rownames(exprs(qPCRBatch.qPCR.techReps))[1:11] #11 genes
qPCRBatch.qPCR.techReps

#calculate the mean of technical replicas - arithmetic mean of Cq
combinedTechReps <- combineTechReps(qPCRBatch.qPCR.techReps)
combinedTechReps

#compactly displaying the internal structure of a R object
str(exprs(combinedTechReps))
sampleNames(combinedTechReps)


#To calculate the value of the stability M:
#To say which the tissue and quantitative of the replicates
#Seeds+Leaves = 12 pools (replicates)
#Seeds (p1,p2,p3,p4,p5,p6) + leaves (p7,p8,p9,p10,p11,p12)

tissue <- as.factor(c(rep("seeds", 6), rep("leaves", 6)))

#Value of the stability M: 
res.p1 <- selectHKs(combinedTechReps[,tissue == "seeds"], method = "geNorm",
                    Symbols = featureNames(combinedTechReps),
                    minNrHKs = 2, trace = F, log = FALSE)

res.p2 <- selectHKs(combinedTechReps[,tissue == "leaves"], method = "geNorm",
                    Symbols = featureNames(combinedTechReps),
                    minNrHKs = 2, trace = F, log = FALSE)

#To do the rank if the genes most stables by sample
ranks <- data.frame(c(1, 1:10), res.p1$ranking, res.p2$ranking)
names(ranks) <- c("rank","seeds","leaves")
ranks

#PLOTS geNORM
#Line graph 
library(RColorBrewer)
mypalette <- brewer.pal(5, "Set1")
matplot(cbind(res.p1$meanM, res.p2$meanM), type = "b",
          ylab = "Average expression stability M",
          xlab = "Number of remaining control genes",
          axes = FALSE, pch = 7, col = mypalette,
          ylim = c(0.005, 0.05), lty = 1, lwd = 3)
axis(1, at = 1:9, labels = as.character(10:2))
axis(2, at = seq(0.005, 0.05, by = 0.01), labels = seq(0.005, 0.05, by = 0.01))
box()
abline(h = seq(0.2, 1.2, by = 0.2), lty = 2, lwd = 1, col = "grey")
legend("topright", legend = c("seeds","leaves"),
                    fill = mypalette)

#Bar graph
mypalette <- brewer.pal(6, "RdBu")
mypalette <- c("darkorange1","darkorange2", "darkorange3", 
               "springgreen4", "springgreen3", "springgreen2",
               "dodgerblue3", "dodgerblue2", "dodgerblue1")
barplot(cbind(res.p1$variation,res.p2$variation), 
          beside = TRUE,
          ylim=c(0,0.013777777),
          col = mypalette, space = c(0, 2),
          names.arg = c("Seeds","Leaves"),
          ylab = "Pairwise variation V")
legend("topright", legend = c("V9/10", "V8/9", "V7/8", "V6/7",
                               "V5/6", "V4/5", "V3/4", "V2/3"),
         fill = mypalette, ncol = 4)
abline(h = seq(0.05, 0.25, by = 0.05), lty = 2, col = "grey")
abline(h = 0.15, lty = 1, col = "black")


###################################################
### geNorm - First analyse: Acari vs. JS (citys) 
###################################################

library(ReadqPCR)
library(NormqPCR)

path <- system.file("exData", package = "NormqPCR")
qPCR.example.techReps <- file.path(path, "geNorm2.txt")
qPCRBatch.qPCR.techReps <- read.qPCR(qPCR.example.techReps)

rownames(exprs(qPCRBatch.qPCR.techReps))[1:11] #11 genes
qPCRBatch.qPCR.techReps

combinedTechReps <- combineTechReps(qPCRBatch.qPCR.techReps)
combinedTechReps

str(exprs(combinedTechReps))
sampleNames(combinedTechReps)

tissue <- as.factor(c(rep("SA", 3), rep("SJ", 3),
                      rep("LA", 3), rep("LJ", 3)))


res.SA <- selectHKs(combinedTechReps[,tissue == "SA"], method = "geNorm",
                    Symbols = featureNames(combinedTechReps),
                    minNrHKs = 2, trace = FALSE, log = FALSE)

res.SJ <- selectHKs(combinedTechReps[,tissue == "SJ"], method = "geNorm",
                    Symbols = featureNames(combinedTechReps),
                    minNrHKs = 2, trace = FALSE, log = FALSE)
res.LA <- selectHKs(combinedTechReps[,tissue == "LA"], method = "geNorm",
                    Symbols = featureNames(combinedTechReps),
                    minNrHKs = 2, trace = FALSE, log = FALSE)

res.LJ <- selectHKs(combinedTechReps[,tissue == "LJ"], method = "geNorm",
                    Symbols = featureNames(combinedTechReps),
                    minNrHKs = 2, trace = FALSE, log = FALSE)


ranks <- data.frame(c(1, 1:10), res.SA$ranking, 
                    res.SJ$ranking,
                    res.LA$ranking,
                    res.LJ$ranking)
names(ranks) <- c("rank","SA","SJ","LA","LJ")
ranks

library(RColorBrewer)
mypalette <- brewer.pal(5, "Set1")
matplot(cbind(res.SA$meanM, res.SJ$meanM, res.LA$meanM,  res.LJ$meanM),
        type = "b",
        ylab = "Average expression stability M",
        xlab = "Number of remaining control genes",
        axes = FALSE, pch = 7, col = mypalette,
        ylim = c(0, 0.05), lty = 1, lwd = 3)
axis(1, at = 1:9, labels = as.character(10:2))
axis(2, at = seq(0.005, 0.05, by = 0.01), labels = seq(0.005, 0.05, by = 0.01))
box()
abline(h = seq(0.2, 1.2, by = 0.2), lty = 2, lwd = 1, col = "grey")
legend("topright", legend = c("SA","SJ","LA","LJ"),
       fill = mypalette)



