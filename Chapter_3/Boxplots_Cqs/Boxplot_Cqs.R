getwd() 
setwd("E:/Doc/Cap 3 - GR_Evelu/Figures/F2")
dir()
#install.packages("wesanderson")
library(ggplot2)
library(wesanderson)
library(readxl)

box <- read.table("dataset_boxplot.txt", header = TRUE, sep = "\t", dec = ".")

#########INDIVIDUAL BOX########
ggplot(box, aes(x=Detector, y=Cq, fill=Detector)) +
  stat_boxplot(geom = "errorbar", width = 0.3)+
  geom_boxplot(alpha = 1,        # Transparency
               color = 1,          # Border color
               outlier.colour = "#707070cc",
               outlier.shape = 21, size=0.4)+
  
  labs(x="Candidates genes", y = "Cq values")+
  #geom_jitter()+
  scale_fill_brewer(palette="Paired")+theme_minimal()
?geom_boxplot

#########BOX BY CITY########

ggplot(box, aes(x=Detector, y=Cq,fill=city)) +
  stat_boxplot(geom = "errorbar", width = 0.7)+
  geom_boxplot(color = 1,outlier.colour = "#707070cc",
               outlier.shape = 21, size=0.3)+
  labs(x="Candidates genes", y = "Cq values")+
  theme_minimal()

#########BOXPLOT BY PLANT STRUCTURE########

ggplot(box, aes(x=Detector, y=Cq,fill=organ)) +
  stat_boxplot(geom = "errorbar", width = 0.7)+
  geom_boxplot(color = 1,outlier.colour = "#707070cc",
               outlier.shape = 21, size=0.3)+
  labs(x="Candidates genes", y = "Cq values")+
  scale_fill_brewer(palette="Dark2")+
  theme_minimal()

