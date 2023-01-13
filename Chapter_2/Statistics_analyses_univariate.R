#1. Select working directory
#2. Visualize data distribution/density (qq-plot, histogram, boxplot, line graph)
#3. homogeneity test
#4. Normality test
#5. Statistical test

#######################################

#1. Select working directory
getwd() 
setwd("E:/Doc/Cap 2 - Tratadas_HPLC_Evelu/Analise_HPLC/RESULTADOS_PROCESSADOS/UV") 
dir() 

data.uv <- read.table("analysis_280_uv.txt", header = T, sep = "\t")
dim(data.uv) 
View(data.uv)
summary(data.uv)
str(data.uv)

data.uv$Group <- as.factor(data.uv$Group) 
data.uv$Class <- as.factor(data.uv$Class)
data.uv$Replicate <- as.factor(data.uv$Replicate)
summary(data.uv) 
str(data.uv)

#2. Visualize data 

library(ggpubr)
library(cowplot)

#Q-Q plot
qq.leavesCT24 <- data.uv [1:5,3:4]
qq.leavesTR24 <- data.uv [6:10,3:4]
qq.rootsCT24 <- data.uv [11:15,3:4]
qq.rootsTR24 <- data.uv [16:19,3:4]
qq.leavesCT48 <- data.uv [20:24,3:4]
qq.leavesTR48 <- data.uv [25:29,3:4]
qq.rootsCT48 <- data.uv [30:34,3:4]
qq.rootsTR48 <- data.uv [35:39,3:4]

LCT24 <- ggqqplot(qq.leavesCT24, x = "Absorbance",
                  color = "Group", 
                  palette = c("#00979299"),
                  ggtheme = theme_pubclean())


LTR24 <- ggqqplot(qq.leavesTR24, x = "Absorbance",
                  color = "Group", 
                  palette = c("#66cd00ff"),
                  ggtheme = theme_pubclean())


RCT24 <- ggqqplot(qq.rootsCT24, x = "Absorbance",
                  color = "Group", 
                  palette = c("#efda0596"),
                  ggtheme = theme_pubclean())

RTR24 <- ggqqplot(qq.rootsTR24, x = "Absorbance",
                  color = "Group", 
                  palette = c("#8b7355ff"),
                  ggtheme = theme_pubclean())

LCT48 <- ggqqplot(qq.leavesCT48, x = "Absorbance",
                  color = "Group", 
                  palette = c("#009792fd"),
                  ggtheme = theme_pubclean())


LTR48 <- ggqqplot(qq.leavesTR48, x = "Absorbance",
                  color = "Group", 
                  palette = c("#006400ff"),
                  ggtheme = theme_pubclean())


RCT48 <- ggqqplot(qq.rootsCT48, x = "Absorbance",
                  color = "Group", 
                  palette = c("#fcd000ff"),
                  ggtheme = theme_pubclean())

RTR48 <- ggqqplot(qq.rootsTR48, x = "Absorbance",
                  color = "Group", 
                  palette = c("#8b4513ff"),
                  ggtheme = theme_pubclean())

plot_grid(LCT24, LTR24, RCT24, RTR24, LCT48, LTR48, RCT48, RTR48)


#Boxplot

#All groups
levels(data.uv$Group)
data.uv$Group <- factor(data.uv$Group,
                        labels=c("Leaves CT 24h", "Leaves 24h", "Roots CT 24h", "Roots 24h", 
                                 "Leaves CT 48h", "Leaves 48h", "Roots CT 48h", "Roots 48h"))
levels(data.uv$Group)
boxplot(data.uv$Absorbance~data.uv$Group, ylab="Absorbance in 280 nm", 
        xlab="",col=c("#00979299", "#66cd00ff", 
                      "#efda0596","#8b7355ff",
                      "#009792fd", "#006400ff", 
                      "#fcd000ff","#8b4513ff"),medcol="#FFFFFF",
        cex.axis=1,cex.lab=1)

#Separated groups
getwd() 
dir()
table <- read.table("peak_number_area.txt", 
                   header = T, sep = "\t")


