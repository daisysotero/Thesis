#BARRAS fold - peak


library(readxl)
library(ggplot2)
library(RColorBrewer)

getwd() 
setwd("E:/Doc/Cap 2 - Tratadas_HPLC_Evelu/Analise_HPLC/RESULTADOS_PROCESSADOS/Results_area") 
dir() 

#fold_all <- read_xlsx("peak_number_area.xlsx", sheet = "fold_peak", col_names = TRUE)

fold_all <- read.table("fold_peak.txt", header = T, sep = "\t")

#1. barras simples - selecionar todos da caoluna Group

ggplot(fold_all, aes(x=Group, y=fold_log2))+ #label=fold_raw = #label - numero na barra
  geom_bar(stat = "identity", fill="blue", color="red", alpha=0.3)+
  #geom_label(size=0.3)+ #colocar os numeros na barra (se colocar label na primera linha)
  coord_flip() #deixar o gráfico vertical 

#2. barras simples - com preenchimento

ggplot(fold_all, aes(x=Group, y=fold_log2, fill=Treatment))+ #label=fold_raw = #label - numero na barra
  geom_bar(stat = "identity")+
  coord_flip()+ #deixar o gráfico vertical 
  theme_bw()+
  geom_hline(yintercept = 0, col="red", alpha=0.5)#colocar linha eixo Y
#geom_vline(xintercept = 1, col="red", alpha=0.5) #colocar linha eixo X

#Colocar ordem
theTable <- within(fold_all, 
                   fold_all$number <- factor(fold_all$number, 
                                                     levels=names(sort(table(fold_all$number)))))
#plotar nova ordem
ggplot(theTable, aes(x=fold_all$number, y=fold_log2, fill=Treatment))+
  coord_flip()+ #deixar o gráfico vertical 
  #label=fold_raw = #label - numero na barra
  geom_bar(stat = "identity", colour="black", size =0.3)+
  theme_bw(base_size = 9)+
  ylim(-0.5, 0.5)+
  geom_hline(yintercept = 0, col="red", alpha=0.5)+#colocar linha eixo Y
  #geom_vline(xintercept = 1, col="red", alpha=0.5) #colocar linha eixo X
  scale_x_discrete(labels=c("1" = "Leaves 50°C", "2" = "Roots 50°C", 
                            
                            "3" = "Leaves 24h", "4" = "Roots 24h", "5" = "Leaves 48h", "6" = "Roots 48h",
                            
                            "7" = "Leaves T1", "8" = "Leaves T2", "9" = "Leaves T3", "10" = "Roots T1", "11" = "Roots T2","12" = "Roots T3",
                            
                            "13" = "Leaves 2 days 1/4","14" = "Leaves 2 days 3/4","15" = "Roots 2 days 1/4","16"= "Roots 2 days 3/4 ",
                            "17"= "Leaves 4 days 1/4","18"= "Leaves 4 days 3/4", "19" = "Roots 4 days 1/4 ","20"= "Roots 4 days 3/4",
                            
                            "21"= "Leaves 2 days 0,25M", "22"= "Leaves 2 days 0,50M","23"= "Roots 2 days 0,25M","24"= "Roots 2 days 0,50M",
                            "25"= "Leaves 4 days 0,25M","26"= "Leaves 4 days 0,50M","27"= "Roots 4 days 0,25M","28"= "Roots 4 days 0,50M",
                            
                            "29" = "Leaves 2 days 25mg/mL", "30" = "Leaves 2 days 50mg/mL", "31" = "Roots 2 days 25mg/mL", "32" = "Roots 2 days 50mg/mL",
                            "33" = "Leaves 4 days 25mg/mL", "34" = "Leaves 4 days  50mg/mL", "35" = "Roots 4 days 25mg/mL", "36" = "Roots 4 days 50mg/mL ",
                            
                            "37" = "Leaves 2 days 40 uM", "38" = "Leaves 2 days 100_uM", "39" = "Roots 2 days 40 uM","40" = "Roots 2 days 100_uM ",
                            "41" = "Leaves 4 days 40 uM","42" = "Leaves 4 days 100_uM","43" = "Roots 4 days 40 uM","44"= "Roots 4 days 100_uM ",
                            
                            "45"= "Leaves 2 days 100 uM","46"= "Leaves 2 days 200 uM","47" = "Roots 2 days 100 uM","48"= "Roots 2 days 200 uM",
                            "49"= "Leaves 4 days 100 uM","50"= "Leaves 4 days 200 uM","51"= "Roots 4 days 100 uM","52"= "Roots 4 days 200 uM",
                            
                            "53"= "Leaves 2 days 1mM", "54"= "Leaves 2 days 2mM","55"= "Roots 2 days 1mM","56"= "Roots 2 days 2mM",
                            "57"= "Leaves 4 days 1mM","58"= "Leaves 4 days 2mM", "59"= "Roots 4 days 1mM","60"= "Roots 4 days 2mM"))+
  
  labs(x="Groups", y="Log2 Fold Change (peak number)")+
  
  scale_fill_manual(values=c("#ad6661ff", "#cbb647ff", "#fc8d62ff",
                             "#969e89ff", "#66c2a5ff", "#589ec9ff",
                             "#a6d854ff", "#8da0cbff", "#e668f3ff"))
  
  
