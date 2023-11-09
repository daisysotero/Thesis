#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt 
from scipy.stats import f_oneway
from scipy.stats import tukey_hsd
from scipy import stats

#Salvar string em um nome
path=r'E:\Doc\Cap 3 - GR_Evelu\Resultados_PCRs\Validacao-GR\Validação\qpcr_python'
excel_file = "deltadeltaaCq.xlsx"
#juntar as strings e fazer uma string unica
arquivo = os.path.join(path, excel_file)

#FAZER A MEDIA DAS REPLICATAS TÉCNICAS -> APENAS 1 VALOR POR GRUPO BIOLÓGICO 
#sample = pools

numero_de_abas=3

#Criar data frame a partir das abas do excel
dfchi = pd.read_excel(arquivo, sheet_name=xls.sheet_names[0], engine='openpyxl')
dfcsf_chi = pd.read_excel(arquivo, sheet_name=xls.sheet_names[1], engine='openpyxl')
dfnle_chi = pd.read_excel(arquivo, sheet_name=xls.sheet_names[2], engine='openpyxl')

#para uma variavel que vai alternar de 0 a 2 -> vai assumir o valor 0,1,2
for k in range(numero_de_abas):
    if k==0: #vai ter por que começa em zero, então vai selecionar
        selecionar_aba=dfchi
    elif k == 1:
        selecionar_aba=dfcsf_chi
    elif k ==2:
        selecionar_aba=dfnle_chi

    lista_sample=[] #criei uma lista em branco
    lista_sample.append(selecionar_aba['sample'][0]) #anotei na lista a primeira informação - p1
    
    #criar uma lista de todos os nomes UNICOS
    for i in range (1,len(selecionar_aba)): #1 por que o a linha zero ja foi salva
        chave=0
        nome=selecionar_aba['sample'][i] #colocar todos os "p1" na variavel nome
        for j in range (len(lista_sample)): #p1
            if nome == lista_sample[j]:# primeiro elemento de lista -> p1
                chave=1
        if chave ==0:
            lista_sample.append(nome)
        #print(dfchi['sample'][i])
    print(lista_sample)
    
    #após criar lista com nomes, queremos ter uma matriz para colocar as medias dos valores Cq
    if k==0:
        media=np.zeros((numero_de_abas,len(lista_sample))) #criar uma matriz com n numeros zeros 
                                                #(no meu caso, 12 -> p1-p12 para cada aba)
    #Fazer as medias dos Cqs e colocar na matriz
    for i in range (len(lista_sample)):
        lista_ct=[] #lista vazia para guardar os Cts -> criar 12 listas, sempre zerando elas

        for j in range(len(selecionar_aba)):
            nome=selecionar_aba['sample'][j]
         
            if nome==lista_sample[i]:
                lista_ct.append(selecionar_aba['ct'][j])
    #Apos anostar os CTs, agora precisamos fazer a média
        #print(lista_ct)
        media[k][i]=np.average(lista_ct)
    print(media[k])
    
    
print(media[0],xls.sheet_names[0])
print(media[1],xls.sheet_names[1])
print(media[2],xls.sheet_names[2])

###DCq: RG1 -> CSF
deltaCq_csf=np.zeros(len(media[0]))

#2.Delta Cq
for i in range (len(media[0])):
    deltaCq_csf[i]=media[0][i]-media[1][i] 
    print(i,lista_sample[i], media[1][i])
print(deltaCq_csf)

###DCq: RG2 -> NLE
deltaCq_nle=np.zeros(len(media[0]))

#2.Delta Cq
for i in range (len(media[0])):
    deltaCq_nle[i]=media[0][i]-media[2][i] 
    print(i,lista_sample[i], media[2][i])
print(deltaCq_nle)


###Escolher as amotras controles (calibrador = "1" -> escolhi p1, p2, p3 - Seeds Acari)
###### CSF #######

#Criar uma lista com p1,p2,p3 #lista_sample=p1-p12
controle_csf=[lista_sample[0],lista_sample[1],lista_sample[2]] 
#Criar uma lista no tamanho de 3 com zero (0,0,0)
lista_controle_csf=np.zeros(len(controle_csf))