str(table)
table$peak_number <- as.numeric(table$peak_number)
table$Replicate <- as.factor(table$Replicate)
table$Class <- as.factor(table$Class)
table$Replicate <- as.factor(table$Replicate)


library(ggplot2)
library(patchwork)
library(ggsignif)

f1 <- ggplot(table, aes(x=organ, y=abs, fill=organ))+geom_boxplot()+
  geom_point(size=1)+theme(text = element_text(size = 13, color= "black"))+
  scale_fill_manual(values = c("#9add58ff","#ff9531ff"))+
  theme_bw()+
  geom_signif(comparisons = list(c("Leaves", "Roots")),
              teste="t.test", tip_length = 0.015, size = 0.5, 
              textsize = 2, map_signif_level = T)+
  xlab(NULL)+
  stat_summary(fun = "mean", geom = "point", shape = 8,
               size = 2, color = "white")

t.test(abs ~ organ, table, var.equal=T)

f2 <- ggplot(table, aes(x=organ, y=peak_number, fill=organ))+geom_boxplot()+
  geom_point(size=1)+theme(text = element_text(size = 13, color= "black"))+
  scale_fill_manual(values = c("#9add58ff","#ff9531ff"))+
  theme_bw()+
  geom_signif(comparisons = list(c("Leaves", "Roots")),
              teste="t.test", tip_length = 0.015, size = 0.5, 
              textsize = 2, map_signif_level = T)+
  xlab(NULL)+
  stat_summary(fun = "mean", geom = "point", shape = 8,
               size = 2, color = "white")

t.test(peak_number ~ organ, table, var.equal=T)

f3 <- ggplot(table, aes(x=time, y=abs, fill=time))+geom_boxplot()+
  geom_point(size=1)+theme(text = element_text(size = 13, color= "black"))+
  scale_fill_manual(values = c("#00979299","#fcd000ff"))+
  theme_bw()+
  geom_signif(comparisons = list(c("24h", "48h")),
              teste="t.test", tip_length = 0.015, size = 0.5, 
              textsize = 2, map_signif_level = TRUE)+
  xlab(NULL)+
  stat_summary(fun = "mean", geom = "point", shape = 8,
               size = 2, color = "white")


t.test(abs ~ time, table, var.equal=T)

f4 <- ggplot(table, aes(x=time, y=peak_number, fill=time))+geom_boxplot()+
  geom_point(size=1)+theme(text = element_text(size = 13, color= "black"))+
  scale_fill_manual(values = c("#00979299","#fcd000ff"))+
  theme_bw()+
  geom_signif(comparisons = list(c("24h", "48h")),
              teste="t.test", tip_length = 0.015, size = 0.5, 
              textsize = 2, map_signif_level = T)+
  xlab(NULL)+
  stat_summary(fun = "mean", geom = "point", shape = 8,
               size = 2, color = "white")

t.test(peak_number ~ time, table, var.equal=T) #*

f5 <- ggplot(table, aes(x=c_uv, y=abs, fill=c_uv))+geom_boxplot()+
  geom_point(size=1)+theme(text = element_text(size = 13, color= "black"))+
  scale_fill_manual(values = c("#F2F2F2","#BE8084"))+
  theme_bw()+
  geom_signif(comparisons = list(c("Control", "UV")),
              teste="t.test", tip_length = 0.015, size = 0.5, 
              textsize = 2, map_signif_level = T)+
  xlab(NULL)+
  stat_summary(fun = "mean", geom = "point", shape = 8,
               size = 2, color = "white")


t.test(abs ~ c_uv, table, var.equal=T)

f6 <- ggplot(table, aes(x=c_uv, y=peak_number, fill=c_uv))+geom_boxplot()+
  geom_point(size=1)+theme(text = element_text(size = 13, color= "black"))+
  scale_fill_manual(values = c("#F2F2F2","#BE8084"))+
  theme_bw()+
  geom_signif(comparisons = list(c("Control", "UV")),
              teste="t.test", tip_length = 0.015, size = 0.5, 
              textsize = 2, map_signif_level = T)+
  xlab(NULL)+
  stat_summary(fun = "mean", geom = "point", shape = 8,
               size = 2, color = "white")

