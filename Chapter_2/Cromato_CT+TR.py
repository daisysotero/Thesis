#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# # TEMPERATURA

# In[2]:


df_T = pd.read_csv(r'E:\Doc\Cap 2 - Tratadas_HPLC_Evelu\Analise_HPLC\RESULTADOS_PROCESSADOS\Figures_cromatograma\temp.csv',sep=',', decimal=',')#,index_col=None
contagem = 1
media_T=np.zeros((4,len(df_T)))
for k in range(len(df_T)):
    for i in range(1,len(df_T.columns)):
        if i % 5 == 0:
#             print(i,k,df_T[df_T.columns[i]][k])
            media_T[int(i/5)-1][k]=np.average((df_T[df_T.columns[i-4]][k],df_T[df_T.columns[i-3]][k],
              df_T[df_T.columns[i-2]][k],df_T[df_T.columns[i-1]][k],
              df_T[df_T.columns[i]][k]))
for i in range(1,len(df_T.columns)):
    if i % 5 == 0:
        print(int(i/5)-1,df_T.columns[i])
        
print(media_T.shape)


# In[ ]:


# plt.rc('text.latex', preamble=r'\usepackage{amsmath} \usepackage{siunitx}')
label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_T[0],label='Leaves 24°C',lw=0.5)
axs.plot(df_T['Time'],media_T[1],label='Leaves 50°C',lw=0.5, alpha=0.7)
# axs.plot(df_T['Time'],media_T[2],c='tan',label='Roots 24°C',lw=0.5)
# axs.plot(df_T['Time'],media_T[3],c='sienna',label='Roots 50°C',lw=0.5)
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
# axs.set_xlim(3.5,25)
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.xticks([5,10,15,20,25,30,35])


