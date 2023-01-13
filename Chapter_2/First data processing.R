#install.packages("writexl")
#install.packages("ggplot2")
#install.packages("dplyr")

library(writexl)
library(ggplot2)
library(dplyr)

getwd()
setwd("E:/Doc/Cap 2/Analise_HPLC/RESULTADOS_BRUTOS/UV/CONTROLE/24h")
getwd()

dir()

##############################################
#PROCESSADO_TOTAL_280_SOMA - Example:UV
##############################################

# Initial processing of raw data (.arw) with branco archive data
X <- read.csv("E:/Doc/Cap 2/Analise_HPLC/RESULTADOS_BRUTOS/UV/CONTROLE/24h/BRANCO 1.arw", sep = "\t")

#Remove lines up to 2.5 min (RT)
dados<-X[1503:29997,]

#Remove columns of the 220-400 nm (wavelength)
dadosA<-dados[,c(1,11:163)]

#Fisrt step -> Save this data (total) in .xlsx
write_xlsx(dadosA,
           path= 
             "E:/Doc/Cap 2/Analise_HPLC/RESULTADOS_BRUTOS_PROCESSADOS/ABSORBANCIA/UV/CONTROLE/24h/PROCESSADO_PARA_SUBTRAIR/PROCESSADO_TOTAL/BRANCO 1.xlsx")

#Two step -> Save only Wavelength 280 nm data in .xlsx
dados1 <- dadosA[, c("Wavelength","X280.8696")]
write_xlsx(dados1, 
           path= 
             "E:/Doc/Cap 2/Analise_HPLC/RESULTADOS_BRUTOS_PROCESSADOS/ABSORBANCIA/UV/CONTROLE/24h/PROCESSADO_PARA_SUBTRAIR/PROCESSADO_280nm/BRANCO 1.xlsx")

#Three step -> Save the data summing all wavelengths in .xlsx
dados_somados <- dadosA %>%
  rowwise() %>%
  mutate(sum_var = sum(c_across(2:154)), .keep = "unused") 
write_xlsx(dados_somados, 
           path=
             "E:/Doc/Cap 2/Analise_HPLC/RESULTADOS_BRUTOS_PROCESSADOS/ABSORBANCIA/UV/CONTROLE/24h/PROCESSADO_PARA_SUBTRAIR/PROCESSADO_SOMA/BRANCO 1.xlsx")

##############################################

# Initial processing of raw data (.arw) with trated archive data -> control (leaves non submitted a UV in 24h)
X <- read.csv("E:/Doc/Cap 2/Analise_HPLC/RESULTADOS_BRUTOS/UV/CONTROLE/24h/FCUV241.1.arw", sep = "\t")
dados<-X[1503:29997,]
dadosA<-dados[,c(1,11:163)]
write_xlsx(dadosA,
           path= 
             "E:/Doc/Cap 2/Analise_HPLC/RESULTADOS_BRUTOS_PROCESSADOS/ABSORBANCIA/UV/CONTROLE/24h/PROCESSADO_PARA_SUBTRAIR/PROCESSADO_TOTAL/FCUV241.1.xlsx")

dados1 <- dadosA[, c("Wavelength","X280.8696")]
write_xlsx(dados1, 
           path= 
             "E:/Doc/Cap 2/Analise_HPLC/RESULTADOS_BRUTOS_PROCESSADOS/ABSORBANCIA/UV/CONTROLE/24h/PROCESSADO_PARA_SUBTRAIR/PROCESSADO_280nm/FCUV241.1.xlsx")

dados_somados <- dadosA %>%
  rowwise() %>%
  mutate(sum_var = sum(c_across(2:154)), .keep = "unused") 
write_xlsx(dados_somados, 
           path=
             "E:/Doc/Cap 2/Analise_HPLC/RESULTADOS_BRUTOS_PROCESSADOS/ABSORBANCIA/UV/CONTROLE/24h/PROCESSADO_PARA_SUBTRAIR/PROCESSADO_SOMA/FCUV241.1.xlsx")


##############################################

# Initial processing of raw data (.arw) with trated archive data -> Treated  (leaves submitted in UV 24h)
X <- read.csv("E:/Doc/Cap 2 - Tratadas_HPLC_Evelu/Analise_HPLC/RESULTADOS_BRUTOS/UV/TRATADO/24h/FUV241.1.arw", sep = "\t")
dados<-X[1503:29997,]
dadosA<-dados[,c(1,11:163)]
write_xlsx(dadosA,
           path= 
             "E:/Doc/Cap 2 - Tratadas_HPLC_Evelu/Analise_HPLC/RESULTADOS_PROCESSADOS/UV/TRATADO/24h/TOTAL/FUV241.1.xlsx")

dados1 <- dadosA[, c("Wavelength","X280.8696")]
write_xlsx(dados1, 
           path= 
             "E:/Doc/Cap 2 - Tratadas_HPLC_Evelu/Analise_HPLC/RESULTADOS_PROCESSADOS/UV/TRATADO/24h/280nm/FUV241.1.xlsx")

dados_somados <- dadosA %>%
  rowwise() %>%
  mutate(sum_var = sum(c_across(2:154)), .keep = "unused") 
write_xlsx(dados_somados, 
           path=
             "E:/Doc/Cap 2 - Tratadas_HPLC_Evelu/Analise_HPLC/RESULTADOS_PROCESSADOS/UV/TRATADO/24h/SOMA/FUV241.1.xlsx")