t.test(peak_number ~ c_uv, table, var.equal=T)


(f1 + f2)/(f3 + f4) / (f5 + f6)
dev.off()


#Line graph - distribution/density
#test scales
plot(c(0,900), c(0,0.010), xlab="Absorbance", ylab="Densidade", type="n", 
     cex.axis=1, cex.lab=1.1, main="")

#plot by group - 24h
lines(density(data.uv$Absorbance[data.uv$Group=="Leaves CT 24h"]),col="#00979299")
lines(density(data.uv$Absorbance[data.uv$Group=="Leaves 24h"]),col="#66cd00ff")
lines(density(data.uv$Absorbance[data.uv$Group=="Roots CT 24h"]),col="#efda0596")
lines(density(data.uv$Absorbance[data.uv$Group=="Roots 24h"]),col="#8b7355ff")

levels(data.uv$Group)
labs <- c("Leaves CT 24h", "Leaves 24h", "Roots CT 24h", "Roots 24h")
levels(data.uv$Group)
legend(locator(1), labs, lty=c(1), col=c("#00979299","#66cd00ff","#efda0596","#8b7355ff"), bty="n")
dev.off()

#plot by group - 48h
plot(c(0,800), c(0,0.008), xlab="Absorbance", ylab="Densidade", type="n", 
     cex.axis=1, cex.lab=1.1, main="")
lines(density(data.uv$Absorbance[data.uv$Group=="Leaves CT 48h"]),col="#009792fd")
lines(density(data.uv$Absorbance[data.uv$Group=="Leaves 48h"]),col="#006400ff")
lines(density(data.uv$Absorbance[data.uv$Group=="Roots CT 48h"]),col="#fcd000ff")
lines(density(data.uv$Absorbance[data.uv$Group=="Roots 48h"]),col="#8b4513ff")

levels(data.uv$Group)
labs <- c("Leaves CT 48h", "Leaves 48h", "Roots CT 48h", "Roots 48h")
levels(data.uv$Group)
legend(locator(1), labs, lty=c(1), col=c("#009792fd","#006400ff","#fcd000ff","#8b4513ff"), bty="n")
dev.off()


#3. Homogeneity test
library(car)

#One test
leveneTest(data.uv$Absorbance ~ data.uv$Group)
#Two test
bartlett.test(data.uv$Absorbance ~ data.uv$Group)


#4. Normality test
shapiro.test(data.uv$Absorbance[data.uv$Group=="Leaves CT 24h"])
shapiro.test(data.uv$Absorbance[data.uv$Group=="Leaves 24h"])
shapiro.test(data.uv$Absorbance[data.uv$Group=="Roots CT 24h"])
shapiro.test(data.uv$Absorbance[data.uv$Group=="Roots 24h"])

shapiro.test(data.uv$Absorbance[data.uv$Group=="Leaves CT 48h"])
shapiro.test(data.uv$Absorbance[data.uv$Group=="Leaves 48h"])
shapiro.test(data.uv$Absorbance[data.uv$Group=="Roots CT 48h"])
shapiro.test(data.uv$Absorbance[data.uv$Group=="Roots 48h"])

tapply(data.uv$Absorbance, data.uv$Group, mean) 
tapply(data.uv$Absorbance, data.uv$Group, median) 


#5. Statistical test
levels(data.uv$Group)
result.anova <- aov(data.uv$Absorbance ~ data.uv$Group)

#See better anova residuals
result.anova$residuals
qqnorm(result.anova$residuals)
qqline(result.anova$residuals, lty=2)
shapiro.test(result.anova$residuals)
leveneTest(result.anova$residuals, data.uv$Group)

#See results of anova
summary(result.anova)

#Post-hoc
#Duncan
library(DescTools)
PostHocTest(result.anova, method = "duncan")

#install.packages("agricolae")
library(agricolae)
result.anova <- aov(Absorbance ~ Group, data.uv)
DMRT = duncan.test(result.anova, "Group",  alpha = 0.05,
                   group = TRUE, console = TRUE)