label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_T[1],label='Leaves 50°C',lw=0.5)
axs.scatter(tempo,picos,label='Leaves 50°C',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_T['Time'][peaks[0][i]] < 35.0:
        plt.text(df_T['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_T['Time'][peaks[0][i]],fontsize=2)


# In[41]:


peaks_l = find_peaks(media_T[1], height = 0.001, prominence=0.01, distance=20)
picos_l = peaks_l[1]['peak_heights']
peaks_r = find_peaks(media_T[3], height = 0.001, prominence=0.01, distance=20)
picos_r = peaks_r[1]['peak_heights']

#df_T['Time'][peaks[0]] posição no eixo x
# peaks_l altura do pico. eixo y
num = 0
label_size=8
plots_em_x=1
plots_em_y=1

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_T[0],label='Leaves 24°C',lw=0.5)
axs.plot(df_T['Time'],media_T[1],label='Leaves 50°C',lw=0.5, alpha=0.7)
# axs.plot(df_T['Time'],media_T[2],c='tan',label='Roots 24°C',lw=0.5)
# axs.plot(df_T['Time'],media_T[3],c='sienna',label='Roots 50°C',lw=0.5)
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
# axs.set_xlim(3.5,25)
axs.legend(fontsize=label_size, frameon=False, loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=2)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
altura1=0.8 #posição em y da altura das linhas
altura2=0.78
for i in range(len(df_T['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_T['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_T['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_T['Time'][peaks_l[0][i]],df_T['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_T['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_T['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_T['Time'][peaks_l[0][i]],df_T['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_T['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_T['Time'][peaks_l[0][i]],fontsize=1.5)

plt.savefig('temp_leaves.pdf',
            bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
# axs.plot(df_T['Time'],media_T[0],c='lime',label='Leaves 24°C',lw=0.5)
# axs.plot(df_T['Time'],media_T[1],c='darkgreen',label='Leaves 50°C',lw=0.5)
axs.plot(df_T['Time'],media_T[2],label='Roots 24°C',lw=0.5)
axs.plot(df_T['Time'],media_T[3],label='Roots 50°C',lw=0.5, alpha=0.7)
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
# axs.set_xlim(3.5,25)
axs.legend(fontsize=label_size, frameon=False, loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=2)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
altura1=0.4
altura2=0.38
for i in range(len(df_T['Time'][peaks_r[0]])):
    if (df_T['Time'][peaks_r[0][i]]) < 35:
        plt.text(df_T['Time'][peaks_r[0][i]]+0.1,picos_r[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0:
            plt.plot((df_T['Time'][peaks_r[0][i]],df_T['Time'][peaks_r[0][i]]),(picos_r[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_T['Time'][peaks_r[0][i]]-0.2,altura1+0.001,'%.1f'%df_T['Time'][peaks_r[0][i]],fontsize=1.5)
        else:
            plt.plot((df_T['Time'][peaks_r[0][i]],df_T['Time'][peaks_r[0][i]]),(picos_r[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_T['Time'][peaks_r[0][i]]-0.2,altura2+0.001,'%.1f'%df_T['Time'][peaks_r[0][i]],fontsize=1.5)


plt.savefig('temp_roots.pdf',
            bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

plt.close(fig)


# # UV

# In[10]:


df_uv = pd.read_csv(r'E:\Doc\Cap 2 - Tratadas_HPLC_Evelu\Analise_HPLC\RESULTADOS_PROCESSADOS\Figures_cromatograma\uv.csv',sep=',', decimal=',')#,index_col=None


# In[11]:


for i in range(len(df_uv.columns)):
    print(i,df_uv.columns[i])


# In[12]:


A = 26
B = 29

UV4 = np.zeros((B-A+1,len(df_uv)))

for i in range (A,B+1):
    UV4[i-A]=df_uv[df_uv.columns[i]]

df2_uv = df_uv.drop(df_uv.columns[[26,27,28,29]],axis = 1)

media_UV=np.zeros((7,len(df2_uv)))
media_UV2=np.zeros(len(UV4[0]))
for k in range(len(df2_uv)):
    for i in range(1,len(df2_uv.columns)):
        if i % 5 == 0:
            media_UV[int(i/5)-1][k]=np.average((df2_uv[df2_uv.columns[i-4]][k],df2_uv[df2_uv.columns[i-3]][k],
                                              df2_uv[df2_uv.columns[i-2]][k],df2_uv[df2_uv.columns[i-1]][k],
                                              df2_uv[df2_uv.columns[i]][k]))

for i in range(1,len(df2_uv.columns)):
    if i % 5 == 0:
        print(int(i/5)-1,df2_uv.columns[i])
        
    for i in range(len(UV4[0])):  
        media_UV2[i]=np.average((UV4[0][i],UV4[1][i],UV4[2][i],UV4[3][i]))
        


# In[13]:


# plt.rc('text.latex', preamble=r'\usepackage{amsmath} \usepackage{siunitx}')
label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_uv['Time'],media_UV[0],label='CT leaves 24h',lw=0.5)
axs.plot(df_uv['Time'],media_UV[4],label='Leaves 24h',lw=0.5, alpha=0.7)
# axs.plot(df_uv['Time'],media_UV[2],c='tan',label='Roots 24°C',lw=0.5)
# axs.plot(df_uv['Time'],media_UV[3],c='sienna',label='Roots 50°C',lw=0.5)
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
# axs.set_xlim(3.5,25)
axs.legend(fontsize=label_size, frameon=False, loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=2)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
num = 0
peaks_l = find_peaks(media_UV[4], height = 0.001, prominence=0.01, distance=20)
picos_l = peaks_l[1]['peak_heights']

altura1=0.4 #posição em y da altura das linhas
altura2=0.38
for i in range(len(df_uv['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_uv['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_uv['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_uv['Time'][peaks_l[0][i]],df_uv['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_uv['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_uv['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_uv['Time'][peaks_l[0][i]],df_uv['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_uv['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_uv['Time'][peaks_l[0][i]],fontsize=1.5)
            
            
plt.savefig('uv24_leaves.pdf',
            bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
# axs.plot(df_uv['Time'],media_UV[0],c='lime',label='Leaves 24°C',lw=0.5)
# axs.plot(df_uv['Time'],media_UV[1],c='darkgreen',label='Leaves 50°C',lw=0.5)
axs.plot(df_uv['Time'],media_UV[2],label='CT leaves 48h',lw=0.5)
axs.plot(df_uv['Time'],media_UV[5],label='Leaves 48h',lw=0.5, alpha=0.7)
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
# axs.set_xlim(3.5,25)
axs.legend(fontsize=label_size, frameon=False, loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=2)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
peaks_l = find_peaks(media_UV[5], height = 0.001, prominence=0.01, distance=20)
picos_l = peaks_l[1]['peak_heights']

altura1=0.8 #posição em y da altura das linhas
altura2=0.78
for i in range(len(df_uv['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_uv['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_uv['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_uv['Time'][peaks_l[0][i]],df_uv['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_uv['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_uv['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_uv['Time'][peaks_l[0][i]],df_uv['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_uv['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_uv['Time'][peaks_l[0][i]],fontsize=1.5)
plt.savefig('uv48_leaves.pdf',
            bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 


fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_uv['Time'],media_UV[1],label='CT roots 24h',lw=0.5)
axs.plot(df2_uv['Time'],media_UV2,label='Roots 24h',lw=0.5,alpha=0.7)
# axs.plot(df_uv['Time'],media_UV[2],c='tan',label='Roots 24°C',lw=0.5)
# axs.plot(df_uv['Time'],media_UV[3],c='sienna',label='Roots 50°C',lw=0.5)
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
# axs.set_xlim(3.5,25)
axs.legend(fontsize=label_size, frameon=False, loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=2)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
peaks_l = find_peaks(media_UV2, height = 0.001, prominence=0.01, distance=20)
picos_l = peaks_l[1]['peak_heights']

altura1=0.4 #posição em y da altura das linhas
altura2=0.38
for i in range(len(df_uv['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_uv['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_uv['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_uv['Time'][peaks_l[0][i]],df_uv['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_uv['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_uv['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_uv['Time'][peaks_l[0][i]],df_uv['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_uv['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_uv['Time'][peaks_l[0][i]],fontsize=1.5)
 
plt.savefig('uv24_roots.pdf',
            bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
# axs.plot(df_uv['Time'],media_UV[0],c='lime',label='Leaves 24°C',lw=0.5)
# axs.plot(df_uv['Time'],media_UV[1],c='darkgreen',label='Leaves 50°C',lw=0.5)
axs.plot(df_uv['Time'],media_UV[3],label='CT roots 48h',lw=0.5)
axs.plot(df_uv['Time'],media_UV[6],label='Roots 48h',lw=0.5, alpha=0.7)
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
# axs.set_xlim(3.5,25)
axs.legend(fontsize=label_size, frameon=False,loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=2)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
peaks_l = find_peaks(media_UV[6], height = 0.001, prominence=0.01, distance=20)
picos_l = peaks_l[1]['peak_heights']

altura1=0.4 #posição em y da altura das linhas
altura2=0.38
for i in range(len(df_uv['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_uv['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_uv['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_uv['Time'][peaks_l[0][i]],df_uv['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_uv['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_uv['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_uv['Time'][peaks_l[0][i]],df_uv['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_uv['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_uv['Time'][peaks_l[0][i]],fontsize=1.5)
plt.savefig('uv48_roots.pdf',
            bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

plt.close(fig)


# # MeJA

# In[14]:


df_meja = pd.read_csv(r'E:\Doc\Cap 2 - Tratadas_HPLC_Evelu\Analise_HPLC\RESULTADOS_PROCESSADOS\Figures_cromatograma\meja.csv',sep=',', decimal=',')#,index_col=None
contagem = 1
media_meja=np.zeros((12,len(df_meja)))
for k in range(len(df_meja)):
    for i in range(1,len(df_meja.columns)):
        if i % 5 == 0:
#             print(i,k,df_T[df_T.columns[i]][k])
            media_meja[int(i/5)-1][k]=np.average((df_meja[df_meja.columns[i-4]][k],df_meja[df_meja.columns[i-3]][k],
                                                  df_meja[df_meja.columns[i-2]][k],df_meja[df_meja.columns[i-1]][k],
                                                  df_meja[df_meja.columns[i]][k]))
for i in range(1,len(df_meja.columns)):
    if i % 5 == 0:
        print(int(i/5)-1,df_meja.columns[i])
        
print(media_meja.shape)


# In[15]:


num = 0
peaks_l = find_peaks(media_meja[4], height = 0.001, prominence=0.01, distance=20)
picos_l = peaks_l[1]['peak_heights']

label_size=6.5
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))

axs.plot(df_meja['Time'],media_meja[0],label='CT leaves 2d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[4],label='Leaves 40 µM 2d',lw=0.5, alpha=0.7)
axs.plot(df_meja['Time'],media_meja[5],label='Leaves 100 µM 2d',lw=0.5,alpha=0.7)

axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
altura1=0.4 #posição em y da altura das linhas
altura2=0.38
for i in range(len(df_T['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_T['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_T['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_T['Time'][peaks_l[0][i]],df_T['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_T['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_T['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_T['Time'][peaks_l[0][i]],df_T['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_T['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_T['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('meja_leaves_2d.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
plt.close(fig)


peaks_l = find_peaks(media_meja[8], height = 0.001, prominence=0.01, distance=20)
picos_l = peaks_l[1]['peak_heights']

label_size=6.5

plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))


axs.plot(df_meja['Time'],media_meja[2],label='CT leaves 4d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[8],label='Leaves 40 µM 4d',lw=0.5,alpha=0.7)
axs.plot(df_meja['Time'],media_meja[9],label='Leaves 100 µM 4d',lw=0.5,alpha=0.7)

axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
altura1=0.9 #posição em y da altura das linhas
altura2=0.88
for i in range(len(df_T['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_T['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_T['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_T['Time'][peaks_l[0][i]],df_T['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_T['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_T['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_T['Time'][peaks_l[0][i]],df_T['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_T['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_T['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('meja_leaves_4d.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
plt.close(fig)


peaks_l = find_peaks(media_meja[6], height = 0.001, prominence=0.01, distance=20)
picos_l = peaks_l[1]['peak_heights']

label_size=6.5
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))

axs.plot(df_meja['Time'],media_meja[1],label='CT roots 2d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[6],label='Roots 40 µM 2d',lw=0.5,alpha=0.7)
axs.plot(df_meja['Time'],media_meja[7],label='Roots 100 µM 2d',lw=0.5,alpha=0.7)

axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})

altura1=0.65 #posição em y da altura das linhas
altura2=0.62
for i in range(len(df_T['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_T['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_T['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_T['Time'][peaks_l[0][i]],df_T['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_T['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_T['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_T['Time'][peaks_l[0][i]],df_T['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_T['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_T['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('meja_roots_2d.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
plt.close(fig)


peaks_l = find_peaks(media_meja[10], height = 0.001, prominence=0.01, distance=20)
picos_l = peaks_l[1]['peak_heights']

label_size=6.5

plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))

axs.plot(df_meja['Time'],media_meja[3],label='CT roots 4d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[10],label='Roots 40 µM 4d',lw=0.5,alpha=0.7)
axs.plot(df_meja['Time'],media_meja[11],label='Roots 100 µM 4d',lw=0.5,alpha=0.7)
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
altura1=0.55 #posição em y da altura das linhas
altura2=0.52
for i in range(len(df_T['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_T['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_T['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_T['Time'][peaks_l[0][i]],df_T['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_T['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_T['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_T['Time'][peaks_l[0][i]],df_T['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_T['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_T['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('meja_roots_4d.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
plt.close(fig)


# # AS

# In[16]:


df_as = pd.read_csv(r'E:\Doc\Cap 2 - Tratadas_HPLC_Evelu\Analise_HPLC\RESULTADOS_PROCESSADOS\Figures_cromatograma\as.csv',sep=',', decimal=',')#,index_col=None
contagem = 1
media_as=np.zeros((12,len(df_as)))
for k in range(len(df_as)):
    for i in range(1,len(df_as.columns)):
        if i % 5 == 0:
#             print(i,k,df_T[df_T.columns[i]][k])
            media_as[int(i/5)-1][k]=np.average((df_as[df_as.columns[i-4]][k],df_as[df_as.columns[i-3]][k],
                                                df_as[df_as.columns[i-2]][k],df_as[df_as.columns[i-1]][k],
                                                df_as[df_as.columns[i]][k]))
for i in range(1,len(df_as.columns)):
    if i % 5 == 0:
        print(int(i/5)-1,df_as.columns[i])
        
print(media_as.shape)


# In[17]:


# plt.rc('text.latex', preamble=r'\usepackage{amsmath} \usepackage{siunitx}')

num = 0
peaks_l = find_peaks(media_as[4], height = 0.001, prominence=0.01, distance=20)
picos_l = peaks_l[1]['peak_heights']

label_size=6.5
plots_em_x=1
plots_em_y=1

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_as['Time'],media_as[0],label='CT leaves 2d',lw=0.5)
axs.plot(df_as['Time'],media_as[4],label='Leaves 1 mM 2d',lw=0.5, alpha=0.7)
axs.plot(df_as['Time'],media_as[5],label='Leaves 2 mM 2d',lw=0.5, alpha=0.7)

axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3.0,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
altura1=0.7 #posição em y da altura das linhas
altura2=0.68
for i in range(len(df_T['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_T['Time'][peaks_l[0][i]]) < 34.5: #selecionar T menor que 35 min
        plt.text(df_T['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_T['Time'][peaks_l[0][i]],df_T['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_T['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_T['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_T['Time'][peaks_l[0][i]],df_T['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_T['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_T['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('AS_leaves_2d.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 

peaks_l = find_peaks(media_as[8], height = 0.001, prominence=0.01, distance=20)
picos_l = peaks_l[1]['peak_heights']
label_size=6.5

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_as['Time'],media_as[2],label='CT leaves 4d',lw=0.5)
axs.plot(df_as['Time'],media_as[8],label='Leaves 1 mM 4d',lw=0.5, alpha=0.7)
axs.plot(df_as['Time'],media_as[9],label='Leaves 2 mM 4d',lw=0.5, alpha=0.7)

axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
altura1=0.8 #posição em y da altura das linhas
altura2=0.78
for i in range(len(df_T['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_T['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_T['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_T['Time'][peaks_l[0][i]],df_T['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_T['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_T['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_T['Time'][peaks_l[0][i]],df_T['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_T['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_T['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('AS_leaves_4d.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 


peaks_l = find_peaks(media_as[6], height = 0.001, prominence=0.01, distance=20)
picos_l = peaks_l[1]['peak_heights']
label_size=6.5

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_as['Time'],media_as[1],label='CT roots 2d',lw=0.5)
axs.plot(df_as['Time'],media_as[6],label='Roots 1 mM 2d',lw=0.5, alpha=0.7)
axs.plot(df_as['Time'],media_as[7],label='Roots 2 mM 2d',lw=0.5, alpha=0.7)

axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
altura1=0.7 #posição em y da altura das linhas
altura2=0.68
for i in range(len(df_T['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_T['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_T['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_T['Time'][peaks_l[0][i]],df_T['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_T['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_T['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_T['Time'][peaks_l[0][i]],df_T['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_T['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_T['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('AS_roots_2d.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 

peaks_l = find_peaks(media_as[10], height = 0.001, prominence=0.01, distance=20)
picos_l = peaks_l[1]['peak_heights']
label_size=6.5

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_as['Time'],media_as[3],label='CT roots 4d',lw=0.5)
axs.plot(df_as['Time'],media_as[10],label='Roots 1 mM 4d',lw=0.5, alpha=0.7)
axs.plot(df_as['Time'],media_as[11],label='Roots 2 mM 4d',lw=0.5, alpha=0.7)
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
altura1=0.7 #posição em y da altura das linhas
altura2=0.68
for i in range(len(df_T['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_T['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_T['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_T['Time'][peaks_l[0][i]],df_T['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_T['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_T['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_T['Time'][peaks_l[0][i]],df_T['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_T['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_T['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('AS_roots_4d.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
plt.close(fig)






# # SNP

# In[18]:


df_snp = pd.read_csv(r'E:\Doc\Cap 2 - Tratadas_HPLC_Evelu\Analise_HPLC\RESULTADOS_PROCESSADOS\Figures_cromatograma\snp.csv',sep=',', decimal=',')#,index_col=None


# In[19]:


for i in range(len(df_snp.columns)):
    print(i,df_snp.columns[i])


# In[20]:


A = 31
B = 34

SNP4 = np.zeros((B-A+1,len(df_snp)))

for i in range (A,B+1):
    SNP4[i-A]=df_snp[df_snp.columns[i]]

df2_snp = df_snp.drop(df_snp.columns[[31,32,33,34]],axis = 1)

media_snp=np.zeros((11,len(df2_snp)))
media_snp2=np.zeros(len(SNP4[0]))
for k in range(len(df2_snp)):
    for i in range(1,len(df2_snp.columns)):
        if i % 5 == 0:
            media_snp[int(i/5)-1][k]=np.average((df2_snp[df2_snp.columns[i-4]][k],df2_snp[df2_snp.columns[i-3]][k],
                                              df2_snp[df2_snp.columns[i-2]][k],df2_snp[df2_snp.columns[i-1]][k],
                                              df2_snp[df2_snp.columns[i]][k]))

for i in range(1,len(df2_snp.columns)):
    if i % 5 == 0:
        print(int(i/5)-1,df2_snp.columns[i])
        
for i in range(len(SNP4[0])):       
    media_snp2[i]=np.average((SNP4[0][i],SNP4[1][i],SNP4[2][i],SNP4[3][i]))
    


# In[21]:


num=0
peaks_l = find_peaks(media_snp[4], height = 0.001, prominence=0.01, distance=20)
picos_l = peaks_l[1]['peak_heights']
label_size=6.5
plots_em_x=1
plots_em_y=1

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df2_snp['Time'],media_snp[0],label='CT leaves 2d',lw=0.5)
axs.plot(df2_snp['Time'],media_snp[4],label='Leaves 100 µM 2d',lw=0.5,alpha=0.7)
axs.plot(df2_snp['Time'],media_snp[5],label='Leaves 200 µM 2d',lw=0.5,alpha=0.7)

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
altura1=2.5 #posição em y da altura das linhas
altura2=2.45
for i in range(len(df2_snp['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df2_snp['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df2_snp['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df2_snp['Time'][peaks_l[0][i]],df2_snp['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df2_snp['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df2_snp['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df2_snp['Time'][peaks_l[0][i]],df2_snp['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df2_snp['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df2_snp['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('snp_leaves_2d.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500)

peaks_l = find_peaks(media_snp[7], height = 0.001, prominence=0.01, distance=20)
picos_l = peaks_l[1]['peak_heights']
label_size=6.5

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df2_snp['Time'],media_snp[2],label='CT leaves 4d',lw=0.5)
axs.plot(df2_snp['Time'],media_snp[7],label='Leaves 100 µM 4d',lw=0.5,alpha=0.7)
axs.plot(df2_snp['Time'],media_snp[8],label='Leaves 200 µM 4d',lw=0.5,alpha=0.7)

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
altura1=1.7 #posição em y da altura das linhas
altura2=1.65
for i in range(len(df2_snp['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df2_snp['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df2_snp['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df2_snp['Time'][peaks_l[0][i]],df2_snp['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df2_snp['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df2_snp['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df2_snp['Time'][peaks_l[0][i]],df2_snp['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df2_snp['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df2_snp['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('snp_leaves_4d.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500)


peaks_l = find_peaks(media_snp2, height = 0.001, prominence=0.01, distance=20)
picos_l = peaks_l[1]['peak_heights']
label_size=6.5

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df2_snp['Time'],media_snp[1],label='CT roots 2d',lw=0.5)
axs.plot(df2_snp['Time'],media_snp2,label='Roots 100 µM 2d',lw=0.5,alpha=0.7)
axs.plot(df2_snp['Time'],media_snp[6],label='Roots 200 µM 2d',lw=0.5,alpha=0.7)

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
altura1=1.3 #posição em y da altura das linhas
altura2=1.25
for i in range(len(df2_snp['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df2_snp['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df2_snp['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df2_snp['Time'][peaks_l[0][i]],df2_snp['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df2_snp['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df2_snp['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df2_snp['Time'][peaks_l[0][i]],df2_snp['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df2_snp['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df2_snp['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('snp_roots_2d.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500)


peaks_l = find_peaks(media_snp[9], height = 0.001, prominence=0.01, distance=20)
picos_l = peaks_l[1]['peak_heights']
label_size=6.5

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df2_snp['Time'],media_snp[3],label='CT roots 4d',lw=0.5)
axs.plot(df2_snp['Time'],media_snp[9],label='Roots 100 µM 4d',lw=0.5,alpha=0.7)
axs.plot(df2_snp['Time'],media_snp[10],label='Roots 200 µM 4d',lw=0.5,alpha=0.7)

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
altura1=0.6 #posição em y da altura das linhas
altura2=0.58
for i in range(len(df2_snp['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df2_snp['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df2_snp['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df2_snp['Time'][peaks_l[0][i]],df2_snp['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df2_snp['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df2_snp['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df2_snp['Time'][peaks_l[0][i]],df2_snp['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df2_snp['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df2_snp['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('snp_roots_4d.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500)

plt.close(fig)


# # DM

# In[22]:


df_dm = pd.read_csv(r'E:\Doc\Cap 2 - Tratadas_HPLC_Evelu\Analise_HPLC\RESULTADOS_PROCESSADOS\Figures_cromatograma\dm.csv',sep=',', decimal=',')#,index_col=None


# In[23]:


for i in range(len(df_dm.columns)):
    print(i,df_dm.columns[i])


# In[24]:


# A = 31
# B = 34

# SNP4 = np.zeros((B-A+1,len(df_dm)))

# for i in range (A,B+1):
#     SNP4[i-A]=df_dm[df_dm.columns[i]]

# df2_snp = df_dm.drop(df_dm.columns[[31,32,33,34]],axis = 1)

media_dm=np.zeros((12,len(df_dm)))
# media_dm2=np.zeros(len(SNP4[0]))
for k in range(len(df_dm)):
    for i in range(1,len(df_dm.columns)):
        if i % 5 == 0:
            media_dm[int(i/5)-1][k]=np.average((df_dm[df_dm.columns[i-4]][k],df_dm[df_dm.columns[i-3]][k],
                                              df_dm[df_dm.columns[i-2]][k],df_dm[df_dm.columns[i-1]][k],
                                              df_dm[df_dm.columns[i]][k]))

for i in range(1,len(df_dm.columns)):
    if i % 5 == 0:
        print(int(i/5)-1,df_dm.columns[i])
        
# for k in range(len(UV4)):       
#     media_dm2[k]=np.average((SNP4[0],SNP4[1],SNP4[2],SNP4[3]))


# In[25]:


num=0
peaks_l = find_peaks(media_dm[4], height = 0.001, prominence=0.01, distance=20)
picos_l = peaks_l[1]['peak_heights']
label_size=6.5
plots_em_x=1
plots_em_y=1

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_dm['Time'],media_dm[0],label='CT leaves 2d',lw=0.5)
axs.plot(df_dm['Time'],media_dm[4],label='Leaves 2d 25%',lw=0.5,alpha=0.7)
axs.plot(df_dm['Time'],media_dm[5],label='Leaves 2d 75%',lw=0.5,alpha=0.7)

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
altura1=0.5 #posição em y da altura das linhas
altura2=0.48
for i in range(len(df_dm['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_dm['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_dm['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_dm['Time'][peaks_l[0][i]],df_dm['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_dm['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_dm['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_dm['Time'][peaks_l[0][i]],df_dm['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_dm['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_dm['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('dm_leaves_2d.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 

peaks_l = find_peaks(media_dm[8], height = 0.001, prominence=0.01, distance=20)
picos_l = peaks_l[1]['peak_heights']
label_size=6.5
plots_em_x=1
plots_em_y=1

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_dm['Time'],media_dm[2],label='CT leaves 4d',lw=0.5)
axs.plot(df_dm['Time'],media_dm[8],label='Leaves 4d 25%',lw=0.5,alpha=0.7)
axs.plot(df_dm['Time'],media_dm[9],label='Leaves 4d 75%',lw=0.5,alpha=0.7)

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
altura1=0.3 #posição em y da altura das linhas
altura2=0.28
for i in range(len(df_dm['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_dm['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_dm['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_dm['Time'][peaks_l[0][i]],df_dm['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_dm['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_dm['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_dm['Time'][peaks_l[0][i]],df_dm['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_dm['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_dm['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('dm_leaves_4d.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500)



peaks_l = find_peaks(media_dm[6], height = 0.001, prominence=0.006, distance=20)
picos_l = peaks_l[1]['peak_heights']

label_size=6.5
plots_em_x=1
plots_em_y=1

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_dm['Time'],media_dm[1],label='CT roots 2d',lw=0.5)
axs.plot(df_dm['Time'],media_dm[6],label='Roots 2d 25%',lw=0.5,alpha=0.7)
axs.plot(df_dm['Time'],media_dm[7],label='Roots 2d 75%',lw=0.5,alpha=0.7)

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
altura1=0.4 #posição em y da altura das linhas
altura2=0.38
for i in range(len(df_dm['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_dm['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_dm['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_dm['Time'][peaks_l[0][i]],df_dm['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_dm['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_dm['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_dm['Time'][peaks_l[0][i]],df_dm['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_dm['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_dm['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('dm_roots_2d.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500)



peaks_l = find_peaks(media_dm[10], height = 0.001, prominence=0.005, distance=20)
picos_l = peaks_l[1]['peak_heights']
label_size=6.5
plots_em_x=1
plots_em_y=1

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_dm['Time'],media_dm[3],label='CT roots 4d',lw=0.5)
axs.plot(df_dm['Time'],media_dm[10],label='Roots 4d 25%',lw=0.5,alpha=0.7)
axs.plot(df_dm['Time'],media_dm[11],label='Roots 4d 75%',lw=0.5,alpha=0.7)

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
altura1=0.5 #posição em y da altura das linhas
altura2=0.48
for i in range(len(df_dm['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_dm['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_dm['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_dm['Time'][peaks_l[0][i]],df_dm['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_dm['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_dm['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_dm['Time'][peaks_l[0][i]],df_dm['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_dm['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_dm['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('dm_roots_4d.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500)


plt.close(fig)


# # Nacl

# In[26]:


df_nacl = pd.read_csv(r'E:\Doc\Cap 2 - Tratadas_HPLC_Evelu\Analise_HPLC\RESULTADOS_PROCESSADOS\Figures_cromatograma\salino.csv',sep=',', decimal=',')#,index_col=None


# In[27]:


for i in range(len(df_nacl.columns)):
    print(i,df_nacl.columns[i])


# In[28]:


A = 21
B = 22

C = 28
D = 30

nacl2 = np.zeros((B-A+1,len(df_nacl)))

for i in range (A,B+1):
    nacl2[i-A]=df_nacl[df_nacl.columns[i]]
    
nacl3 = np.zeros((D-C+1,len(df_nacl)))

for i in range (C,D+1):
    nacl3[i-D]=df_nacl[df_nacl.columns[i]]

df2_nacl = df_nacl.drop(df_nacl.columns[[21,22,28,29,30]],axis = 1)


media_nacl=np.zeros((10,len(df2_nacl)))
media_nacl2=np.zeros(len(nacl2[0]))
media_nacl3=np.zeros(len(nacl3[0]))
for k in range(len(df2_nacl)):
    for i in range(1,len(df2_nacl.columns)):
        if i % 5 == 0:
            media_nacl[int(i/5)-1][k]=np.average((df2_nacl[df2_nacl.columns[i-4]][k],df2_nacl[df2_nacl.columns[i-3]][k],
                                              df2_nacl[df2_nacl.columns[i-2]][k],df2_nacl[df2_nacl.columns[i-1]][k],
                                              df2_nacl[df2_nacl.columns[i]][k]))

for i in range(1,len(df2_nacl.columns)):
    if i % 5 == 0:
        print(int(i/5)-1,df2_nacl.columns[i])
        
for i in range(len(nacl2[0])):       
    media_nacl2[i]=np.average((nacl2[0][i],nacl2[1][i]))
    
for i in range(len(nacl3[0])):       
    media_nacl3[i]=np.average((nacl3[0][i],nacl3[1][i],nacl3[2][i]))
    
    


# In[30]:


num=0
peaks_l = find_peaks(media_nacl2, height = 0.001, prominence=0.01, distance=20)
picos_l = peaks_l[1]['peak_heights']
label_size=6.5
plots_em_x=1
plots_em_y=1

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))

axs.plot(df2_nacl['Time'],media_nacl[0],label='CT leaves 2d',lw=0.5)
axs.plot(df2_nacl['Time'],media_nacl2,label='Leaves 2d 0,25M',lw=0.5,alpha=0.7)
axs.plot(df2_nacl['Time'],media_nacl[4],label='Leaves 2d 0,50M',lw=0.5,alpha=0.7)

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
altura1=0.5 #posição em y da altura das linhas
altura2=0.48
for i in range(len(df2_nacl['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df2_nacl['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df2_nacl['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df2_nacl['Time'][peaks_l[0][i]],df2_nacl['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df2_nacl['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df2_nacl['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df2_nacl['Time'][peaks_l[0][i]],df2_nacl['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df2_nacl['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df2_nacl['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('nacl_leaves_2d.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500)



peaks_l = find_peaks(media_nacl[6], height = 0.001, prominence=0.01, distance=20)
picos_l = peaks_l[1]['peak_heights']
label_size=6.5

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df2_nacl['Time'],media_nacl[2],label='CT leaves 4d',lw=0.5)
axs.plot(df2_nacl['Time'],media_nacl[6],label='Leaves 4d 0,25M',lw=0.5,alpha=0.7)
axs.plot(df2_nacl['Time'],media_nacl[7],label='Leaves 4d 0,50M',lw=0.5,alpha=0.7)

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
altura1=0.5 #posição em y da altura das linhas
altura2=0.48
for i in range(len(df2_nacl['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df2_nacl['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df2_nacl['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df2_nacl['Time'][peaks_l[0][i]],df2_nacl['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df2_nacl['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df2_nacl['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df2_nacl['Time'][peaks_l[0][i]],df2_nacl['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df2_nacl['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df2_nacl['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('nacl_leaves_4d.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500)



peaks_l = find_peaks(media_nacl3, height = 0.001, prominence=0.01, distance=20)
picos_l = peaks_l[1]['peak_heights']
label_size=6.5

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df2_nacl['Time'],media_nacl[1],label='CT roots 2d',lw=0.5)
axs.plot(df2_nacl['Time'],media_nacl3,label='Roots 2d 0,25M',lw=0.5,alpha=0.7)
axs.plot(df2_nacl['Time'],media_nacl[5],label='Roots 2d 0,50M',lw=0.5,alpha=0.7)

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
altura1=0.4 #posição em y da altura das linhas
altura2=0.38
for i in range(len(df2_nacl['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df2_nacl['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df2_nacl['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df2_nacl['Time'][peaks_l[0][i]],df2_nacl['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df2_nacl['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df2_nacl['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df2_nacl['Time'][peaks_l[0][i]],df2_nacl['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df2_nacl['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df2_nacl['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('nacl_roots_2d.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500)



peaks_l = find_peaks(media_nacl[8], height = 0.001, prominence=0.01, distance=20)
picos_l = peaks_l[1]['peak_heights']
label_size=6.5

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df2_nacl['Time'],media_nacl[3],label='CT roots 4d',lw=0.5)
axs.plot(df2_nacl['Time'],media_nacl[8],label='Roots 4d 0,25M',lw=0.5,alpha=0.7)
axs.plot(df2_nacl['Time'],media_nacl[9],label='Roots 4d 0,50M',lw=0.5,alpha=0.7)

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
altura1=0.5 #posição em y da altura das linhas
altura2=0.48
for i in range(len(df2_nacl['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df2_nacl['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df2_nacl['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df2_nacl['Time'][peaks_l[0][i]],df2_nacl['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df2_nacl['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df2_nacl['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df2_nacl['Time'][peaks_l[0][i]],df2_nacl['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df2_nacl['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df2_nacl['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('nacl_roots_4d.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500)


plt.close(fig)


# # ABA

# In[31]:


df_aba = pd.read_csv(r'E:\Doc\Cap 2 - Tratadas_HPLC_Evelu\Analise_HPLC\RESULTADOS_PROCESSADOS\Figures_cromatograma\aba.csv',sep=',', decimal=',')#,index_col=None


# In[32]:


for i in range(len(df_aba.columns)):
    print(i,df_aba.columns[i])


# In[33]:


# A = 31
# B = 34

# SNP4 = np.zeros((B-A+1,len(df_aba)))

# for i in range (A,B+1):
#     SNP4[i-A]=df_aba[df_aba.columns[i]]

# df2_snp = df_aba.drop(df_aba.columns[[31,32,33,34]],axis = 1)

media_aba=np.zeros((12,len(df_aba)))
# media_aba2=np.zeros(len(SNP4[0]))
for k in range(len(df_aba)):
    for i in range(1,len(df_aba.columns)):
        if i % 5 == 0:
            media_aba[int(i/5)-1][k]=np.average((df_aba[df_aba.columns[i-4]][k],df_aba[df_aba.columns[i-3]][k],
                                              df_aba[df_aba.columns[i-2]][k],df_aba[df_aba.columns[i-1]][k],
                                              df_aba[df_aba.columns[i]][k]))

for i in range(1,len(df_aba.columns)):
    if i % 5 == 0:
        print(int(i/5)-1,df_aba.columns[i])
        
# for k in range(len(UV4)):       
#     media_aba2[k]=np.average((SNP4[0],SNP4[1],SNP4[2],SNP4[3]))


# In[34]:


num=0
peaks_l = find_peaks(media_aba[4], height = 0.001, prominence=0.007, distance=20)
picos_l = peaks_l[1]['peak_heights']
label_size=6.5
plots_em_x=1
plots_em_y=1

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_aba['Time'],media_aba[0],label=r'CT leaves 2d',lw=0.5)
axs.plot(df_aba['Time'],media_aba[4],label=r'Leaves 2d 25 mg/mL',lw=0.5,alpha=0.7)
axs.plot(df_aba['Time'],media_aba[5],label=r'Leaves 2d 50 mg/mL',lw=0.5,alpha=0.7)

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
altura1=0.5 #posição em y da altura das linhas
altura2=0.48
for i in range(len(df_aba['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_aba['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_aba['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_aba['Time'][peaks_l[0][i]],df_aba['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_aba['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_aba['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_aba['Time'][peaks_l[0][i]],df_aba['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_aba['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_aba['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('aba_leaves_2d.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500)



peaks_l = find_peaks(media_aba[8], height = 0.001, prominence=0.007, distance=20)
picos_l = peaks_l[1]['peak_heights']
label_size=6.5

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_aba['Time'],media_aba[2],label=r'CT leaves 4d',lw=0.5)
axs.plot(df_aba['Time'],media_aba[8],label=r'Leaves 4d 25 mg/mL',lw=0.5,alpha=0.7)
axs.plot(df_aba['Time'],media_aba[9],label=r'Leaves 4d 50 mg/mL',lw=0.5,alpha=0.7)

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
altura1=0.5 #posição em y da altura das linhas
altura2=0.48
for i in range(len(df_aba['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_aba['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_aba['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_aba['Time'][peaks_l[0][i]],df_aba['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_aba['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_aba['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_aba['Time'][peaks_l[0][i]],df_aba['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_aba['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_aba['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('aba_leaves_4d.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 


peaks_l = find_peaks(media_aba[6], height = 0.001, prominence=0.007, distance=20)
picos_l = peaks_l[1]['peak_heights']
label_size=6.5

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_aba['Time'],media_aba[1],label=r'CT roots 2d',lw=0.5)
axs.plot(df_aba['Time'],media_aba[6],label=r'Roots 2d 25 mg/mL',lw=0.5,alpha=0.7)
axs.plot(df_aba['Time'],media_aba[7],label=r'Roots 2d 50 mg/mL',lw=0.5,alpha=0.7)

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
altura1=0.5 #posição em y da altura das linhas
altura2=0.48
for i in range(len(df_aba['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_aba['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_aba['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_aba['Time'][peaks_l[0][i]],df_aba['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_aba['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_aba['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_aba['Time'][peaks_l[0][i]],df_aba['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_aba['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_aba['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('aba_roots_2d.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 




peaks_l = find_peaks(media_aba[10], height = 0.001, prominence=0.007, distance=20)
picos_l = peaks_l[1]['peak_heights']
label_size=6.5

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_aba['Time'],media_aba[3],label=r'CT roots 4d',lw=0.5)
axs.plot(df_aba['Time'],media_aba[10],label=r'Roots 4d 25 mg/mL',lw=0.5,alpha=0.7)
axs.plot(df_aba['Time'],media_aba[11],label=r'Roots 4d 50 mg/mL',lw=0.5,alpha=0.7)

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
altura1=0.5 #posição em y da altura das linhas
altura2=0.48
for i in range(len(df_aba['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_aba['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_aba['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_aba['Time'][peaks_l[0][i]],df_aba['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_aba['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_aba['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_aba['Time'][peaks_l[0][i]],df_aba['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_aba['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_aba['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('aba_roots_4d.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 


plt.close(fig)


# # HIDRICO

# In[42]:


df_h = pd.read_csv(r'E:\Doc\Cap 2 - Tratadas_HPLC_Evelu\Analise_HPLC\RESULTADOS_PROCESSADOS\Figures_cromatograma\hidrico.csv',sep=',', decimal=',')#,index_col=None


# In[43]:


for i in range(len(df_h.columns)):
    print(i,df_h.columns[i])


# In[44]:


# A = 31
# B = 34

# SNP4 = np.zeros((B-A+1,len(df_h)))

# for i in range (A,B+1):
#     SNP4[i-A]=df_h[df_h.columns[i]]

# df2_snp = df_h.drop(df_h.columns[[31,32,33,34]],axis = 1)

media_h=np.zeros((14,len(df_h)))
# media_h2=np.zeros(len(SNP4[0]))
for k in range(len(df_h)):
    for i in range(1,len(df_h.columns)):
        if i % 5 == 0:
            media_h[int(i/5)-1][k]=np.average((df_h[df_h.columns[i-4]][k],df_h[df_h.columns[i-3]][k],
                                              df_h[df_h.columns[i-2]][k],df_h[df_h.columns[i-1]][k],
                                              df_h[df_h.columns[i]][k]))

for i in range(1,len(df_h.columns)):
    if i % 5 == 0:
        print(int(i/5)-1,df_h.columns[i])
        
# for k in range(len(UV4)):       
#     media_h2[k]=np.average((SNP4[0],SNP4[1],SNP4[2],SNP4[3]))


# In[45]:


num=0
peaks_l = find_peaks(media_h[1], height = 0.001, prominence=0.005, distance=20)
picos_l = peaks_l[1]['peak_heights']
label_size=6.5
plots_em_x=1
plots_em_y=1


fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_h['Time'],media_h[8],label=r'CT leaves T1',lw=0.5)
#axs.plot(df_h['Time'],media_h[0],label=r'Leaves T0',lw=0.5,alpha=0.7)
axs.plot(df_h['Time'],media_h[1],label=r'Leaves T1',lw=0.5,alpha=0.7)

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
altura1=0.25 #posição em y da altura das linhas
altura2=0.23
for i in range(len(df_h['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_h['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_h['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_h['Time'][peaks_l[0][i]],df_h['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_h['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_h['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_h['Time'][peaks_l[0][i]],df_h['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_h['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_h['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('h_leaves_t1.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 

peaks_l = find_peaks(media_h[1], height = 0.001, prominence=0.005, distance=20)
picos_l = peaks_l[1]['peak_heights']
label_size=6.5
plots_em_x=1
plots_em_y=1

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_h['Time'],media_h[0],label=r'CT leaves T0',lw=0.5)
#axs.plot(df_h['Time'],media_h[0],label=r'Leaves T0',lw=0.5,alpha=0.7)
axs.plot(df_h['Time'],media_h[1],label=r'Leaves T1',lw=0.5,alpha=0.7)

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
altura1=0.25 #posição em y da altura das linhas
altura2=0.23
for i in range(len(df_h['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_h['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_h['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_h['Time'][peaks_l[0][i]],df_h['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_h['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_h['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_h['Time'][peaks_l[0][i]],df_h['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_h['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_h['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('h_leaves_t1_t0.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 




peaks_l = find_peaks(media_h[2], height = 0.001, prominence=0.005, distance=20)
picos_l = peaks_l[1]['peak_heights']
label_size=6.5

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_h['Time'],media_h[9],label=r'CT leaves T2',lw=0.5)
axs.plot(df_h['Time'],media_h[2],label=r'Leaves T2',lw=0.5,alpha=0.7)

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
altura1=0.25 #posição em y da altura das linhas
altura2=0.23
for i in range(len(df_h['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_h['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_h['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_h['Time'][peaks_l[0][i]],df_h['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_h['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_h['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_h['Time'][peaks_l[0][i]],df_h['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_h['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_h['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('h_leaves_t2.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 

peaks_l = find_peaks(media_h[2], height = 0.001, prominence=0.005, distance=20)
picos_l = peaks_l[1]['peak_heights']
label_size=6.5

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_h['Time'],media_h[0],label=r'CT leaves T0',lw=0.5)
axs.plot(df_h['Time'],media_h[2],label=r'Leaves T2',lw=0.5,alpha=0.7)

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
altura1=0.25 #posição em y da altura das linhas
altura2=0.23
for i in range(len(df_h['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_h['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_h['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_h['Time'][peaks_l[0][i]],df_h['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_h['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_h['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_h['Time'][peaks_l[0][i]],df_h['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_h['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_h['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('h_leaves_t2_t0.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 




peaks_l = find_peaks(media_h[3], height = 0.001, prominence=0.005, distance=20)
picos_l = peaks_l[1]['peak_heights']
label_size=6.5

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_h['Time'],media_h[10],label=r'CT Leaves T3',lw=0.5)
axs.plot(df_h['Time'],media_h[3],label=r'Leaves T3',lw=0.5,alpha=0.7)

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
altura1=1.0 #posição em y da altura das linhas
altura2=0.97
for i in range(len(df_h['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_h['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_h['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_h['Time'][peaks_l[0][i]],df_h['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_h['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_h['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_h['Time'][peaks_l[0][i]],df_h['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_h['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_h['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('h_leaves_t3.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 



peaks_l = find_peaks(media_h[3], height = 0.001, prominence=0.005, distance=20)
picos_l = peaks_l[1]['peak_heights']
label_size=6.5

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_h['Time'],media_h[0],label=r'CT Leaves T0',lw=0.5)
axs.plot(df_h['Time'],media_h[3],label=r'Leaves T3',lw=0.5,alpha=0.7)

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
altura1=1.0 #posição em y da altura das linhas
altura2=0.97
for i in range(len(df_h['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_h['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_h['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_h['Time'][peaks_l[0][i]],df_h['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_h['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_h['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_h['Time'][peaks_l[0][i]],df_h['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_h['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_h['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('h_leaves_t3_t0.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 



peaks_l = find_peaks(media_h[5], height = 0.001, prominence=0.005, distance=20)
picos_l = peaks_l[1]['peak_heights']
label_size=6.5

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_h['Time'],media_h[11],label=r'CT Roots T1',lw=0.5)
#axs.plot(df_h['Time'],media_h[4],label=r'Roots T0',lw=0.5,alpha=0.7)
axs.plot(df_h['Time'],media_h[5],label=r'Roots T1',lw=0.5,alpha=0.7)

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
altura1=0.6 #posição em y da altura das linhas
altura2=0.58
for i in range(len(df_h['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_h['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_h['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_h['Time'][peaks_l[0][i]],df_h['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_h['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_h['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_h['Time'][peaks_l[0][i]],df_h['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_h['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_h['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('h_roots_t1.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500)

peaks_l = find_peaks(media_h[5], height = 0.001, prominence=0.005, distance=20)
picos_l = peaks_l[1]['peak_heights']
label_size=6.5

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_h['Time'],media_h[0],label=r'CT Roots T0',lw=0.5)
#axs.plot(df_h['Time'],media_h[4],label=r'Roots T0',lw=0.5,alpha=0.7)
axs.plot(df_h['Time'],media_h[5],label=r'Roots T1',lw=0.5,alpha=0.7)

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
altura1=0.6 #posição em y da altura das linhas
altura2=0.58
for i in range(len(df_h['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_h['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_h['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_h['Time'][peaks_l[0][i]],df_h['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_h['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_h['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_h['Time'][peaks_l[0][i]],df_h['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_h['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_h['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('h_roots_t1_t0.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500)



peaks_l = find_peaks(media_h[6], height = 0.001, prominence=0.005, distance=20)
picos_l = peaks_l[1]['peak_heights']
label_size=6.5

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_h['Time'],media_h[12],label=r'CT Roots T2',lw=0.5)
axs.plot(df_h['Time'],media_h[6],label=r'Roots T2',lw=0.5,alpha=0.7)

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
altura1=0.45 #posição em y da altura das linhas
altura2=0.43
for i in range(len(df_h['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_h['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_h['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_h['Time'][peaks_l[0][i]],df_h['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_h['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_h['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_h['Time'][peaks_l[0][i]],df_h['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_h['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_h['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('h_roots_t2.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 



peaks_l = find_peaks(media_h[6], height = 0.001, prominence=0.005, distance=20)
picos_l = peaks_l[1]['peak_heights']
label_size=6.5

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_h['Time'],media_h[0],label=r'CT Roots T0',lw=0.5)
axs.plot(df_h['Time'],media_h[6],label=r'Roots T2',lw=0.5,alpha=0.7)

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
altura1=0.45 #posição em y da altura das linhas
altura2=0.43
for i in range(len(df_h['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_h['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_h['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_h['Time'][peaks_l[0][i]],df_h['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_h['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_h['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_h['Time'][peaks_l[0][i]],df_h['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_h['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_h['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('h_roots_t2_t0.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 







peaks_l = find_peaks(media_h[7], height = 0.001, prominence=0.005, distance=20)
picos_l = peaks_l[1]['peak_heights']
label_size=6.5

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_h['Time'],media_h[13],label=r'CT Roots T3',lw=0.5)
axs.plot(df_h['Time'],media_h[7],label=r'Roots T3',lw=0.5,alpha=0.7)

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
altura1=0.35 #posição em y da altura das linhas
altura2=0.33
for i in range(len(df_h['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_h['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_h['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_h['Time'][peaks_l[0][i]],df_h['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_h['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_h['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_h['Time'][peaks_l[0][i]],df_h['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_h['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_h['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('h_roots_t3.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500)

peaks_l = find_peaks(media_h[7], height = 0.001, prominence=0.005, distance=20)
picos_l = peaks_l[1]['peak_heights']
label_size=6.5

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_h['Time'],media_h[0],label=r'CT Roots T0',lw=0.5)
axs.plot(df_h['Time'],media_h[7],label=r'Roots T3',lw=0.5,alpha=0.7)

axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica-Normal']})
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
altura1=0.35 #posição em y da altura das linhas
altura2=0.33
for i in range(len(df_h['Time'][peaks_l[0]])): #andar em todo os tempos que tem picos
    if (df_h['Time'][peaks_l[0][i]]) < 35: #selecionar T menor que 35 min
        plt.text(df_h['Time'][peaks_l[0][i]]+0.1,picos_l[i]*0.98,'%s'%num,fontsize=1.5) #escrever numeração dos picos
        num+=1
        if i%2==0: #seleciona linhas pares. se entrar fazer a linha cinza e escrever o tempo em cima dela
            plt.plot((df_h['Time'][peaks_l[0][i]],df_h['Time'][peaks_l[0][i]]),(picos_l[i],altura1),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_h['Time'][peaks_l[0][i]]-0.2,altura1+0.001,'%.1f'%df_h['Time'][peaks_l[0][i]],fontsize=1.5)
        else: #seleciona linhas impares.
            plt.plot((df_h['Time'][peaks_l[0][i]],df_h['Time'][peaks_l[0][i]]),(picos_l[i],altura2),c='grey',alpha=0.8,lw=0.1,ls='--')
            plt.text(df_h['Time'][peaks_l[0][i]]-0.2,altura2+0.001,'%.1f'%df_h['Time'][peaks_l[0][i]],fontsize=1.5)
axs.legend(fontsize=label_size, loc='upper center', bbox_to_anchor=(0.4, 1.15), ncol=3, 
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('h_roots_t3_t0.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500)

plt.close(fig)


# In[ ]:





# In[39]:









# In[ ]:




