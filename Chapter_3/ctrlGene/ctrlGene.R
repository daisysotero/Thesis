#install.packages("ctrlGene")

#Call the directory named "library" from the desired package
library(ctrlGene)


getwd() #See which directory you are in
#Add the directory desired
setwd("E:/Doc/Cap 3 - GR_Evelu/Scripts/Chapter_3/ctrlGene")
getwd()
dir() #See which paste is in the directory

#specify the file and give a variable
expression <- read.table("dataset_Bestkeeper.txt")
expression

#analyse: Bestkeeper
bestKeeper(expression, ctVal = TRUE)

#Analyzes genes versus BestKeeper index
bki(expression, ctVal = TRUE)

#Calculates descriptive statistics
cpSta(expression, ctVal = TRUE)

#geNorm Ranks genes
geNorm(expression, genes = data.frame(Genes = character(0), Avg.M =
                                        numeric(0)), ctVal = T)

#plotM Plots average M of remaining genes
x=geNorm(expression,ctVal=T)
plotM(x)

#plotV Plots V(n+1/n) values
Vs1=pairwiseV(expression,ctVal=T)
plotV(Vs1)

#geNorm2 Ranks genes
geNorm2(expression, genes = data.frame(Genes = character(0), Avg.M =
                                         numeric(0)), ctVal = TRUE)

#measureM Calculates measure M
measureM(expression, ctVal = TRUE)

#pairwiseV Calculates V(n+1/n) values
pairwiseV(expression, ctVal = TRUE)

#pearsonCor Analyzes pair-wise correlation
pearsonCor(expression, ctVal = TRUE)



