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


def normalizacao_quimica(dados, inicio_pico_padrao, final_pico_padrao, altura_padrao_corrigida):
    dados_normalizado = np.zeros((len(dados.columns),len(dados))) #fazer uma matriz vazia com zeros
    colunas=[]
    for i in range(len(dados.columns)):#andei nas colunas
        colunas.append(dados.columns[i]) #salvar nome na lista colunas
        if dados.columns[i] =='Time': #se a coluna tiver Time
            dados_normalizado[i] = dados['Time'] #salve o Time
        else: #se nao...
            altura_pico_padrao = max(dados[dados.columns[i]][inicio_pico_padrao:final_pico_padrao])
            dados_normalizado[i] = dados[dados.columns[i]]/altura_pico_padrao*altura_padrao_corrigida
        
    dados_normalizados_transpose=dados_normalizado.T #transpose de coluna pra linha
    df_dados_normalizados = pd.DataFrame(dados_normalizados_transpose, columns=colunas) #gerar o data frame
    return df_dados_normalizados

