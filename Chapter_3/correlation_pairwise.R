getwd()
setwd("E:/Doc/Cap 3 - GR_Evelu/Resultados_PCRs/tratamentos/Scripts/all_700")
getwd()
dir()

Cts <- read.table("Bestkeeper_all.txt")
Cts
str(Cts)

#Medindo as correlações (sem teste):
cor(Cts)#default=pearson
?cor

#Olhando para as correlações 
plot(Cts)

#Criando um objeto para as relacões
result.cor2 <- cor(Cts)
result.cor2

#salvar o data.frame criado como uma tabela
library(writexl)
dataframe <- data.frame(result.cor2)
write_xlsx(dataframe,
           path= 
             "D:/Doc/Cap 3 - GR_Evelu/Resultados_PCRs/tratamentos/Scripts/all_700/result.cor.xlsx")
#write.csv(result.cor2, file = "result.cor_pairwise.csv", row.names = TRUE)


###Gr?fico 1
#install.packages("ggcorrplot")
library(ggcorrplot)
library(ggplot2)
library(RColorBrewer)
library(RColorBrewer)
#Fazer matriz de p-value ao dado result.cor2
result.cor2
?cor_pmat
p.mat <- cor_pmat(result.cor2)
head(p.mat[, 1:11]) #matriz em todas as linhas, e coluna 1 a 11
#salvar o p-value
dataframe.pmat <- data.frame(p.mat)
write_xlsx(dataframe.pmat,
           path= 
             "D:/Doc/Cap 3 - GR_Evelu/Resultados_PCRs/tratamentos/Scripts/all_700/result.cor_pvalue.xlsx")

#mypalette <- brewer.pal(3, 'RdYlBu')
#mypalette <- brewer.pal(6, "Set1")
ggcorrplot(result.cor2, #objeto onde estão contidas as correla??es
           hc.order = T, #se TRUE ordena a matriz em fun??o dos valores de correla??o
           type = "lower", #mostra apenas a diagonal inferior
           sig.level=0.05,
           ggtheme = ggplot2::theme_gray,
           #p.mat = p.mat,
           #insig = "blank",
           digits = 2,
           legend.title = "Correlation \n coefficient",
           outline.col = "white",#titulo da legenda,
           lab = TRUE, #mostrar legenda
           lab_size = 2, #tamanho da legenda
           method = "square") #mostrando os resultados em circulos coloridos
           #colors = c("#fee6ce","#fdae6b","#e6550d"))
           #olors=mypalette)
           #theme_linedraw() #coloca um box em volta do grafico

?ggcorrplot