#####################################

#BARRAS fold - peak number


library(readxl)
library(ggplot2)
library(RColorBrewer)

getwd() 
setwd("E:/Doc/Cap 2 - Tratadas_HPLC_Evelu/Analise_HPLC/RESULTADOS_PROCESSADOS/Results_area") 
dir() 

fold_all <- read_xlsx("peak_number_area.xlsx", 
                      sheet = "fold_area", col_names = TRUE)

#1. barras simples - selecionar todos da caoluna Group

ggplot(fold_all, aes(x=Group, y=fold_log2))+ #label=fold_raw = #label - numero na barra
  geom_bar(stat = "identity", fill="blue", color="red", alpha=0.3)+
  #geom_label(size=0.3)+ #colocar os numeros na barra (se colocar label na primera linha)
  coord_flip() #deixar o gráfico vertical 

#2. barras simples - com preenchimento

ggplot(fold_all, aes(x=Group, y=fold_log2, fill=Treatment))+ #label=fold_raw = #label - numero na barra
  geom_bar(stat = "identity")+
  coord_flip()+ #deixar o gráfico vertical 
  theme_bw()+
  geom_hline(yintercept = 0, col="red", alpha=0.5)#colocar linha eixo Y
#geom_vline(xintercept = 1, col="red", alpha=0.5) #colocar linha eixo X

#Colocar ordem
theTable <- within(fold_all, 
                   fold_all$number <- factor(fold_all$number, 
                                             levels=names(sort(table(fold_all$number)))))
#plotar nova ordem
ggplot(theTable, aes(x=fold_all$number, y=fold_log2, fill=Treatment))+
  coord_flip()+ #deixar o gráfico vertical 
  #label=fold_raw = #label - numero na barra
  geom_bar(stat = "identity", colour="black", size =0.3)+
  theme_bw(base_size = 9)+
  ylim(-2, 2)+
  geom_hline(yintercept = 0, col="red", alpha=0.5)+#colocar linha eixo Y
  #geom_vline(xintercept = 1, col="red", alpha=0.5) #colocar linha eixo X
  scale_x_discrete(labels=c("1" = "Leaves 50°C", "2" = "Roots 50°C", 
                            
                            "3" = "Leaves 24h", "4" = "Roots 24h", "5" = "Leaves 48h", "6" = "Roots 48h",
                            
                            "7" = "Leaves T1", "8" = "Leaves T2", "9" = "Leaves T3", "10" = "Roots T1", "11" = "Roots T2","12" = "Roots T3",
                            
                            "13" = "Leaves 2 days 1/4","14" = "Leaves 2 days 3/4","15" = "Roots 2 days 1/4","16"= "Roots 2 days 3/4 ",
                            "17"= "Leaves 4 days 1/4","18"= "Leaves 4 days 3/4", "19" = "Roots 4 days 1/4 ","20"= "Roots 4 days 3/4",
                            
                            "21"= "Leaves 2 days 0,25M", "22"= "Leaves 2 days 0,50M","23"= "Roots 2 days 0,25M","24"= "Roots 2 days 0,50M",
                            "25"= "Leaves 4 days 0,25M","26"= "Leaves 4 days 0,50M","27"= "Roots 4 days 0,25M","28"= "Roots 4 days 0,50M",
                            
                            "29" = "Leaves 2 days 25mg/mL", "30" = "Leaves 2 days 50mg/mL", "31" = "Roots 2 days 25mg/mL", "32" = "Roots 2 days 50mg/mL",
                            "33" = "Leaves 4 days 25mg/mL", "34" = "Leaves 4 days  50mg/mL", "35" = "Roots 4 days 25mg/mL", "36" = "Roots 4 days 50mg/mL ",
                            
                            "37" = "Leaves 2 days 40 uM", "38" = "Leaves 2 days 100_uM", "39" = "Roots 2 days 40 uM","40" = "Roots 2 days 100_uM ",
                            "41" = "Leaves 4 days 40 uM","42" = "Leaves 4 days 100_uM","43" = "Roots 4 days 40 uM","44"= "Roots 4 days 100_uM ",
                            
                            "45"= "Leaves 2 days 100 uM","46"= "Leaves 2 days 200 uM","47" = "Roots 2 days 100 uM","48"= "Roots 2 days 200 uM",
                            "49"= "Leaves 4 days 100 uM","50"= "Leaves 4 days 200 uM","51"= "Roots 4 days 100 uM","52"= "Roots 4 days 200 uM",
                            
                            "53"= "Leaves 2 days 1mM", "54"= "Leaves 2 days 2mM","55"= "Roots 2 days 1mM","56"= "Roots 2 days 2mM",
                            "57"= "Leaves 4 days 1mM","58"= "Leaves 4 days 2mM", "59"= "Roots 4 days 1mM","60"= "Roots 4 days 2mM"))+
  
  labs(x="Groups", y="Log2 Fold Change (area)")+
  
  scale_fill_manual(values=c("#ad6661ff", "#cbb647ff", "#fc8d62ff",
                             "#969e89ff", "#66c2a5ff", "#589ec9ff",
                             "#a6d854ff", "#8da0cbff", "#e668f3ff"))

