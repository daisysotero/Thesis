getwd()
setwd("E:/Doc/Cap 3 - GR_Evelu/Figures/F4")
getwd()
dir()

Cts <- read.table("dataset_Bestkeeper.txt")
Cts
str(Cts)

#Measuring the correlations (no tests statistics):
cor(Cts)#default=pearson
?cor

#Looking for correlations 
plot(Cts)

#Creating an object for relations
result.cor2 <- cor(Cts)
result.cor2

#save the created data.frame as a table
library(writexl)
dataframe <- data.frame(result.cor2)
write_xlsx(dataframe,
           path= 
             "C:/Users/daisy/Desktop/housekeeping/ctrlGene-geNorm+Bestkeeper/result.cor_pairwise.xlsx")
#write.csv(result.cor2, file = "result.cor_pairwise.csv", row.names = TRUE)


###Graph 1
#install.packages("ggcorrplot")
library(ggcorrplot)
library(ggplot2)
library(RColorBrewer)

#Make a p-value array of the result.cor2 data
result.cor2
?cor_pmat
p.mat <- cor_pmat(result.cor2)
head(p.mat[, 1:11]) #matrix in all rows and column 1 to 11
#save the p-value
dataframe.pmat <- data.frame(p.mat)
write_xlsx(dataframe.pmat,
           path= 
             "C:/Users/daisy/Desktop/housekeeping/ctrlGene-geNorm+Bestkeeper/result.cor_pvalue.xlsx")

#mypalette <- brewer.pal(3, 'RdYlBu')
ggcorrplot(result.cor2, #object where the correlations are contained
           hc.order = TRUE, #if TRUE orders the matrix according to the correlation values
           type = "lower", #show only the lower diagonal
           sig.level=0.05,
           #p.mat = p.mat,
           digits = 2,
           legend.title = "Correlation coefficient",
           outline.col = "black",# caption title,
           lab = TRUE, #show caption
           lab_size = 3, #subtitle size
           method = "square", #showing the results in colored circles
           colors = c("dodgerblue4", "white", "orangered2"))
           #colors=mypalette)
          #ggtheme = theme_linedraw) #put a box around the graph




