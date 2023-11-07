library(ReadqPCR)
library(NormqPCR)
library(writexl)
library(dplyr)

######NORMPCR#######

#Place the dataset archive (.txt) in the normqPCR directory
#normqPCR directory: "C:/Users/daisy/AppData/Local/R/win-library/4.2/NormqPCR/exData"
#Realized two analyses: leaves vs. seeds ("dataset_geNorm.txt") and Acari vs. JS ("geNorm2.txt")

path <- system.file("exData", package = "NormqPCR")
dir()
qPCR.example.techReps <- file.path(path, "geNorm1_all.txt")
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

tissue <- as.factor(c(rep("CT4", 4), rep("MJ", 4),rep("SNP",4)))

#Value of the stability M: 
res.p1 <- selectHKs(combinedTechReps[,tissue == "CT4"], method = "geNorm",
                    Symbols = featureNames(combinedTechReps),
                    minNrHKs = 2, trace = F, log = FALSE)

res.p2 <- selectHKs(combinedTechReps[,tissue == "MJ"], method = "geNorm",
                    Symbols = featureNames(combinedTechReps),
                    minNrHKs = 2, trace = F, log = FALSE)

res.p3 <- selectHKs(combinedTechReps[,tissue == "SNP"], method = "geNorm",
                    Symbols = featureNames(combinedTechReps),
                    minNrHKs = 2, trace = F, log = FALSE)

###SERRAPILHEIRA ############
path <- system.file("exData", package = "NormqPCR")
qPCR.example.techReps <- file.path(path, "geNorm2_all.txt")
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


#To do the rank if the genes most stables by sample
ranks <- data.frame(c(1, 1:10), res.p1$ranking, res.p2$ranking,res.p3$ranking,
                    res.SA$ranking, 
                    res.SJ$ranking,
                    res.LA$ranking,
                    res.LJ$ranking)
names(ranks) <- c("rank","CT4","MJ","SNP", "SA", "SJ","LA","LJ")
ranks


#PLOTS geNORM
#Bar graph
mypalette <- brewer.pal(9, "RdBu")

barplot(cbind(res.p1$variation,res.p2$variation,res.p3$variation,
              res.SA$variation,res.SJ$variation,res.LA$variation,res.LJ$variation), 
        beside = TRUE,
        ylim=c(0,0.100000),
        col = mypalette, space = c(0, 2),
        names.arg = c("CT","MJ","SNP", "SA", "SJ","LA","LJ"),
        ylab = "Pairwise variation V")
legend("topright", legend = c("V10/11","V9/10", "V8/9", "V7/8", "V6/7",
                              "V5/6", "V4/5", "V3/4", "V2/3"),
       fill = mypalette, ncol = 4)
abline(h = seq(0.05, 0.25, by = 0.05), lty = 2, col = "grey")
abline(h = 0.15, lty = 1, col = "black")