#fazer a media do controle
for i in range (len(controle_csf)):
    for j in range (len(lista_sample)): #varia de 0 a 11
        if controle_csf[i]==lista_sample[j]: 
            lista_controle_csf[i]=deltaCq_csf[j] #anota o DCq na lista #não é append pq criei com np.zeros e não []
            
#fazer a media desses numeros
media_controle_csf=np.average(lista_controle_csf)


###### NLE #######
#Criar uma lista com p1,p2,p3 #lista_sample=p1-p12
controle_nle=[lista_sample[0],lista_sample[1],lista_sample[2]] 
#Criar uma lista no tamanho de 3 com zero (0,0,0)
lista_controle_nle=np.zeros(len(controle_nle))

#fazer a media do controle
for i in range (len(controle_nle)):
    for j in range (len(lista_sample)): #varia de 0 a 11
        if controle_nle[i]==lista_sample[j]: 
            lista_controle_nle[i]=deltaCq_nle[j] #anota o DCq na lista #não é append pq criei com np.zeros e não []
            
#fazer a media desses numeros
media_controle_nle=np.average(lista_controle_nle)


print(media_controle_csf)
print(media_controle_nle)


###DDCq_csf
ddCq_csf=np.zeros(len(deltaCq_csf))
for i in range (len(deltaCq_csf)):
    ddCq_csf[i]=deltaCq_csf [i]-media_controle_csf

#DDCq_nle
ddCq_nle=np.zeros(len(deltaCq_nle))
for i in range (len(deltaCq_nle)):
    ddCq_nle[i]=deltaCq_nle[i]-media_controle_nle

print(ddCq_csf)
print(ddCq_nle)

for i in range (len(lista_sample)):
    print(i,lista_sample[i])
    
###Lista dos numeros do DDcq de cada grupo -> para depois plotar
#### CSF ####
seeds_acari_csf=[lista_sample[0],lista_sample[1],lista_sample[2]]
seeds_jardim_csf=[lista_sample[3],lista_sample[4],lista_sample[5]]
leaves_acari_csf=[lista_sample[6],lista_sample[7],lista_sample[8]]
leaves_jardim_csf=[lista_sample[9],lista_sample[10],lista_sample[11]]

lista_seeds_acari_csf=np.zeros(len(controle_csf))
lista_seeds_jardim_csf=np.zeros(len(controle_csf))
lista_leaves_acari_csf=np.zeros(len(controle_csf))
lista_leaves_jardim_csf=np.zeros(len(controle_csf))

for i in range (len(controle_csf)):
    for j in range (len(lista_sample)):
        if seeds_acari_csf[i]==lista_sample[j]:
            lista_seeds_acari_csf[i]=ddCq_csf[j]
        
        if seeds_jardim_csf[i]==lista_sample[j]:
            lista_seeds_jardim_csf[i]=ddCq_csf[j]
            
        if leaves_acari_csf[i]==lista_sample[j]:
            lista_leaves_acari_csf[i]=ddCq_csf[j]
            
        if leaves_jardim_csf[i]==lista_sample[j]:
            lista_leaves_jardim_csf[i]=ddCq_csf[j]
            

#### NLE ####

seeds_acari_nle=[lista_sample[0],lista_sample[1],lista_sample[2]]
seeds_jardim_nle=[lista_sample[3],lista_sample[4],lista_sample[5]]
leaves_acari_nle=[lista_sample[6],lista_sample[7],lista_sample[8]]
leaves_jardim_nle=[lista_sample[9],lista_sample[10],lista_sample[11]]

lista_seeds_acari_nle=np.zeros(len(controle_csf))
lista_seeds_jardim_nle=np.zeros(len(controle_csf))
lista_leaves_acari_nle=np.zeros(len(controle_csf))
lista_leaves_jardim_nle=np.zeros(len(controle_csf))

for i in range (len(controle_nle)):
    for j in range (len(lista_sample)):
        if seeds_acari_nle[i]==lista_sample[j]:
            lista_seeds_acari_nle[i]=ddCq_nle[j]
        
        if seeds_jardim_nle[i]==lista_sample[j]:
            lista_seeds_jardim_nle[i]=ddCq_nle[j]
            
        if leaves_acari_nle[i]==lista_sample[j]:
            lista_leaves_acari_nle[i]=ddCq_nle[j]
            
        if leaves_jardim_nle[i]==lista_sample[j]:
            lista_leaves_jardim_nle[i]=ddCq_nle[j]

            
