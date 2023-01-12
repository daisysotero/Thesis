
#Primeiro: Faz um direotio "normfinder", coloca o arquivo (r.NormOldStab5.txt)
#Segundo: Coloca esse direotio como diretorio de trabalho
          #Vai em: tools>global options>coloca o diretorio criado>ok
          #fecha o R e abre novamente, para seguir com as linhas abaixo.


#First: Make a directory "normfinder", place the file (r.NormOldStab5.txt)
#Second: Put this directory as working directory
  #Go to: tools>global options>place the created directory>ok
  # close R and open it again, to continue with the lines below.


source("r.NormOldStab5.txt")
Result=Normfinder("dataset_normfinder.txt")

#Result$Ordered: resultados dos grupos (folhas e sementes) juntos 
#Result$Ordered: results of groups (leaves and seeds) together
Result$Ordered 
#1a coluna: nome do gene
#2a coluna (GroupDif): é uma medida da diferença entre os grupos 
#3a coluna (GroupSD): é o desvio padrão comum dentro de um grupo (uma média ponderada das variâncias intragrupo)
#4a coluna (Estabilidade): contém a medida de estabilidade dada pela média dos termos na equação C. 

#Result$UnOrdered: resultados dos grupos (folhas e sementes) separados 
#Result$UnOrdered: results of separate groups (leaves and seeds)
Result$UnOrdered
#Esta tabela tem as mesmas colunas de antes e inclui os desvios padrão individuais
#para cada grupo (IGroupSD) e as diferenças individuais do grupo 

#Result$PairOfGenes: analise par a par
#Result$PairOfGenes: Analyze pair by pair
Result$PairOfGenes
#Para cada combinação de dois genes, é calculado o valor de estabilidade 
#A tabela produzida os nomes dos dois genes e o valor de Estabilidade. 
#A tabela contém apenas a combinação de genes para os quais o valor de 
#estabilidade, desde a primeira execução sem genes combinados, é inferior a 0,25
#(este último valor pode ser definido por pStabLim na chamada do Normfinder)


