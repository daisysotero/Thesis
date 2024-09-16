#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.cm as cm
import matplotlib as mpl
from __future__ import unicode_literals
from matplotlib.gridspec import GridSpec
#matplotlib.rcParams['text.usetex'] = True
from matplotlib.ticker import ScalarFormatter
from matplotlib.ticker import AutoMinorLocator
from scipy.signal import find_peaks
import matplotlib.patches as patches
from statistics import mean, stdev
from math import sqrt
from scipy.stats import f_oneway
from scipy.stats import tukey_hsd
from scipy import stats

#plt.rc('text.latex', preamble=r'\usepackage{amsmath} \usepackage{siunitx}')
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})


# In[ ]:


def media_repbiologicas(dados):
    
    #FAZER LISTAS PARA ANOTAR NOMES UNICOS
    nomes_unicos=[]
    coluna=dados.columns[0] #nao quero que time apareca para colocar na lista
    nome_replicata=coluna.split('-')[0] #zero é tudo que vem antes do ponto

    nomes_unicos.append(nome_replicata)
    for i in range (1,len(dados.columns)):
        coluna=dados.columns[i]
        nome_replicata=coluna.split('-')[0]
        chave=0
        for j in range (len(nomes_unicos)):
            if nome_replicata == nomes_unicos[j]:
                chave=1
        if chave == 0:
            nomes_unicos.append(nome_replicata)
    print(nomes_unicos)

    #######CRIAR MATRIZ PARA FAZER MÉDIAS DAS BIOLÓGICAS
    contador=np.zeros(len(nomes_unicos))

    medias_replicatas=np.zeros((len(dados),len(nomes_unicos))) #np.zeros = criar matriz cujo numero de linhas e colunas sejam de water stresse e nomes_unicos, respectivamente
    for i in range (len(dados.columns)):
        coluna=dados.columns[i]
        nome_replicata=coluna.split('-')[0]
        lista_replicata=[]
        for j in range (len(nomes_unicos)):
            if nome_replicata == nomes_unicos[j]:
                lista_replicata.append(coluna)
                numero_j=j
        if len(lista_replicata)>0:
            medias_replicatas[:,numero_j]+=dados[coluna]
            contador[numero_j]+=1
            #print(lista_replicata)
    print(contador) #ver numero de replicatas biológicas
    for i in range(len(nomes_unicos)):
        medias_replicatas[:,i]=medias_replicatas[:,i]/contador[i]

    dados_media=pd.DataFrame.from_records(medias_replicatas,columns=nomes_unicos)
    return dados_media