#2^(-DDCq) + salvar esse resultado
### CSF ###
expressao_seeds_acari_csf=2**(-lista_seeds_acari_csf)
expressao_seeds_jardim_csf=2**(-lista_seeds_jardim_csf)
expressao_leaves_acari_csf=2**(-lista_leaves_acari_csf)
expressao_leaves_jardim_csf=2**(-lista_leaves_jardim_csf)

### NLE ###
expressao_seeds_acari_nle=2**(-lista_seeds_acari_nle)
expressao_seeds_jardim_nle=2**(-lista_seeds_jardim_nle)
expressao_leaves_acari_nle=2**(-lista_leaves_acari_nle)
expressao_leaves_jardim_nle=2**(-lista_leaves_jardim_nle)

#printar o resultado
#CSF
print(expressao_seeds_acari_csf)
print(expressao_seeds_jardim_csf)
print(expressao_leaves_acari_csf)
print(expressao_leaves_jardim_csf)
#NLE
print(expressao_seeds_acari_nle)
print(expressao_seeds_jardim_nle)
print(expressao_leaves_acari_nle)
print(expressao_leaves_jardim_nle)

##### FAZER UMA LISTA PARA COLOCAR OS VALORES DE 2^-DDCq -> 6 valores por lista (3 csf+3nle) ####

lista_expressao_seeds_acari=[]
lista_expressao_seeds_jardim=[]
lista_expressao_leaves_acari=[]
lista_expressao_leaves_jardim=[]

for i in range(3):
    lista_expressao_seeds_acari.append(expressao_seeds_acari_csf[i])
    lista_expressao_seeds_acari.append(expressao_seeds_acari_nle[i])
    
    lista_expressao_seeds_jardim.append(expressao_seeds_jardim_csf[i])
    lista_expressao_seeds_jardim.append(expressao_seeds_jardim_nle[i])
        
    lista_expressao_leaves_acari.append(expressao_leaves_acari_csf[i])
    lista_expressao_leaves_acari.append(expressao_leaves_acari_nle[i])
    
    lista_expressao_leaves_jardim.append(expressao_leaves_jardim_csf[i])
    lista_expressao_leaves_jardim.append(expressao_leaves_jardim_nle[i])

print(lista_expressao_seeds_acari)
print(lista_expressao_seeds_jardim)
print(lista_expressao_leaves_acari)
print(lista_expressao_leaves_jardim)

#Média 2^(-DDCq) -> 1. média entre as replicatas do GR1 (CSF) e GR2 (NLE)
media_seeds_acari=np.average(lista_expressao_seeds_acari)
media_seeds_jardim=np.average(lista_expressao_seeds_jardim)
media_leaves_acari=np.average(lista_expressao_leaves_acari)
media_leaves_jardim=np.average(lista_expressao_leaves_jardim)

std_seeds_acari_csf=np.std(lista_expressao_seeds_acari)/np.sqrt(6)
std_seeds_jardim_csf=np.std(lista_expressao_seeds_jardim)/np.sqrt(6)
std_leaves_acari_csf=np.std(lista_expressao_leaves_acari)/np.sqrt(6)
std_leaves_jardim_csf=np.std(lista_expressao_leaves_jardim)/np.sqrt(6)


fig, ax = plt.subplots()

groups = ['Seeds \nAcari', 'Seeds \nJardim', 'Leaves \nAcari', 'Leaves \nJardim']
contagem = [media_seeds_acari,media_seeds_jardim,media_leaves_acari,media_leaves_jardim]
error=[std_seeds_acari_csf,std_seeds_jardim_csf,std_leaves_acari_csf,std_leaves_jardim_csf]
bar_colors = ['#C55A11', '#F4B183', '#385723', '#A9D18E']
ax.bar(groups, contagem, yerr=error, capsize=3.5,align='center', color=bar_colors)

ax.set_ylabel('Relative expression')

#plt.savefig(r'E:\Doc\Cap 3 - GR_Evelu\Resultados_PCRs\Validacao-GR\Validação\CHI_CSF_NLE.pdf',bbox_inches='tight',pad_inches=0.02, transparent=True, dpi=700)

