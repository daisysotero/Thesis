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


# In[3]:


# plt.rc('text.latex', preamble=r'\usepackage{amsmath} \usepackage{siunitx}')
label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_T[0],c='lime',label='Leaves 24°C',lw=0.5)
axs.plot(df_T['Time'],media_T[1],c='darkgreen',label='Leaves 50°C',lw=0.5)
axs.plot(df_T['Time'],media_T[2],c='tan',label='Roots 24°C',lw=0.5)
axs.plot(df_T['Time'],media_T[3],c='sienna',label='Roots 50°C',lw=0.5)
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')

# axs.set_xlim(3.5,25)
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
#axs.yaxis.get_major_formatter()._usetex = False
#axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('temp.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 
plt.close(fig)

# plt.rc('text.latex', preamble=r'\usepackage{amsmath} \usepackage{siunitx}')
label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_T[0],c='lime',label='Leaves 24°C',lw=0.5)
axs.plot(df_T['Time'],media_T[1],c='darkgreen',label='Leaves 50°C',lw=0.5)
axs.plot(df_T['Time'],media_T[2],c='tan',label='Roots 24°C',lw=0.5)
axs.plot(df_T['Time'],media_T[3],c='sienna',label='Roots 50°C',lw=0.5)
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')

axs.set_xlim(3.5,25)
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
#axs.yaxis.get_major_formatter()._usetex = False
#axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('temp2.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 
plt.close(fig)

# plt.rc('text.latex', preamble=r'\usepackage{amsmath} \usepackage{siunitx}')
label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_T[1]-media_T[0],c='C2',label='Leaves 50°C',lw=0.5)
# axs.plot(df_T['Time'],,c='darkgreen',label='Leaves 50°C',lw=0.5)
axs.plot(df_T['Time'],media_T[3]-media_T[2],c='C5',label='Roots 50°C',lw=0.5)
# axs.plot(df_T['Time'],,c='sienna',label='Roots 50°C',lw=0.5)
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')

# axs.set_xlim(3.5,25)
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
#axs.yaxis.get_major_formatter()._usetex = False
#axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('temp_dif.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 
plt.close(fig)

# plt.rc('text.latex', preamble=r'\usepackage{amsmath} \usepackage{siunitx}')
label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_T[1]-media_T[0],c='C2',label='Leaves 50°C',lw=0.5)
# axs.plot(df_T['Time'],,c='darkgreen',label='Leaves 50°C',lw=0.5)
axs.plot(df_T['Time'],media_T[3]-media_T[2],c='C5',label='Roots 50°C',lw=0.5)
# axs.plot(df_T['Time'],,c='sienna',label='Roots 50°C',lw=0.5)
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')

axs.set_xlim(3,30)
axs.legend(fontsize=label_size, loc = "upper right",  
           #bbox_to_anchor = (0.6, 0.99),ncol=1, 
           fancybox=False,frameon=False)
#axs.yaxis.get_major_formatter()._usetex = False
#axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('temp2_dif.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 
plt.close(fig)


# In[17]:


peaks = find_peaks(media_T[3], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df_T['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_T[3],label='Roots 50°C',lw=0.5)
axs.scatter(tempo,picos,label='Roots 50°C',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_T['Time'][peaks[0][i]] < 35.0:
        plt.text(df_T['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_T['Time'][peaks[0][i]],fontsize=2)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('Roots_50°C_time.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

###########

peaks = find_peaks(media_T[1], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df_T['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_T[1],label='Leaves 50°C',lw=0.5)
axs.scatter(tempo,picos,label='Leaves 50°C',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_T['Time'][peaks[0][i]] < 35.0:
        plt.text(df_T['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_T['Time'][peaks[0][i]],fontsize=2)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('Leaves_50°C_time.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 
plt.close(fig)


# In[3]:


altura1=0.18
altura2=0.2
for i in range(len(df_T['Time'][peaks[0]])):
    if (df_T['Time'][peaks[0][i]]) < 35:
        if i%2==0:
            plt.plot((df_T['Time'][peaks[0][i]],df_T['Time'][peaks[0][i]]),(picos[i],altura1),c='grey',alpha=0.5,lw=0.1,ls='--')
            plt.text(df_T['Time'][peaks[0][i]]-0.2,altura1+0.001,'%.1f'%df_T['Time'][peaks[0][i]],fontsize=2)
        else:
            plt.plot((df_T['Time'][peaks[0][i]],df_T['Time'][peaks[0][i]]),(picos[i],altura2),c='grey',alpha=0.5,lw=0.1,ls='--')
            plt.text(df_T['Time'][peaks[0][i]]-0.2,altura2+0.001,'%.1f'%df_T['Time'][peaks[0][i]],fontsize=2)


# # UV

# In[18]:


df_uv = pd.read_csv(r'E:\Doc\Cap 2 - Tratadas_HPLC_Evelu\Analise_HPLC\RESULTADOS_PROCESSADOS\Figures_cromatograma\uv.csv',sep=',', decimal=',')#,index_col=None


# In[19]:


for i in range(len(df_uv.columns)):
    print(i,df_uv.columns[i])


# In[25]:


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
        


# In[32]:


peaks = find_peaks(media_UV2, height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_UV2,label='uv_roots24h_time',lw=0.5)
axs.scatter(tempo,picos,label='uv_roots24h_time',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_T['Time'][peaks[0][i]] < 35.0:
        plt.text(df_T['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_T['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('uv_roots24h_time.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################

peaks = find_peaks(media_UV[6], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_UV[6],label='uv_roots48h_time',lw=0.5)
axs.scatter(tempo,picos,label='uv_roots48h_time',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_T['Time'][peaks[0][i]] < 35.0:
        plt.text(df_T['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_T['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('uv_roots48h_time.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################


peaks = find_peaks(media_UV[4], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_UV[4],label='uv_leaves24h',lw=0.5)
axs.scatter(tempo,picos,label='uv_leaves24h',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_T['Time'][peaks[0][i]] < 35.0:
        plt.text(df_T['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_T['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('uv_leaves24h_time.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################

peaks = find_peaks(media_UV[5], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_UV[5],label='uv_leaves48h',lw=0.5)
axs.scatter(tempo,picos,label='uv_leaves48h',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_T['Time'][peaks[0][i]] < 35.0:
        plt.text(df_T['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_T['Time'][peaks[0][i]],fontsize=2)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('uv_leaves48h_time.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

plt.close(fig)


# In[ ]:





# In[7]:


label_size=8
plots_em_x=1
plots_em_y=1

colors=['#00979299','#efda0596','#009792fd','#fcd000ff','#66cd00ff','#006400ff','#8b4513ff']
labels=['CT leaves 24h','CT roots 24h','CT leaves 48h','CT roots 48h','Leaves 24h','Leaves 48h','Roots 48h']
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))

# for i in range (7):
#     axs.plot(df2_uv['Time'],media_UV[i],c=colors[i],label=labels[i],lw=0.5)

axs.plot(df2_uv['Time'],media_UV[0],c=colors[0],label=labels[0],lw=0.5)
axs.plot(df2_uv['Time'],media_UV[4],c=colors[4],label=labels[4],lw=0.5)
axs.plot(df2_uv['Time'],media_UV[2],c=colors[2],label=labels[2],lw=0.5)
axs.plot(df2_uv['Time'],media_UV[5],c=colors[5],label=labels[5],lw=0.5)
axs.plot(df2_uv['Time'],media_UV[1],c=colors[1],label=labels[1],lw=0.5)
axs.plot(df2_uv['Time'],media_UV2,c='#8b7355ff',label='Roots 24h',lw=0.5)
axs.plot(df2_uv['Time'],media_UV[3],c=colors[3],label=labels[3],lw=0.5)
axs.plot(df2_uv['Time'],media_UV[6],c=colors[6],label=labels[6],lw=0.5)

# axs.set_xlim(3.5,37)  
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
axs.legend(fontsize=label_size, loc = "upper right",  
           #bbox_to_anchor = (0.34, 0.99),ncol=1, 
           fancybox=False,frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('UV.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
plt.close(fig)



fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))

# for i in range (7):
#     axs.plot(df2_uv['Time'],media_UV[i],c=colors[i],label=labels[i],lw=0.5)

axs.plot(df2_uv['Time'],media_UV[0],c=colors[0],label=labels[0],lw=0.5)
axs.plot(df2_uv['Time'],media_UV[4],c=colors[4],label=labels[4],lw=0.5)
axs.plot(df2_uv['Time'],media_UV[2],c=colors[2],label=labels[2],lw=0.5)
axs.plot(df2_uv['Time'],media_UV[5],c=colors[5],label=labels[5],lw=0.5)
axs.plot(df2_uv['Time'],media_UV[1],c=colors[1],label=labels[1],lw=0.5)
axs.plot(df2_uv['Time'],media_UV2,c='#8b7355ff',label='Roots 24h',lw=0.5)
axs.plot(df2_uv['Time'],media_UV[3],c=colors[3],label=labels[3],lw=0.5)
axs.plot(df2_uv['Time'],media_UV[6],c=colors[6],label=labels[6],lw=0.5)

axs.set_xlim(3.5,37)  
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
axs.legend(fontsize=label_size, loc = "upper right",  
           #bbox_to_anchor = (0.34, 0.99),ncol=1, 
           fancybox=False,frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('UV2.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
plt.close(fig)


fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))


labels=['CT leaves 24h','CT roots 24h','CT leaves 48h','CT roots 48h','Leaves 24h','Leaves 48h','Roots 48h']


labels1=['Leaves 24h',
        'Leaves 48h',
        'Roots 24h',
        'Roots 48h']

colors1=['springgreen','C2','chocolate','C5']
# for i in range (7):
#     axs.plot(df2_uv['Time'],media_UV[i],c=colors[i],label=labels[i],lw=0.5)

axs.plot(df2_uv['Time'],media_UV[4]-media_UV[0],c=colors1[0],label=labels1[0],lw=0.5)
# axs.plot(df2_uv['Time'],,c=colors[4],label=labels[4],lw=0.5)
axs.plot(df2_uv['Time'],media_UV[5]-media_UV[2],c=colors1[1],label=labels1[1],lw=0.5)
# axs.plot(df2_uv['Time'],,c=colors[5],label=labels[5],lw=0.5)
axs.plot(df2_uv['Time'],media_UV2-media_UV[1],c=colors1[2],label=labels1[2],lw=0.5)
# axs.plot(df2_uv['Time'],,c='#8b7355ff',label='Roots 24h',lw=0.5)
axs.plot(df2_uv['Time'],media_UV[6]-media_UV[3],c=colors1[3],label=labels1[3],lw=0.5)
# axs.plot(df2_uv['Time'],,c=colors[6],label=labels[6],lw=0.5)

# axs.set_xlim(3.5,37)  
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.legend(fontsize=label_size, loc = "upper right",  
           #bbox_to_anchor = (0.45, 0.99),ncol=1, 
           fancybox=False,frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('UV_diff.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
plt.close(fig)



fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))


labels=['CT leaves 24h','CT roots 24h','CT leaves 48h','CT roots 48h','Leaves 24h','Leaves 48h','Roots 48h']


labels1=['Leaves 24h',
        'Leaves 48h',
        'Roots 24h',
        'Roots 48h']
# for i in range (7):
#     axs.plot(df2_uv['Time'],media_UV[i],c=colors[i],label=labels[i],lw=0.5)

axs.plot(df2_uv['Time'],media_UV[4]-media_UV[0],c=colors1[0],label=labels1[0],lw=0.5)
# axs.plot(df2_uv['Time'],,c=colors[4],label=labels[4],lw=0.5)
axs.plot(df2_uv['Time'],media_UV[5]-media_UV[2],c=colors1[1],label=labels1[1],lw=0.5)
# axs.plot(df2_uv['Time'],,c=colors[5],label=labels[5],lw=0.5)
axs.plot(df2_uv['Time'],media_UV2-media_UV[1],c=colors1[2],label=labels1[2],lw=0.5)
# axs.plot(df2_uv['Time'],,c='#8b7355ff',label='Roots 24h',lw=0.5)
axs.plot(df2_uv['Time'],media_UV[6]-media_UV[3],c=colors1[3],label=labels1[3],lw=0.5)
# axs.plot(df2_uv['Time'],,c=colors[6],label=labels[6],lw=0.5)

axs.set_xlim(3.5,37)  
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.legend(fontsize=label_size, loc = "upper right",  
           #bbox_to_anchor = (0.45, 0.99),ncol=1, 
           fancybox=False,frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('UV2_diff.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
plt.close(fig)


# In[8]:


UV4.shape


# # MEJA

# In[33]:


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


# In[35]:



peaks = find_peaks(media_meja[4], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_meja[4],label='meja_leaves2d_40uM',lw=0.5)
axs.scatter(tempo,picos,label='meja_leaves2d_40uM',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_T['Time'][peaks[0][i]] < 35.0:
        plt.text(df_T['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_T['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('meja_leaves2d_40uM.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################

peaks = find_peaks(media_meja[5], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_meja[5],label='meja_leaves2d_100uM',lw=0.5)
axs.scatter(tempo,picos,label='meja_leaves2d_100uM',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_T['Time'][peaks[0][i]] < 35.0:
        plt.text(df_T['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_T['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('meja_leaves2d_100uM.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################


peaks = find_peaks(media_meja[6], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_meja[6],label='meja_roots2d_40uM',lw=0.5)
axs.scatter(tempo,picos,label='meja_roots2d_40uM',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_T['Time'][peaks[0][i]] < 35.0:
        plt.text(df_T['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_T['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('meja_roots2d_40uM.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################

peaks = find_peaks(media_meja[7], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_meja[7],label='meja_roots2d_100uM',lw=0.5)
axs.scatter(tempo,picos,label='meja_roots2d_100uM',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_T['Time'][peaks[0][i]] < 35.0:
        plt.text(df_T['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_T['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('meja_roots2d_100uM.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################
#####################

peaks = find_peaks(media_meja[8], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_meja[8],label='meja_leaves4d_40uM',lw=0.5)
axs.scatter(tempo,picos,label='meja_leaves4d_40uM',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_T['Time'][peaks[0][i]] < 35.0:
        plt.text(df_T['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_T['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('meja_leaves4d_40uM.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################

peaks = find_peaks(media_meja[9], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_meja[9],label='meja_leaves4d_100uM',lw=0.5)
axs.scatter(tempo,picos,label='meja_leaves4d_100uM',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_T['Time'][peaks[0][i]] < 35.0:
        plt.text(df_T['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_T['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('meja_leaves4d_100uM.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################


peaks = find_peaks(media_meja[10], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_meja[10],label='meja_roots4d_40uM',lw=0.5)
axs.scatter(tempo,picos,label='meja_roots4d_40uM',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_T['Time'][peaks[0][i]] < 35.0:
        plt.text(df_T['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_T['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('meja_roots4d_40uM.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################

peaks = find_peaks(media_meja[11], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_meja[11],label='meja_roots4d_100uM',lw=0.5)
axs.scatter(tempo,picos,label='meja_roots4d_100uM',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_T['Time'][peaks[0][i]] < 35.0:
        plt.text(df_T['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_T['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('meja_roots4d_100uM.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 


# In[ ]:





# In[10]:


label_size=5.5

plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))

axs.plot(df_meja['Time'],media_meja[0],c='#00979299',label='CT leaves 2d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[4],c='#15ff156c',label='Leaves 40 µM 2d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[5],c='#66cd00ff',label='Leaves 100 µM 2d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[1],c='#efda0596',label='CT roots 2d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[6],c='#c97d84ff',label='Roots 40 µM 2d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[7],c='#ffa54fff',label='Roots 100 µM 2d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[2],c='#009792fd',label='CT leaves 4d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[8],c='#a9f260ff',label='Leaves 40 µM 4d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[9],c='#006400ff',label='Leaves 100 µM 4d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[3],c='#fcd000ff',label='CT roots 4d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[10],c='#8b7355ff',label='Roots 40 µM 4d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[11],c='#8b4513ff',label='Roots 100 µM 4d',lw=0.5)
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')

# axs.set_xlim(3.5,30)
axs.legend(fontsize=label_size, loc = "upper right",  
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           fancybox=False,frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('meja.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
plt.close(fig)


fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))

axs.plot(df_meja['Time'],media_meja[0],c='#00979299',label='CT leaves 2d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[4],c='#15ff156c',label='Leaves 40 µM 2d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[5],c='#66cd00ff',label='Leaves 100 µM 2d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[1],c='#efda0596',label='CT roots 2d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[6],c='#c97d84ff',label='Roots 40 µM 2d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[7],c='#ffa54fff',label='Roots 100 µM 2d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[2],c='#009792fd',label='CT leaves 4d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[8],c='#a9f260ff',label='Leaves 40 µM 4d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[9],c='#006400ff',label='Leaves 100 µM 4d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[3],c='#fcd000ff',label='CT roots 4d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[10],c='#8b7355ff',label='Roots 40 µM 4d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[11],c='#8b4513ff',label='Roots 100 µM 4d',lw=0.5)
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')

axs.set_xlim(3.5,30)
axs.legend(fontsize=label_size, loc = "upper right",  
           #bbox_to_anchor = (0.45, 0.99),ncol=2, 
           fancybox=False,frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('meja2.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
plt.close(fig)


colors1=['aquamarine','palegreen','C2','darkgreen','antiquewhite','tan','chocolate','C5']

label_size=7

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))

# axs.plot(df_meja['Time'],media_meja[0],c='#00979299',label='CT leaves 2 day',lw=0.5)
axs.plot(df_meja['Time'],media_meja[4]-media_meja[0],c=colors1[0],label='Leaves 40 µM 2d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[5]-media_meja[0],c=colors1[1],label='Leaves 100 µM 2d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[8]-media_meja[2],c=colors1[2],label='Leaves 40 µM 4d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[9]-media_meja[2],c=colors1[3],label='Leaves 100 µM 4d',lw=0.5)

# axs.plot(df_meja['Time'],media_meja[1],c='#efda0596',label='CT roots 2 day',lw=0.5)
axs.plot(df_meja['Time'],media_meja[6]-media_meja[1],c=colors1[4],label='Roots 40 µM 2d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[7]-media_meja[1],c=colors1[5],label='Roots 100 µM 2d',lw=0.5)
# axs.plot(df_meja['Time'],media_meja[2],c='#009792fd',label='CT leaves 4 day',lw=0.5)

# axs.plot(df_meja['Time'],media_meja[3],c='#fcd000ff',label='CT roots 4 day',lw=0.5)
axs.plot(df_meja['Time'],media_meja[10]-media_meja[3],c=colors1[6],label='Roots 40 µM 4d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[11]-media_meja[3],c=colors1[7],label='Roots 100 µM 4d',lw=0.5)
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')

# axs.set_xlim(3.5,30)
axs.legend(fontsize=label_size, loc = "upper right",  
           #bbox_to_anchor = (0.4, 0.99),ncol=1,  
           fancybox=False,frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('meja_diff.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
plt.close(fig)

label_size=7
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
colors1=['aquamarine','palegreen','C2','darkgreen','antiquewhite','tan','chocolate','C5']
# axs.plot(df_meja['Time'],media_meja[0],c='#00979299',label='CT leaves 2 day',lw=0.5)
axs.plot(df_meja['Time'],media_meja[4]-media_meja[0],c=colors1[0],label='Leaves 40 µM 2d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[5]-media_meja[0],c=colors1[1],label='Leaves 100 µM 2d',lw=0.5)
# axs.plot(df_meja['Time'],media_meja[1],c='#efda0596',label='CT roots 2 day',lw=0.5)
# axs.plot(df_meja['Time'],media_meja[2],c='#009792fd',label='CT leaves 4 day',lw=0.5)
axs.plot(df_meja['Time'],media_meja[8]-media_meja[2],c=colors1[2],label='Leaves 40 µM 4d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[9]-media_meja[2],c=colors1[3],label='Leaves 100 µM 4d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[6]-media_meja[1],c=colors1[4],label='Roots 40 µM 2d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[7]-media_meja[1],c=colors1[5],label='Roots 100 µM 2d',lw=0.5)
# axs.plot(df_meja['Time'],media_meja[3],c='#fcd000ff',label='CT roots 4 day',lw=0.5)
axs.plot(df_meja['Time'],media_meja[10]-media_meja[3],c=colors1[6],label='Roots 40 µM 4d',lw=0.5)
axs.plot(df_meja['Time'],media_meja[11]-media_meja[3],c=colors1[7],label='Roots 100 µM 4d',lw=0.5)
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')

axs.set_xlim(3.5,30)
axs.legend(fontsize=label_size, loc = "upper right",  
           #bbox_to_anchor = (0.5, 0.99),ncol=1, 
           fancybox=False,frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('meja2_diff.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
plt.close(fig)


# # AS

# In[36]:


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


# In[37]:



peaks = find_peaks(media_as[4], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_as[4],label='as_leaves2d_1mM',lw=0.5)
axs.scatter(tempo,picos,label='as_leaves2d_1mM',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_T['Time'][peaks[0][i]] < 35.0:
        plt.text(df_T['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_T['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('as_leaves2d_1mM.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################

peaks = find_peaks(media_as[5], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_as[5],label='as_leaves2d_2mM',lw=0.5)
axs.scatter(tempo,picos,label='as_leaves2d_2mM',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_T['Time'][peaks[0][i]] < 35.0:
        plt.text(df_T['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_T['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('as_leaves2d_2mM.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################


peaks = find_peaks(media_as[6], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_as[6],label='as_roots2d_1mM',lw=0.5)
axs.scatter(tempo,picos,label='as_roots2d_1mM',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_T['Time'][peaks[0][i]] < 35.0:
        plt.text(df_T['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_T['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('as_roots2d_1mM.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################

peaks = find_peaks(media_as[7], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_as[7],label='as_roots2d_2mM',lw=0.5)
axs.scatter(tempo,picos,label='as_roots2d_2mM',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_T['Time'][peaks[0][i]] < 35.0:
        plt.text(df_T['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_T['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('as_roots2d_2mM.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################
#####################

peaks = find_peaks(media_as[8], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_as[8],label='as_leaves4d_1mM',lw=0.5)
axs.scatter(tempo,picos,label='as_leaves4d_1mM',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_T['Time'][peaks[0][i]] < 35.0:
        plt.text(df_T['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_T['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('as_leaves4d_1mM.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################

peaks = find_peaks(media_as[9], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_as[9],label='as_leaves4d_2mM',lw=0.5)
axs.scatter(tempo,picos,label='as_leaves4d_2mM',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_T['Time'][peaks[0][i]] < 35.0:
        plt.text(df_T['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_T['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('as_leaves4d_2mM.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################


peaks = find_peaks(media_as[10], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_as[10],label='as_roots4d_1mM',lw=0.5)
axs.scatter(tempo,picos,label='as_roots4d_1mM',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_T['Time'][peaks[0][i]] < 35.0:
        plt.text(df_T['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_T['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('as_roots4d_1mM.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################

peaks = find_peaks(media_as[11], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_as[11],label='as_roots4d_2mM',lw=0.5)
axs.scatter(tempo,picos,label='as_roots4d_2mM',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_T['Time'][peaks[0][i]] < 35.0:
        plt.text(df_T['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_T['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('as_roots4d_2mM.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 


# In[ ]:





# In[12]:


# plt.rc('text.latex', preamble=r'\usepackage{amsmath} \usepackage{siunitx}')
label_size=6.5
plots_em_x=1
plots_em_y=1


fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))

axs.plot(df_as['Time'],media_as[0],c='#00979299',label='CT leaves 2d',lw=0.5)
axs.plot(df_as['Time'],media_as[4],c='#15ff156c',label='Leaves 1 mM 2d',lw=0.5)
axs.plot(df_as['Time'],media_as[5],c='#66cd00ff',label='Leaves 2 mM 2d',lw=0.5)
axs.plot(df_as['Time'],media_as[1],c='#efda0596',label='CT roots 2d',lw=0.5)
axs.plot(df_as['Time'],media_as[6],c='#c97d84ff',label='Roots 1 mM 2d',lw=0.5)
axs.plot(df_as['Time'],media_as[7],c='#ffa54fff',label='Roots 2 mM 2d',lw=0.5)
axs.plot(df_as['Time'],media_as[2],c='#009792fd',label='CT leaves 4d',lw=0.5)
axs.plot(df_as['Time'],media_as[8],c='#a9f260ff',label='Leaves 1 mM 4d',lw=0.5)
axs.plot(df_as['Time'],media_as[9],c='#006400ff',label='Leaves 2 mM 4d',lw=0.5)
axs.plot(df_as['Time'],media_as[3],c='#fcd000ff',label='CT roots 4d',lw=0.5)
axs.plot(df_as['Time'],media_as[10],c='#8b7355ff',label='Roots 1 mM 4d',lw=0.5)
axs.plot(df_as['Time'],media_as[11],c='#8b4513ff',label='Roots 2 mM 4d',lw=0.5)
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
axs.legend(fontsize=label_size, loc = "upper right",  
           #bbox_to_anchor = (0.32, 0.99),ncol=2, 
           fancybox=False,frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('AS.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
plt.close(fig)


fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))

axs.plot(df_as['Time'],media_as[0],c='#00979299',label='CT leaves 2d',lw=0.5)
axs.plot(df_as['Time'],media_as[4],c='#15ff156c',label='Leaves 1 mM 2d',lw=0.5)
axs.plot(df_as['Time'],media_as[5],c='#66cd00ff',label='Leaves 2 mM 2d',lw=0.5)
axs.plot(df_as['Time'],media_as[1],c='#efda0596',label='CT roots 2d',lw=0.5)
axs.plot(df_as['Time'],media_as[6],c='#c97d84ff',label='Roots 1 mM 2d',lw=0.5)
axs.plot(df_as['Time'],media_as[7],c='#ffa54fff',label='Roots 2 mM 2d',lw=0.5)
axs.plot(df_as['Time'],media_as[2],c='#009792fd',label='CT leaves 4d',lw=0.5)
axs.plot(df_as['Time'],media_as[8],c='#a9f260ff',label='Leaves 1 mM 4d',lw=0.5)
axs.plot(df_as['Time'],media_as[9],c='#006400ff',label='Leaves 2 mM 4d',lw=0.5)
axs.plot(df_as['Time'],media_as[3],c='#fcd000ff',label='CT roots 4d',lw=0.5)
axs.plot(df_as['Time'],media_as[10],c='#8b7355ff',label='Roots 1 mM 4d',lw=0.5)
axs.plot(df_as['Time'],media_as[11],c='#8b4513ff',label='Roots 2 mM 4d',lw=0.5)
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')

axs.set_xlim(3.5,37)
axs.legend(fontsize=label_size, loc = "upper right",  
           #bbox_to_anchor = (0.35, 0.999),ncol=2, 
           fancybox=False,frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('AS2.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
plt.close(fig)

colors1=['aquamarine','palegreen','C2','darkgreen','antiquewhite','tan','chocolate','C5']

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
colors1=['aquamarine','palegreen','C2','darkgreen','antiquewhite','tan','chocolate','C5']

# axs.plot(df_as['Time'],media_as[0],c='#00979299',label='CT leaves 2 day',lw=0.5)
axs.plot(df_as['Time'],media_as[4]-media_as[0],c=colors1[0],label='Leaves 1 mM 2d',lw=0.5)
axs.plot(df_as['Time'],media_as[5]-media_as[0],c=colors1[1],label='Leaves 2 mM 2d',lw=0.5)
axs.plot(df_as['Time'],media_as[8]-media_as[2],c=colors1[2],label='Leaves 1 mM 4d',lw=0.5)
axs.plot(df_as['Time'],media_as[9]-media_as[2],c=colors1[3],label='Leaves 2 mM 4d',lw=0.5)
# axs.plot(df_as['Time'],media_as[1],c='#efda0596',label='CT roots 2 day',lw=0.5)
axs.plot(df_as['Time'],media_as[6]-media_as[1],c=colors1[4],label='Roots 1 mM 2d',lw=0.5)
axs.plot(df_as['Time'],media_as[7]-media_as[1],c=colors1[5],label='Roots 2 mM 2d',lw=0.5)
# axs.plot(df_as['Time'],media_as[2],c='#009792fd',label='CT leaves 4 day',lw=0.5)

# axs.plot(df_as['Time'],media_as[3],c='#fcd000ff',label='CT roots 4 day',lw=0.5)
axs.plot(df_as['Time'],media_as[10]-media_as[3],c=colors1[6],label='Roots 1 mM 4d',lw=0.5)
axs.plot(df_as['Time'],media_as[11]-media_as[3],c=colors1[7],label='Roots 2 mM 4d',lw=0.5)
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')

# axs.set_xlim(3.5,37)
axs.legend(fontsize=label_size, loc = "upper right",  
           #bbox_to_anchor = (0.32, 0.999),ncol=2, 
           fancybox=False,frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('AS_diff.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
# plt.close(fig)


# fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))

# # axs.plot(df_as['Time'],media_as[0],c='#00979299',label='CT leaves 2 day',lw=0.5)
# axs.plot(df_as['Time'],media_as[4]-media_as[0],c=colors1[0],label='Leaves 1 mM 2d',lw=0.5)
# axs.plot(df_as['Time'],media_as[5]-media_as[0],c=colors1[1],label='Leaves 2 mM 2d',lw=0.5)
# axs.plot(df_as['Time'],media_as[8]-media_as[2],c=colors1[2],label='Leaves 1 mM 4d',lw=0.5)
# axs.plot(df_as['Time'],media_as[9]-media_as[2],c=colors1[3],label='Leaves 2 mM 4d',lw=0.5)
# # axs.plot(df_as['Time'],media_as[1],c='#efda0596',label='CT roots 2 day',lw=0.5)
# axs.plot(df_as['Time'],media_as[6]-media_as[1],c=colors1[4],label='Roots 1 mM 2d',lw=0.5)
# axs.plot(df_as['Time'],media_as[7]-media_as[1],c=colors1[5],label='Roots 2 mM 2d',lw=0.5)
# # axs.plot(df_as['Time'],media_as[2],c='#009792fd',label='CT leaves 4 day',lw=0.5)

# # axs.plot(df_as['Time'],media_as[3],c='#fcd000ff',label='CT roots 4 day',lw=0.5)
# axs.plot(df_as['Time'],media_as[10]-media_as[3],c=colors1[6],label='Roots 1 mM 4d',lw=0.5)
# axs.plot(df_as['Time'],media_as[11]-media_as[3],c=colors1[7],label='Roots 2 mM 4d',lw=0.5)
# axs.set_ylabel(r'Absorbance difference')
# axs.set_xlabel(r'Retention time')

axs.set_xlim(5,37)
# axs.legend(fontsize=label_size, loc = "upper right",  
#            #bbox_to_anchor = (0.33, 0.999),ncol=2, 
#            fancybox=False,frameon=False)
# axs.yaxis.get_major_formatter()._usetex = False
# axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('AS2_diff.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
plt.close(fig)


# # SNP

# In[40]:


df_snp = pd.read_csv(r'E:\Doc\Cap 2 - Tratadas_HPLC_Evelu\Analise_HPLC\RESULTADOS_PROCESSADOS\Figures_cromatograma\snp.csv',sep=',', decimal=',')#,index_col=None


# In[41]:


for i in range(len(df_snp.columns)):
    print(i,df_snp.columns[i])


# In[43]:


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
        
for i in range(len(UV4[0])):       
    media_snp2[i]=np.average((SNP4[0][i],SNP4[1][i],SNP4[2][i],SNP4[3][i]))
    


# In[44]:


peaks = find_peaks(media_snp[4], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_snp['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_snp[4],label='snp_leaves2d_100mM',lw=0.5)
axs.scatter(tempo,picos,label='snp_leaves2d_100mM',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_T['Time'][peaks[0][i]] < 35.0:
        plt.text(df_T['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_T['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('snp_leaves2d_100mM.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################

peaks = find_peaks(media_snp[5], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_snp['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_snp[5],label='snp_leaves2d_200mM',lw=0.5)
axs.scatter(tempo,picos,label='snp_leaves2d_200mM',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_T['Time'][peaks[0][i]] < 35.0:
        plt.text(df_T['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_T['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('snp_leaves2d_200mM.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################


peaks = find_peaks(media_snp2, height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_snp['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_snp2,label='snp_roots2d_100mM',lw=0.5)
axs.scatter(tempo,picos,label='snp_roots2d_100mM',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_T['Time'][peaks[0][i]] < 35.0:
        plt.text(df_T['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_T['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('snp_roots2d_100mM.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################

peaks = find_peaks(media_snp[6], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_snp['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_snp[6],label='snp_roots2d_200mM',lw=0.5)
axs.scatter(tempo,picos,label='snp_roots2d_200mM',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_T['Time'][peaks[0][i]] < 35.0:
        plt.text(df_T['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_T['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('snp_roots2d_200mM.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################
#####################

peaks = find_peaks(media_snp[7], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_snp['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_snp[7],label='snp_leaves4d_100mM',lw=0.5)
axs.scatter(tempo,picos,label='snp_leaves4d_100mM',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_T['Time'][peaks[0][i]] < 35.0:
        plt.text(df_T['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_T['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('snp_leaves4d_100mM.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################

peaks = find_peaks(media_snp[8], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_snp['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_snp[8],label='snp_leaves4d_200mM',lw=0.5)
axs.scatter(tempo,picos,label='snp_leaves4d_200mM',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_T['Time'][peaks[0][i]] < 35.0:
        plt.text(df_T['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_T['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('snp_leaves4d_200mM.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################


peaks = find_peaks(media_snp[9], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_snp['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_snp[9],label='snp_roots4d_100mM',lw=0.5)
axs.scatter(tempo,picos,label='snp_roots4d_100mM',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_T['Time'][peaks[0][i]] < 35.0:
        plt.text(df_T['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_T['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('snp_roots4d_100mM.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################

peaks = find_peaks(media_snp[10], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_snp['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_T['Time'],media_snp[10],label='snp_roots4d_200mM',lw=0.5)
axs.scatter(tempo,picos,label='snp_roots4d_200mM',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_T['Time'][peaks[0][i]] < 35.0:
        plt.text(df_T['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_T['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('snp_roots4d_200mM.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 


# In[ ]:





# In[16]:


label_size=6
plots_em_x=1
plots_em_y=1

colors=['#009792fd','tan','lime','lightcoral',
         'aqua','teal','orange',
         'mediumseagreen','darkgreen','chocolate','sienna']

labels=['CT leaves 2d','CT roots 2d','CT leaves 4d','CT roots 4d',
        'Leaves 100 µM 2d','Leaves 200 µM 2d','Roots 200 µM 2d',
        'Leaves 100 µM 4d','Leaves 200 µM 4d','Roots 100 µM 4d','Roots 200 µM 4d']

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))


# for i in range (7):
#     axs.plot(df2_uv['Time'],media_snp[i],c=colors[i],label=labels[i],lw=0.5)

axs.plot(df2_snp['Time'],media_snp[0],c=colors[0],label=labels[0],lw=0.5)
axs.plot(df2_snp['Time'],media_snp[4],c=colors[4],label=labels[4],lw=0.5)
axs.plot(df2_snp['Time'],media_snp[5],c=colors[5],label=labels[5],lw=0.5)
axs.plot(df2_snp['Time'],media_snp[2],c=colors[2],label=labels[2],lw=0.5)
axs.plot(df2_snp['Time'],media_snp[7],c=colors[7],label=labels[7],lw=0.5)
axs.plot(df2_snp['Time'],media_snp[8],c=colors[8],label=labels[8],lw=0.5)
axs.plot(df2_snp['Time'],media_snp[1],c=colors[1],label=labels[1],lw=0.5)
axs.plot(df2_snp['Time'],media_snp2,c='darkgoldenrod',label='Roots 100 µM 2d',lw=0.5)
axs.plot(df2_snp['Time'],media_snp[6],c=colors[6],label=labels[6],lw=0.5)
axs.plot(df2_snp['Time'],media_snp[3],c=colors[3],label=labels[3],lw=0.5)
axs.plot(df2_snp['Time'],media_snp[9],c=colors[9],label=labels[9],lw=0.5)
axs.plot(df2_snp['Time'],media_snp[10],c=colors[10],label=labels[10],lw=0.5)

#axs.set_xlim(3.5,25)
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
axs.legend(fontsize=label_size, loc = "upper right",  
           #bbox_to_anchor = (0.25, 0.99),ncol=2, 
           fancybox=False,frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('snp.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
# plt.close(fig)

# fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))

# for i in range (7):
#     axs.plot(df2_uv['Time'],media_snp[i],c=colors[i],label=labels[i],lw=0.5)

# axs.plot(df2_snp['Time'],media_snp[0],c=colors[0],label=labels[0],lw=0.5)
# axs.plot(df2_snp['Time'],media_snp[4],c=colors[4],label=labels[4],lw=0.5)
# axs.plot(df2_snp['Time'],media_snp[5],c=colors[5],label=labels[5],lw=0.5)
# axs.plot(df2_snp['Time'],media_snp[2],c=colors[2],label=labels[2],lw=0.5)
# axs.plot(df2_snp['Time'],media_snp[7],c=colors[7],label=labels[7],lw=0.5)
# axs.plot(df2_snp['Time'],media_snp[8],c=colors[8],label=labels[8],lw=0.5)
# axs.plot(df2_snp['Time'],media_snp[1],c=colors[1],label=labels[1],lw=0.5)
# axs.plot(df2_snp['Time'],media_snp2,c='darkgoldenrod',label='Roots 100 µM 2 day',lw=0.5)
# axs.plot(df2_snp['Time'],media_snp[6],c=colors[6],label=labels[6],lw=0.5)
# axs.plot(df2_snp['Time'],media_snp[3],c=colors[3],label=labels[3],lw=0.5)
# axs.plot(df2_snp['Time'],media_snp[9],c=colors[9],label=labels[9],lw=0.5)
# axs.plot(df2_snp['Time'],media_snp[10],c=colors[10],label=labels[10],lw=0.5)

axs.set_xlim(3.5,25)
# axs.set_ylabel(r'Absorbance (280 nm)')
# axs.set_xlabel(r'Retention time')
# axs.legend(fontsize=label_size, loc = "upper left",  
#            bbox_to_anchor = (0.25, 0.99),ncol=2, 
#            fancybox=False,frameon=False)
# axs.yaxis.get_major_formatter()._usetex = False
# axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('snp2.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
plt.close(fig)

label_size=8
colors1=['aquamarine','palegreen','C2','darkgreen','antiquewhite','tan','chocolate','C5']


fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))


# for i in range (7):
#     axs.plot(df2_uv['Time'],media_snp[i],c=colors[i],label=labels[i],lw=0.5)
colors=['#009792fd','tan','lime','lightcoral',
         'aqua','teal','orange',
         'mediumseagreen','darkgreen','chocolate','sienna']

labels=['CT leaves 2d','CT roots 2d','CT leaves 4d','CT roots 4d',
        'Leaves 100 µM 2d','Leaves 200 µM 2d','Roots 200 µM 2d',
        'Leaves 100 µM 4d','Leaves 200 µM 4d','Roots 100 µM 4d','Roots 200 µM 4d']
# axs.plot(df2_snp['Time'],media_snp[0],c=colors[0],label=labels[0],lw=0.5)
axs.plot(df2_snp['Time'],media_snp[4]-media_snp[0],c=colors[4],label=labels[4],lw=0.5)
axs.plot(df2_snp['Time'],media_snp[5]-media_snp[0],c=colors[5],label=labels[5],lw=0.5)
# axs.plot(df2_snp['Time'],media_snp[2],c=colors[2],label=labels[2],lw=0.5)
axs.plot(df2_snp['Time'],media_snp[7]-media_snp[2],c=colors[7],label=labels[7],lw=0.5)
axs.plot(df2_snp['Time'],media_snp[8]-media_snp[2],c=colors[8],label=labels[8],lw=0.5)
# axs.plot(df2_snp['Time'],media_snp[1],c=colors[1],label=labels[1],lw=0.5)
axs.plot(df2_snp['Time'],media_snp2-media_snp[1],c='darkgoldenrod',label='Roots 100 µM 2d',lw=0.5)
axs.plot(df2_snp['Time'],media_snp[6]-media_snp[1],c=colors[6],label=labels[6],lw=0.5)
# axs.plot(df2_snp['Time'],media_snp[3],c=colors[3],label=labels[3],lw=0.5)
axs.plot(df2_snp['Time'],media_snp[9]-media_snp[3],c=colors[9],label=labels[9],lw=0.5)
axs.plot(df2_snp['Time'],media_snp[10]-media_snp[3],c=colors[10],label=labels[10],lw=0.5)

#axs.set_xlim(3.5,25)
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.legend(fontsize=label_size, loc = "upper right",  
           #bbox_to_anchor = (0.25, 0.99),ncol=2, 
           fancybox=False,frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('snp_diff.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
# plt.close(fig)


# fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))


# for i in range (7):
#     axs.plot(df2_uv['Time'],media_snp[i],c=colors[i],label=labels[i],lw=0.5)

# axs.plot(df2_snp['Time'],media_snp[0],c=colors[0],label=labels[0],lw=0.5)
# axs.plot(df2_snp['Time'],media_snp[4],c=colors[4],label=labels[4],lw=0.5)
# axs.plot(df2_snp['Time'],media_snp[5],c=colors[5],label=labels[5],lw=0.5)
# axs.plot(df2_snp['Time'],media_snp[2],c=colors[2],label=labels[2],lw=0.5)
# axs.plot(df2_snp['Time'],media_snp[7],c=colors[7],label=labels[7],lw=0.5)
# axs.plot(df2_snp['Time'],media_snp[8],c=colors[8],label=labels[8],lw=0.5)
# axs.plot(df2_snp['Time'],media_snp[1],c=colors[1],label=labels[1],lw=0.5)
# axs.plot(df2_snp['Time'],media_snp2,c='darkgoldenrod',label='Roots 100 µM 2 day',lw=0.5)
# axs.plot(df2_snp['Time'],media_snp[6],c=colors[6],label=labels[6],lw=0.5)
# axs.plot(df2_snp['Time'],media_snp[3],c=colors[3],label=labels[3],lw=0.5)
# axs.plot(df2_snp['Time'],media_snp[9],c=colors[9],label=labels[9],lw=0.5)
# axs.plot(df2_snp['Time'],media_snp[10],c=colors[10],label=labels[10],lw=0.5)

axs.set_xlim(3.5,30)
# axs.set_ylabel(r'Absorbance (280 nm)')
# axs.set_xlabel(r'Retention time')
# axs.legend(fontsize=label_size, loc = "upper left",  
#            bbox_to_anchor = (0.25, 0.99),ncol=2, 
#            fancybox=False,frameon=False)
# axs.yaxis.get_major_formatter()._usetex = False
# axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('snp2_diff.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
plt.close(fig)


# # DANO MECANICO

# In[45]:


df_dm = pd.read_csv(r'E:\Doc\Cap 2 - Tratadas_HPLC_Evelu\Analise_HPLC\RESULTADOS_PROCESSADOS\Figures_cromatograma\dm.csv',sep=',', decimal=',')#,index_col=None


# In[49]:


for i in range(len(df_dm.columns)):
    print(i,df_dm.columns[i])


# In[50]:


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


# In[53]:



peaks = find_peaks(media_dm[4], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df_dm['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_dm['Time'],media_dm[4],label='dm_leaves2d_1-4',lw=0.5)
axs.scatter(tempo,picos,label='dm_leaves2d_1-4',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_dm['Time'][peaks[0][i]] < 35.0:
        plt.text(df_dm['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_dm['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('dm_leaves2d_1-4.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################

peaks = find_peaks(media_dm[5], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_dm['Time'],media_dm[5],label='dm_leaves2d_3-4',lw=0.5)
axs.scatter(tempo,picos,label='dm_leaves2d_3-4',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_dm['Time'][peaks[0][i]] < 35.0:
        plt.text(df_dm['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_dm['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('dm_leaves2d_3-4.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################


peaks = find_peaks(media_dm[6], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_dm['Time'],media_dm[6],label='dm_roots2d_1-4',lw=0.5)
axs.scatter(tempo,picos,label='dm_roots2d_1-4',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_dm['Time'][peaks[0][i]] < 35.0:
        plt.text(df_dm['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_dm['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('dm_roots2d_1-4.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################

peaks = find_peaks(media_dm[7], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_dm['Time'],media_dm[7],label='dm_roots2d_3-4',lw=0.5)
axs.scatter(tempo,picos,label='dm_roots2d_3-4',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_dm['Time'][peaks[0][i]] < 35.0:
        plt.text(df_dm['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_dm['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('dm_roots2d_3-4.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################
#####################

peaks = find_peaks(media_dm[8], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_dm['Time'],media_dm[8],label='dm_leaves4d_1-4',lw=0.5)
axs.scatter(tempo,picos,label='dm_leaves4d_1-4',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_dm['Time'][peaks[0][i]] < 35.0:
        plt.text(df_dm['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_dm['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('dm_leaves4d_1-4.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################

peaks = find_peaks(media_dm[9], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_dm['Time'],media_dm[9],label='dm_leaves4d_3-4',lw=0.5)
axs.scatter(tempo,picos,label='dm_leaves4d_3-4',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_dm['Time'][peaks[0][i]] < 35.0:
        plt.text(df_dm['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_dm['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('dm_leaves4d_3-4.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################


peaks = find_peaks(media_dm[10], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_dm['Time'],media_dm[10],label='dm_roots4d_1-4',lw=0.5)
axs.scatter(tempo,picos,label='dm_roots4d_1-4',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_dm['Time'][peaks[0][i]] < 35.0:
        plt.text(df_dm['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_dm['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('dm_roots4d_1-4.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################

peaks = find_peaks(media_dm[11], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_dm['Time'],media_dm[11],label='dm_roots4d_3-4',lw=0.5)
axs.scatter(tempo,picos,label='dm_roots4d_3-4',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_dm['Time'][peaks[0][i]] < 35.0:
        plt.text(df_dm['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_dm['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('dm_roots4d_3-4.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 


# In[ ]:





# In[20]:


label_size=6
plots_em_x=1
plots_em_y=1

colors=['#009792fd','tan','lime','lightcoral',
         'aqua','teal','orange','darkgoldenrod',
         'mediumseagreen','darkgreen','chocolate','sienna']

# labels=['CT leaves 2d','CT roots 2d','CT leaves 4d','CT roots 4d',
#         'Leaves 100 µM 2d','Leaves 200 µM 2d','Roots 200 µM 2d',
#         'Leaves 100 µM 4d','Leaves 200 µM 4d','Roots 100 µM 4d','Roots 200 µM 4d']

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))


# for i in range (7):
#     axs.plot(df2_uv['Time'],media_dm[i],c=colors[i],label=labels[i],lw=0.5)


axs.plot(df_dm['Time'],media_dm[0],c=colors[0],label='CT leaves 2d',lw=0.5)
axs.plot(df_dm['Time'],media_dm[4],c=colors[1],label='Leaves 2d 25\%',lw=0.5)
axs.plot(df_dm['Time'],media_dm[5],c=colors[2],label='Leaves 2d 75\%',lw=0.5)
axs.plot(df_dm['Time'],media_dm[2],c=colors[3],label='CT leaves 4d',lw=0.5)
axs.plot(df_dm['Time'],media_dm[8],c=colors[4],label='Leaves 4d 25\%',lw=0.5)
axs.plot(df_dm['Time'],media_dm[9],c=colors[5],label='Leaves 4d 75\%',lw=0.5)
axs.plot(df_dm['Time'],media_dm[1],c=colors[6],label='CT roots 2d',lw=0.5)
axs.plot(df_dm['Time'],media_dm[6],c=colors[7],label='Roots 2d 25\%',lw=0.5)
axs.plot(df_dm['Time'],media_dm[7],c=colors[8],label='Roots 2d 75\%',lw=0.5)
axs.plot(df_dm['Time'],media_dm[3],c=colors[9],label='CT roots 4d',lw=0.5)
axs.plot(df_dm['Time'],media_dm[10],c=colors[10],label='Roots 4d 25\%',lw=0.5)
axs.plot(df_dm['Time'],media_dm[11],c=colors[11],label='Roots 4d 75\%',lw=0.5)

#axs.set_xlim(3.5,25)
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
axs.legend(fontsize=label_size, loc = "upper right",  
           #bbox_to_anchor = (0.25, 0.99),ncol=2, 
           fancybox=False,frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('dm.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
# plt.close(fig)

# fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))

# for i in range (7):
#     axs.plot(df2_uv['Time'],media_dm[i],c=colors[i],label=labels[i],lw=0.5)

# axs.plot(df_dm['Time'],media_dm[0],c=colors[0],label=labels[0],lw=0.5)
# axs.plot(df_dm['Time'],media_dm[4],c=colors[4],label=labels[4],lw=0.5)
# axs.plot(df_dm['Time'],media_dm[5],c=colors[5],label=labels[5],lw=0.5)
# axs.plot(df_dm['Time'],media_dm[2],c=colors[2],label=labels[2],lw=0.5)
# axs.plot(df_dm['Time'],media_dm[7],c=colors[7],label=labels[7],lw=0.5)
# axs.plot(df_dm['Time'],media_dm[8],c=colors[8],label=labels[8],lw=0.5)
# axs.plot(df_dm['Time'],media_dm[1],c=colors[1],label=labels[1],lw=0.5)
# axs.plot(df_dm['Time'],media_dm2,c='darkgoldenrod',label='Roots 100 µM 2 day',lw=0.5)
# axs.plot(df_dm['Time'],media_dm[6],c=colors[6],label=labels[6],lw=0.5)
# axs.plot(df_dm['Time'],media_dm[3],c=colors[3],label=labels[3],lw=0.5)
# axs.plot(df_dm['Time'],media_dm[9],c=colors[9],label=labels[9],lw=0.5)
# axs.plot(df_dm['Time'],media_dm[10],c=colors[10],label=labels[10],lw=0.5)

axs.set_xlim(3.5,30)
# axs.set_ylabel(r'Absorbance (280 nm)')
# axs.set_xlabel(r'Retention time')
# axs.legend(fontsize=label_size, loc = "upper left",  
#            bbox_to_anchor = (0.25, 0.99),ncol=2, 
#            fancybox=False,frameon=False)
# axs.yaxis.get_major_formatter()._usetex = False
# axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('dm2.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
plt.close(fig)

label_size=5
# colors1=['aquamarine','palegreen','C2','darkgreen','antiquewhite','tan','chocolate','C5']


fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))


# for i in range (7):
#     axs.plot(df2_uv['Time'],media_dm[i],c=colors[i],label=labels[i],lw=0.5)

# axs.plot(df_dm['Time'],media_dm[0],c=colors[0],label='CT leaves 2d',lw=0.5)
axs.plot(df_dm['Time'],media_dm[4]-media_dm[0],c='aquamarine',label='Leaves 2d 25\%',lw=0.5)
axs.plot(df_dm['Time'],media_dm[5]-media_dm[0],c='palegreen',label='Leaves 2d 75\%',lw=0.5)
# axs.plot(df_dm['Time'],media_dm[2],c=colors[3],label='CT leaves 4d',lw=0.5)
axs.plot(df_dm['Time'],media_dm[8]-media_dm[2],c='C2',label='Leaves 4d 25\%',lw=0.5)
axs.plot(df_dm['Time'],media_dm[9]-media_dm[2],c='darkgreen',label='Leaves 4d 75\%',lw=0.5)
# axs.plot(df_dm['Time'],media_dm[1],c=colors[6],label='CT roots 2d',lw=0.5)
axs.plot(df_dm['Time'],media_dm[6]-media_dm[1],c='antiquewhite',label='Roots 2d 25\%',lw=0.5)
axs.plot(df_dm['Time'],media_dm[7]-media_dm[1],c='tan',label='Roots 2d 75\%',lw=0.5)
# axs.plot(df_dm['Time'],media_dm[3],c=colors[9],label='CT roots 4d',lw=0.5)
axs.plot(df_dm['Time'],media_dm[10]-media_dm[3],c='chocolate',label='Roots 4d 25\%',lw=0.5)
axs.plot(df_dm['Time'],media_dm[11]-media_dm[3],c='C5',label='Roots 4d 75\%',lw=0.5)

#axs.set_xlim(3.5,25)
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.legend(fontsize=label_size, loc = "upper right",  
           ncol=1, #bbox_to_anchor = (0.25, 0.99),
           fancybox=False,frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('dm_diff.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
# plt.close(fig)


# fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))


# for i in range (7):
#     axs.plot(df2_uv['Time'],media_dm[i],c=colors[i],label=labels[i],lw=0.5)

# axs.plot(df_dm['Time'],media_dm[0],c=colors[0],label=labels[0],lw=0.5)
# axs.plot(df_dm['Time'],media_dm[4],c=colors[4],label=labels[4],lw=0.5)
# axs.plot(df_dm['Time'],media_dm[5],c=colors[5],label=labels[5],lw=0.5)
# axs.plot(df_dm['Time'],media_dm[2],c=colors[2],label=labels[2],lw=0.5)
# axs.plot(df_dm['Time'],media_dm[7],c=colors[7],label=labels[7],lw=0.5)
# axs.plot(df_dm['Time'],media_dm[8],c=colors[8],label=labels[8],lw=0.5)
# axs.plot(df_dm['Time'],media_dm[1],c=colors[1],label=labels[1],lw=0.5)
# axs.plot(df_dm['Time'],media_dm2,c='darkgoldenrod',label='Roots 100 µM 2 day',lw=0.5)
# axs.plot(df_dm['Time'],media_dm[6],c=colors[6],label=labels[6],lw=0.5)
# axs.plot(df_dm['Time'],media_dm[3],c=colors[3],label=labels[3],lw=0.5)
# axs.plot(df_dm['Time'],media_dm[9],c=colors[9],label=labels[9],lw=0.5)
# axs.plot(df_dm['Time'],media_dm[10],c=colors[10],label=labels[10],lw=0.5)
label_size=5
axs.set_xlim(3.5,30)
# axs.set_ylabel(r'Absorbance (280 nm)')
# axs.set_xlabel(r'Retention time')
axs.legend(fontsize=label_size, loc = "lower right",  ncol=1,
#            bbox_to_anchor = (0.25, 0.99), 
            fancybox=False,frameon=False)
# axs.yaxis.get_major_formatter()._usetex = False
# axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('dm2_diff.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
plt.close(fig)


# # Nacl

# In[2]:


df_nacl = pd.read_csv(r'E:\Doc\Cap 2 - Tratadas_HPLC_Evelu\Analise_HPLC\RESULTADOS_PROCESSADOS\Figures_cromatograma\salino.csv',sep=',', decimal=',')#,index_col=None


# In[3]:


for i in range(len(df_nacl.columns)):
    print(i,df_nacl.columns[i])


# In[4]:


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
    
    


# In[58]:



peaks = find_peaks(media_nacl[4], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df_dm['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_dm['Time'],media_nacl[4],label='nacl_leaves2d_50M',lw=0.5)
axs.scatter(tempo,picos,label='nacl_leaves2d_50M',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_dm['Time'][peaks[0][i]] < 35.0:
        plt.text(df_dm['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_dm['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('nacl_leaves2d_50M.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

####

peaks = find_peaks(media_nacl[5], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df_dm['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_dm['Time'],media_nacl[5],label='nacl_roots2d_50M',lw=0.5)
axs.scatter(tempo,picos,label='nacl_roots2d_50M',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_dm['Time'][peaks[0][i]] < 35.0:
        plt.text(df_dm['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_dm['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('nacl_roots2d_50M.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

####

peaks = find_peaks(media_nacl2, height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df_dm['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_dm['Time'],media_nacl2,label='nacl_leaves2d_50M',lw=0.5)
axs.scatter(tempo,picos,label='nacl_leaves2d_25M',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_dm['Time'][peaks[0][i]] < 35.0:
        plt.text(df_dm['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_dm['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('nacl_leaves2d_25M.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

####

peaks = find_peaks(media_nacl3, height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df_dm['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_dm['Time'],media_nacl3,label='nacl_roots2d_25M',lw=0.5)
axs.scatter(tempo,picos,label='nacl_roots2d_25M',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_dm['Time'][peaks[0][i]] < 35.0:
        plt.text(df_dm['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_dm['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('nacl_roots2d_25M.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

##################################


eaks = find_peaks(media_nacl[6], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df_dm['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_dm['Time'],media_nacl[6],label='nacl_leaves4d_25M',lw=0.5)
axs.scatter(tempo,picos,label='nacl_leaves4d_25M',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_dm['Time'][peaks[0][i]] < 35.0:
        plt.text(df_dm['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_dm['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('nacl_leaves4d_25M.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

####

peaks = find_peaks(media_nacl[7], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df_dm['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_dm['Time'],media_nacl[7],label='nacl_leaves4d_50M',lw=0.5)
axs.scatter(tempo,picos,label='nacl_leaves4d_50M',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_dm['Time'][peaks[0][i]] < 35.0:
        plt.text(df_dm['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_dm['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('nacl_leaves4d_50M.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

####


peaks = find_peaks(media_nacl[8], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df_dm['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_dm['Time'],media_nacl[8],label='nacl_roots4d_25M',lw=0.5)
axs.scatter(tempo,picos,label='nacl_roots4d_25M',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_dm['Time'][peaks[0][i]] < 35.0:
        plt.text(df_dm['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_dm['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('nacl_roots4d_25M.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

####

peaks = find_peaks(media_nacl[9], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df_dm['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_dm['Time'],media_nacl[9],label='nacl_roots4d_50M',lw=0.5)
axs.scatter(tempo,picos,label='nacl_roots4d_50M',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_dm['Time'][peaks[0][i]] < 35.0:
        plt.text(df_dm['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_dm['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('nacl_roots4d_50M.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 


# In[9]:


label_size=6
plots_em_x=1
plots_em_y=1

colors=['#009792fd','tan','lime','lightcoral',
         'aqua','teal','orange',
         'mediumseagreen','darkgreen','chocolate']

# labels=['CT leaves 2d','CT roots 2d','CT leaves 4d','CT roots 4d',
#         'Leaves 100 µM 2d','Leaves 200 µM 2d','Roots 200 µM 2d',
#         'Leaves 100 µM 4d','Leaves 200 µM 4d','Roots 100 µM 4d','Roots 200 µM 4d']

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))


# for i in range (7):
#     axs.plot(df2_uv['Time'],media_nacl[i],c=colors[i],label=labels[i],lw=0.5)

axs.plot(df2_nacl['Time'],media_nacl[0],c=colors[0],label='CT leaves 2d',lw=0.5)
axs.plot(df2_nacl['Time'],media_nacl2,c='darkgoldenrod',label='Leaves 2d 0,25M',lw=0.5)
axs.plot(df2_nacl['Time'],media_nacl[4],c=colors[4],label='Leaves 2d 0,50M',lw=0.5)
axs.plot(df2_nacl['Time'],media_nacl[2],c=colors[5],label='CT leaves 4d',lw=0.5)
axs.plot(df2_nacl['Time'],media_nacl[6],c=colors[2],label='Leaves 4d 0,25M',lw=0.5)
axs.plot(df2_nacl['Time'],media_nacl[7],c=colors[7],label='Leaves 4d 0,50M',lw=0.5)

axs.plot(df2_nacl['Time'],media_nacl[1],c=colors[0],label='CT roots 2d',lw=0.5)
axs.plot(df2_nacl['Time'],media_nacl3,c='sienna',label='Roots 2d 0,25M',lw=0.5)
axs.plot(df2_nacl['Time'],media_nacl[5],c=colors[4],label='Roots 2d 0,50M',lw=0.5)
axs.plot(df2_nacl['Time'],media_nacl[3],c=colors[5],label='CT roots 4d',lw=0.5)
axs.plot(df2_nacl['Time'],media_nacl[8],c=colors[2],label='Roots 4d 0,25M',lw=0.5)
axs.plot(df2_nacl['Time'],media_nacl[9],c=colors[7],label='Roots 4d 0,50M',lw=0.5)

#axs.set_xlim(3.5,25)
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
axs.legend(fontsize=label_size, loc = "upper right",  
           #bbox_to_anchor = (0.25, 0.99),ncol=2, 
           fancybox=False,frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('nacl.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
# plt.close(fig)

# fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))

# for i in range (7):
#     axs.plot(df2_uv['Time'],media_nacl[i],c=colors[i],label=labels[i],lw=0.5)

# axs.plot(df2_nacl['Time'],media_nacl[0],c=colors[0],label=labels[0],lw=0.5)
# axs.plot(df2_nacl['Time'],media_nacl[4],c=colors[4],label=labels[4],lw=0.5)
# axs.plot(df2_nacl['Time'],media_nacl[5],c=colors[5],label=labels[5],lw=0.5)
# axs.plot(df2_nacl['Time'],media_nacl[2],c=colors[2],label=labels[2],lw=0.5)
# axs.plot(df2_nacl['Time'],media_nacl[7],c=colors[7],label=labels[7],lw=0.5)
# axs.plot(df2_nacl['Time'],media_nacl[8],c=colors[8],label=labels[8],lw=0.5)
# axs.plot(df2_nacl['Time'],media_nacl[1],c=colors[1],label=labels[1],lw=0.5)
# axs.plot(df2_nacl['Time'],media_nacl2,c='darkgoldenrod',label='Roots 100 µM 2 day',lw=0.5)
# axs.plot(df2_nacl['Time'],media_nacl[6],c=colors[6],label=labels[6],lw=0.5)
# axs.plot(df2_nacl['Time'],media_nacl[3],c=colors[3],label=labels[3],lw=0.5)
# axs.plot(df2_nacl['Time'],media_nacl[9],c=colors[9],label=labels[9],lw=0.5)
# axs.plot(df2_nacl['Time'],media_nacl[10],c=colors[10],label=labels[10],lw=0.5)

axs.set_xlim(3.5,35)
# axs.set_ylabel(r'Absorbance (280 nm)')
# axs.set_xlabel(r'Retention time')
# axs.legend(fontsize=label_size, loc = "upper left",  
#            bbox_to_anchor = (0.25, 0.99),ncol=2, 
#            fancybox=False,frameon=False)
# axs.yaxis.get_major_formatter()._usetex = False
# axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('nacl2.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
plt.close(fig)


# colors1=['aquamarine','palegreen','C2','darkgreen','antiquewhite','tan','chocolate','C5']

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))


# for i in range (7):
#     axs.plot(df2_uv['Time'],media_nacl[i],c=colors[i],label=labels[i],lw=0.5)

# axs.plot(df2_nacl['Time'],media_nacl[0],c=colors[0],label='CT leaves 2d',lw=0.5)
axs.plot(df2_nacl['Time'],media_nacl2-media_nacl[0],c='aquamarine',label='Leaves 2d 0,25M',lw=0.5)
axs.plot(df2_nacl['Time'],media_nacl[4]-media_nacl[0],c='palegreen',label='Leaves 2d 0,50M',lw=0.5)
# axs.plot(df2_nacl['Time'],media_nacl[2],c=colors[5],label='CT leaves 4d',lw=0.5)
axs.plot(df2_nacl['Time'],media_nacl[6]-media_nacl[2],c='C2',label='Leaves 4d 0,25M',lw=0.5)
axs.plot(df2_nacl['Time'],media_nacl[7]-media_nacl[2],c='darkgreen',label='Leaves 4d 0,50M',lw=0.5)

# axs.plot(df2_nacl['Time'],media_nacl[1],c=colors[0],label='CT roots 2d',lw=0.5)
axs.plot(df2_nacl['Time'],media_nacl3-media_nacl[1],c='antiquewhite',label='Roots 2d 0,25M',lw=0.5)
axs.plot(df2_nacl['Time'],media_nacl[5]-media_nacl[1],c='tan',label='Roots 2d 0,50M',lw=0.5)
# axs.plot(df2_nacl['Time'],media_nacl[3],c=colors[5],label='CT roots 4d',lw=0.5)
axs.plot(df2_nacl['Time'],media_nacl[8]-media_nacl[3],c='chocolate',label='Roots 4d 0,25M',lw=0.5)
axs.plot(df2_nacl['Time'],media_nacl[9]-media_nacl[3],c='C5',label='Roots 4d 0,50M',lw=0.5)

#axs.set_xlim(3.5,25)
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
label_size=5.3
axs.legend(fontsize=label_size, loc = "lower right",  
           #bbox_to_anchor = (0.25, 0.99),ncol=2, 
           fancybox=False,frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('nacl_diff.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
# plt.close(fig)


# fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))


# for i in range (7):
#     axs.plot(df2_uv['Time'],media_nacl[i],c=colors[i],label=labels[i],lw=0.5)

# axs.plot(df2_nacl['Time'],media_nacl[0],c=colors[0],label=labels[0],lw=0.5)
# axs.plot(df2_nacl['Time'],media_nacl[4],c=colors[4],label=labels[4],lw=0.5)
# axs.plot(df2_nacl['Time'],media_nacl[5],c=colors[5],label=labels[5],lw=0.5)
# axs.plot(df2_nacl['Time'],media_nacl[2],c=colors[2],label=labels[2],lw=0.5)
# axs.plot(df2_nacl['Time'],media_nacl[7],c=colors[7],label=labels[7],lw=0.5)
# axs.plot(df2_nacl['Time'],media_nacl[8],c=colors[8],label=labels[8],lw=0.5)
# axs.plot(df2_nacl['Time'],media_nacl[1],c=colors[1],label=labels[1],lw=0.5)
# axs.plot(df2_nacl['Time'],media_nacl2,c='darkgoldenrod',label='Roots 100 µM 2 day',lw=0.5)
# axs.plot(df2_nacl['Time'],media_nacl[6],c=colors[6],label=labels[6],lw=0.5)
# axs.plot(df2_nacl['Time'],media_nacl[3],c=colors[3],label=labels[3],lw=0.5)
# axs.plot(df2_nacl['Time'],media_nacl[9],c=colors[9],label=labels[9],lw=0.5)
# axs.plot(df2_nacl['Time'],media_nacl[10],c=colors[10],label=labels[10],lw=0.5)
label_size=5.3
axs.set_xlim(3.5,35)
# axs.set_ylabel(r'Absorbance (280 nm)')
# axs.set_xlabel(r'Retention time')
axs.legend(fontsize=label_size, loc = "lower right",  
#            bbox_to_anchor = (0.25, 0.99),ncol=2, 
             fancybox=False,frameon=False)
# axs.yaxis.get_major_formatter()._usetex = False
# axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('nacl2_diff.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
plt.close(fig)


# # ABA

# In[59]:


df_aba = pd.read_csv(r'E:\Doc\Cap 2 - Tratadas_HPLC_Evelu\Analise_HPLC\RESULTADOS_PROCESSADOS\Figures_cromatograma\aba.csv',sep=',', decimal=',')#,index_col=None


# In[60]:


for i in range(len(df_aba.columns)):
    print(i,df_aba.columns[i])


# In[62]:


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


# In[63]:



peaks = find_peaks(media_aba[4], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df_aba['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_aba['Time'],media_aba[4],label='aba_leaves2d_25mg-ml',lw=0.5)
axs.scatter(tempo,picos,label='aba_leaves2d_25mg-ml',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_aba['Time'][peaks[0][i]] < 35.0:
        plt.text(df_aba['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_aba['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('aba_leaves2d_25mg-ml.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################

peaks = find_peaks(media_aba[5], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_aba['Time'],media_aba[5],label='aba_leaves2d_50mg-ml',lw=0.5)
axs.scatter(tempo,picos,label='aba_leaves2d_50mg-ml',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_aba['Time'][peaks[0][i]] < 35.0:
        plt.text(df_aba['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_aba['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('aba_leaves2d_50mg-ml.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################


peaks = find_peaks(media_aba[6], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_aba['Time'],media_aba[6],label='aba_roots2d_25mg-ml',lw=0.5)
axs.scatter(tempo,picos,label='aba_roots2d_25mg-ml',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_aba['Time'][peaks[0][i]] < 35.0:
        plt.text(df_aba['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_aba['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('aba_roots2d_25mg-ml.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################

peaks = find_peaks(media_aba[7], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_aba['Time'],media_aba[7],label='aba_roots2d_50mg-ml',lw=0.5)
axs.scatter(tempo,picos,label='aba_roots2d_50mg-ml',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_aba['Time'][peaks[0][i]] < 35.0:
        plt.text(df_aba['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_aba['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('aba_roots2d_50mg-ml.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################
#####################

peaks = find_peaks(media_aba[8], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_aba['Time'],media_aba[8],label='aba_leaves4d_25mg-ml',lw=0.5)
axs.scatter(tempo,picos,label='aba_leaves4d_25mg-ml',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_aba['Time'][peaks[0][i]] < 35.0:
        plt.text(df_aba['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_aba['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('aba_leaves4d_25mg-ml.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################

peaks = find_peaks(media_aba[9], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_aba['Time'],media_aba[9],label='aba_leaves4d_50mg-ml',lw=0.5)
axs.scatter(tempo,picos,label='aba_leaves4d_50mg-ml',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_aba['Time'][peaks[0][i]] < 35.0:
        plt.text(df_aba['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_aba['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('aba_leaves4d_50mg-ml.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################


peaks = find_peaks(media_aba[10], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_aba['Time'],media_aba[10],label='aba_roots4d_25mg-ml',lw=0.5)
axs.scatter(tempo,picos,label='aba_roots4d_25mg-ml',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_aba['Time'][peaks[0][i]] < 35.0:
        plt.text(df_aba['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_aba['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('aba_roots4d_25mg-ml.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################

peaks = find_peaks(media_aba[11], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df2_uv['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_aba['Time'],media_aba[11],label='aba_roots4d_50mg-ml',lw=0.5)
axs.scatter(tempo,picos,label='aba_roots4d_50mg-ml',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_aba['Time'][peaks[0][i]] < 35.0:
        plt.text(df_aba['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_aba['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('aba_roots4d_50mg-ml.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 


# In[ ]:





# In[28]:


label_size=6
plots_em_x=1
plots_em_y=1


# 0 FC2425
# 1 RC2425
# 2 FC2445
# 3 RC2445
# 4 FABA2525
# 5 FABA5025
# 6 RABA2525
# 7 RABA5025
# 8 FABA2545
# 9 FABA5045
# 10 RABA2545
# 11 RABA5045

colors=['#009792fd','tan','lime','lightcoral',
         'aqua','teal','orange','darkgoldenrod',
         'mediumseagreen','darkgreen','chocolate','sienna']

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))


# for i in range (7):
#     axs.plot(df2_uv['Time'],media_aba[i],c=colors[i],label=labels[i],lw=0.5)


axs.plot(df_aba['Time'],media_aba[0],c=colors[0],label=r'CT leaves 2d',lw=0.5)
axs.plot(df_aba['Time'],media_aba[4],c=colors[1],label=r'Leaves 2d 25 mg/mL',lw=0.5)
axs.plot(df_aba['Time'],media_aba[5],c=colors[2],label=r'Leaves 2d 50 mg/mL',lw=0.5)
axs.plot(df_aba['Time'],media_aba[2],c=colors[3],label=r'CT leaves 4d',lw=0.5)
axs.plot(df_aba['Time'],media_aba[8],c=colors[4],label=r'Leaves 4d 25 mg/mL',lw=0.5)
axs.plot(df_aba['Time'],media_aba[9],c=colors[5],label=r'Leaves 4d 50 mg/mL',lw=0.5)
axs.plot(df_aba['Time'],media_aba[1],c=colors[6],label=r'CT roots 2d',lw=0.5)
axs.plot(df_aba['Time'],media_aba[6],c=colors[7],label=r'Roots 2d 25 mg/mL',lw=0.5)
axs.plot(df_aba['Time'],media_aba[7],c=colors[8],label=r'Roots 2d 50 mg/mL',lw=0.5)
axs.plot(df_aba['Time'],media_aba[3],c=colors[9],label=r'CT roots 4d',lw=0.5)
axs.plot(df_aba['Time'],media_aba[10],c=colors[10],label=r'Roots 4d 25 mg/mL',lw=0.5)
axs.plot(df_aba['Time'],media_aba[11],c=colors[11],label=r'Roots 4d 50 mg/mL',lw=0.5)

#axs.set_xlim(3.5,25)
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
axs.legend(fontsize=label_size, loc = "upper right",  
           #bbox_to_anchor = (0.25, 0.99),ncol=2, 
           fancybox=False,frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('aba.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
# plt.close(fig)

# fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))

# for i in range (7):
#     axs.plot(df2_uv['Time'],media_aba[i],c=colors[i],label=labels[i],lw=0.5)

# axs.plot(df_aba['Time'],media_aba[0],c=colors[0],label=labels[0],lw=0.5)
# axs.plot(df_aba['Time'],media_aba[4],c=colors[4],label=labels[4],lw=0.5)
# axs.plot(df_aba['Time'],media_aba[5],c=colors[5],label=labels[5],lw=0.5)
# axs.plot(df_aba['Time'],media_aba[2],c=colors[2],label=labels[2],lw=0.5)
# axs.plot(df_aba['Time'],media_aba[7],c=colors[7],label=labels[7],lw=0.5)
# axs.plot(df_aba['Time'],media_aba[8],c=colors[8],label=labels[8],lw=0.5)
# axs.plot(df_aba['Time'],media_aba[1],c=colors[1],label=labels[1],lw=0.5)
# axs.plot(df_aba['Time'],media_aba2,c='darkgoldenrod',label='Roots 100 µM 2 day',lw=0.5)
# axs.plot(df_aba['Time'],media_aba[6],c=colors[6],label=labels[6],lw=0.5)
# axs.plot(df_aba['Time'],media_aba[3],c=colors[3],label=labels[3],lw=0.5)
# axs.plot(df_aba['Time'],media_aba[9],c=colors[9],label=labels[9],lw=0.5)
# axs.plot(df_aba['Time'],media_aba[10],c=colors[10],label=labels[10],lw=0.5)
label_size=5
axs.set_xlim(3.5,35)
# axs.set_ylabel(r'Absorbance (280 nm)')
# axs.set_xlabel(r'Retention time')
# axs.legend(fontsize=label_size, loc = "upper left",  
#            bbox_to_anchor = (0.25, 0.99),ncol=2, 
#            fancybox=False,frameon=False)
# axs.yaxis.get_major_formatter()._usetex = False
# axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('aba2.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
plt.close(fig)

label_size=6
# colors1=['aquamarine','palegreen','C2','darkgreen','antiquewhite','tan','chocolate','C5']


fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))


# for i in range (7):
#     axs.plot(df2_uv['Time'],media_aba[i],c=colors[i],label=labels[i],lw=0.5)

# axs.plot(df_aba['Time'],media_aba[0],c=colors[0],label=r'CT leaves 2d',lw=0.5)
axs.plot(df_aba['Time'],media_aba[4]-media_aba[0],c='aquamarine',label=r'Leaves 2d 25 mg/mL',lw=0.5)
axs.plot(df_aba['Time'],media_aba[5]-media_aba[0],c='palegreen',label=r'Leaves 2d 50 mg/mL',lw=0.5)
# axs.plot(df_aba['Time'],media_aba[2],c=colors[3],label=r'CT leaves 4d',lw=0.5)
axs.plot(df_aba['Time'],media_aba[8]-media_aba[2],c='C2',label=r'Leaves 4d 25 mg/mL',lw=0.5)
axs.plot(df_aba['Time'],media_aba[9]-media_aba[2],c='darkgreen',label=r'Leaves 4d 50 mg/mL',lw=0.5)
# axs.plot(df_aba['Time'],media_aba[1],c=colors[6],label=r'CT roots 2d',lw=0.5)
axs.plot(df_aba['Time'],media_aba[6]-media_aba[1],c='antiquewhite',label=r'Roots 2d 25 mg/mL',lw=0.5)
axs.plot(df_aba['Time'],media_aba[7]-media_aba[1],c='tan',label=r'Roots 2d 50 mg/mL',lw=0.5)
# axs.plot(df_aba['Time'],media_aba[3],c=colors[9],label=r'CT roots 4d',lw=0.5)
axs.plot(df_aba['Time'],media_aba[10]-media_aba[3],c='chocolate',label=r'Roots 4d 25 mg/mL',lw=0.5)
axs.plot(df_aba['Time'],media_aba[11]-media_aba[3],c='C5',label=r'Roots 4d 50 mg/mL',lw=0.5)

#axs.set_xlim(3.5,25)
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.legend(fontsize=label_size, loc = "lower right",  
           ncol=1, #bbox_to_anchor = (0.25, 0.99),
           fancybox=False,frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('aba_diff.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
# plt.close(fig)


# fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))


# for i in range (7):
#     axs.plot(df2_uv['Time'],media_aba[i],c=colors[i],label=labels[i],lw=0.5)

# axs.plot(df_aba['Time'],media_aba[0],c=colors[0],label=labels[0],lw=0.5)
# axs.plot(df_aba['Time'],media_aba[4],c=colors[4],label=labels[4],lw=0.5)
# axs.plot(df_aba['Time'],media_aba[5],c=colors[5],label=labels[5],lw=0.5)
# axs.plot(df_aba['Time'],media_aba[2],c=colors[2],label=labels[2],lw=0.5)
# axs.plot(df_aba['Time'],media_aba[7],c=colors[7],label=labels[7],lw=0.5)
# axs.plot(df_aba['Time'],media_aba[8],c=colors[8],label=labels[8],lw=0.5)
# axs.plot(df_aba['Time'],media_aba[1],c=colors[1],label=labels[1],lw=0.5)
# axs.plot(df_aba['Time'],media_aba2,c='darkgoldenrod',label='Roots 100 µM 2 day',lw=0.5)
# axs.plot(df_aba['Time'],media_aba[6],c=colors[6],label=labels[6],lw=0.5)
# axs.plot(df_aba['Time'],media_aba[3],c=colors[3],label=labels[3],lw=0.5)
# axs.plot(df_aba['Time'],media_aba[9],c=colors[9],label=labels[9],lw=0.5)
# axs.plot(df_aba['Time'],media_aba[10],c=colors[10],label=labels[10],lw=0.5)
label_size=6
axs.set_xlim(3.5,35)
# axs.set_ylabel(r'Absorbance (280 nm)')
# axs.set_xlabel(r'Retention time')
axs.legend(fontsize=label_size, loc = "lower right",  ncol=1,
#            bbox_to_anchor = (0.25, 0.99), 
            fancybox=False,frameon=False)
# axs.yaxis.get_major_formatter()._usetex = False
# axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('aba2_diff.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
plt.close(fig)


# # HIDRICO

# In[64]:


df_h = pd.read_csv(r'E:\Doc\Cap 2 - Tratadas_HPLC_Evelu\Analise_HPLC\RESULTADOS_PROCESSADOS\Figures_cromatograma\hidrico.csv',sep=',', decimal=',')#,index_col=None


# In[65]:


for i in range(len(df_h.columns)):
    print(i,df_h.columns[i])


# In[66]:


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


# In[67]:



peaks = find_peaks(media_h[1], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df_h['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_h['Time'],media_h[1],label='h_leaves_t1',lw=0.5)
axs.scatter(tempo,picos,label='h_leaves_t1',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_h['Time'][peaks[0][i]] < 35.0:
        plt.text(df_h['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_h['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('h_leaves_t1.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################

peaks = find_peaks(media_h[2], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df_h['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_h['Time'],media_h[2],label='h_leaves_t2',lw=0.5)
axs.scatter(tempo,picos,label='h_leaves_t2',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_h['Time'][peaks[0][i]] < 35.0:
        plt.text(df_h['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_h['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('h_leaves_t2.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################

peaks = find_peaks(media_h[3], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df_h['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_h['Time'],media_h[3],label='h_leaves_t3',lw=0.5)
axs.scatter(tempo,picos,label='h_leaves_t3',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_h['Time'][peaks[0][i]] < 35.0:
        plt.text(df_h['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_h['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('h_leaves_t3.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################

peaks = find_peaks(media_h[5], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df_h['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_h['Time'],media_h[5],label='h_roots_t1',lw=0.5)
axs.scatter(tempo,picos,label='h_roots_t1',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_h['Time'][peaks[0][i]] < 35.0:
        plt.text(df_h['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_h['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('h_roots_t1.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################

peaks = find_peaks(media_h[6], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df_h['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_h['Time'],media_h[6],label='h_roots_t2',lw=0.5)
axs.scatter(tempo,picos,label='h_roots_t2',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_h['Time'][peaks[0][i]] < 35.0:
        plt.text(df_h['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_h['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('h_roots_t2.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################

peaks = find_peaks(media_h[7], height = 0.001, prominence=0.01, distance=20)
picos = peaks[1]['peak_heights']
tempo = df_h['Time'][peaks[0]]

label_size=8
plots_em_x=1
plots_em_y=1
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))
axs.plot(df_h['Time'],media_h[7],label='h_roots_t3',lw=0.5)
axs.scatter(tempo,picos,label='h_roots_t3',s=5,c='C1',marker='.',linewidths=0)

for i in range(len(tempo)):
    if df_h['Time'][peaks[0][i]] < 35.0:
        plt.text(df_h['Time'][peaks[0][i]]-1,picos[i]+0.001,'%s'%df_h['Time'][peaks[0][i]],fontsize=1)
    
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.set_xlim(3,35)
plt.xticks([5,10,15,20,25,30,35])
axs.legend(fontsize=label_size, frameon=False, bbox_to_anchor=(0.99, 0.99))
plt.savefig('h_roots_t3.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=700) 

#####################


# In[ ]:





# In[9]:


label_size=5.5
plots_em_x=1
plots_em_y=1


# 0 FC2425
# 1 RC2425
# 2 FC2445
# 3 RC2445
# 4 FABA2525
# 5 FABA5025
# 6 RABA2525
# 7 RABA5025
# 8 FABA2545
# 9 FABA5045
# 10 RABA2545
# 11 RABA5045

colors=['#009792fd','tan','lime','lightcoral',
         'aqua','teal','orange','darkgoldenrod',
         'mediumseagreen','darkgreen','chocolate','sienna', 'C4', 'C5']

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))


# for i in range (7):
#     axs.plot(df2_uv['Time'],media_h[i],c=colors[i],label=labels[i],lw=0.5)


# 8 FCTH1-5, 0 FTH0-5,1 FTH1-5 
# 9 FCTH2-5, 2 FTH2-5
# 10 FCTH3-5, 3 FTH3-5

# 11 RCTH1-5, 4 RTH0-5, 5 RTH1-5
# 12 RCTH2-5, 6 RTH2-5
# 13 RCTH3-5, 7 RTH3-4.1


axs.plot(df_h['Time'],media_h[8],c=colors[0],label=r'CT leaves T1',lw=0.5)
axs.plot(df_h['Time'],media_h[0],c=colors[1],label=r'Leaves T0',lw=0.5)
axs.plot(df_h['Time'],media_h[1],c=colors[2],label=r'Leaves T1',lw=0.5)
axs.plot(df_h['Time'],media_h[9],c=colors[3],label=r'CT leaves T2',lw=0.5)
axs.plot(df_h['Time'],media_h[2],c=colors[4],label=r'Leaves T2',lw=0.5)
axs.plot(df_h['Time'],media_h[10],c=colors[5],label=r'CT Leaves T3',lw=0.5)
axs.plot(df_h['Time'],media_h[3],c=colors[6],label=r'Leaves T3',lw=0.5)

axs.plot(df_h['Time'],media_h[11],c=colors[7],label=r'CT Roots T1',lw=0.5)
axs.plot(df_h['Time'],media_h[4],c=colors[8],label=r'Roots T0',lw=0.5)
axs.plot(df_h['Time'],media_h[5],c=colors[9],label=r'Roots T1',lw=0.5)
axs.plot(df_h['Time'],media_h[12],c=colors[10],label=r'CT Roots T2',lw=0.5)
axs.plot(df_h['Time'],media_h[6],c=colors[11],label=r'Roots T2',lw=0.5)
axs.plot(df_h['Time'],media_h[13],c=colors[10],label=r'CT Roots T3',lw=0.5)
axs.plot(df_h['Time'],media_h[7],c=colors[11],label=r'Roots T3',lw=0.5)

#axs.set_xlim(3.5,25)
axs.set_ylabel(r'Absorbance (280 nm)')
axs.set_xlabel(r'Retention time')
axs.legend(fontsize=label_size, loc = "upper right",  
           #bbox_to_anchor = (0.25, 0.99),ncol=2, 
           fancybox=False,frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('h.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
# plt.close(fig)

# fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))

# for i in range (7):
#     axs.plot(df2_uv['Time'],media_h[i],c=colors[i],label=labels[i],lw=0.5)

# axs.plot(df_h['Time'],media_h[0],c=colors[0],label=labels[0],lw=0.5)
# axs.plot(df_h['Time'],media_h[4],c=colors[4],label=labels[4],lw=0.5)
# axs.plot(df_h['Time'],media_h[5],c=colors[5],label=labels[5],lw=0.5)
# axs.plot(df_h['Time'],media_h[2],c=colors[2],label=labels[2],lw=0.5)
# axs.plot(df_h['Time'],media_h[7],c=colors[7],label=labels[7],lw=0.5)
# axs.plot(df_h['Time'],media_h[8],c=colors[8],label=labels[8],lw=0.5)
# axs.plot(df_h['Time'],media_h[1],c=colors[1],label=labels[1],lw=0.5)
# axs.plot(df_h['Time'],media_h2,c='darkgoldenrod',label='Roots 100 µM 2 day',lw=0.5)
# axs.plot(df_h['Time'],media_h[6],c=colors[6],label=labels[6],lw=0.5)
# axs.plot(df_h['Time'],media_h[3],c=colors[3],label=labels[3],lw=0.5)
# axs.plot(df_h['Time'],media_h[9],c=colors[9],label=labels[9],lw=0.5)
# axs.plot(df_h['Time'],media_h[10],c=colors[10],label=labels[10],lw=0.5)
label_size=5
axs.set_xlim(3.5,35)
# axs.set_ylabel(r'Absorbance (280 nm)')
# axs.set_xlabel(r'Retention time')
# axs.legend(fontsize=label_size, loc = "upper left",  
#            bbox_to_anchor = (0.25, 0.99),ncol=2, 
#            fancybox=False,frameon=False)
# axs.yaxis.get_major_formatter()._usetex = False
# axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('h2.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
plt.close(fig)

label_size=6
# colors1=['aquamarine','palegreen','C2','darkgreen','antiquewhite','tan','chocolate','C5']


fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))


# for i in range (7):
#     axs.plot(df2_uv['Time'],media_h[i],c=colors[i],label=labels[i],lw=0.5)

# axs.plot(df_h['Time'],media_h[8],c=colors[0],label=r'CT leaves T1',lw=0.5)
axs.plot(df_h['Time'],media_h[1]-media_h[8],c='aquamarine',label=r'Leaves T1',lw=0.5)
# axs.plot(df_h['Time'],media_h[9],c=colors[3],label=r'CT leaves T2',lw=0.5)
axs.plot(df_h['Time'],media_h[2]-media_h[9],c='palegreen',label=r'Leaves T2',lw=0.5)
# axs.plot(df_h['Time'],media_h[10],c=colors[5],label=r'CT Leaves T3',lw=0.5)
axs.plot(df_h['Time'],media_h[3]-media_h[10],c='C2',label=r'Leaves T3',lw=0.5)

# axs.plot(df_h['Time'],media_h[11],c=colors[7],label=r'CT Roots T1',lw=0.5)
axs.plot(df_h['Time'],media_h[5]-media_h[11],c='antiquewhite',label=r'Roots T1',lw=0.5)
# axs.plot(df_h['Time'],media_h[12],c=colors[10],label=r'CT Roots T2',lw=0.5)
axs.plot(df_h['Time'],media_h[6]-media_h[12],c='tan',label=r'Roots T2',lw=0.5)
# axs.plot(df_h['Time'],media_h[13],c=colors[10],label=r'CT Roots T3',lw=0.5)
axs.plot(df_h['Time'],media_h[7]-media_h[13],c='C5',label=r'Roots T3',lw=0.5)

#axs.set_xlim(3.5,25)
axs.set_ylabel(r'Absorbance difference')
axs.set_xlabel(r'Retention time')
axs.legend(fontsize=label_size, loc = "upper right",  
           ncol=1, #bbox_to_anchor = (0.25, 0.99),
           fancybox=False,frameon=False)
axs.yaxis.get_major_formatter()._usetex = False
axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('h_diff.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
# plt.close(fig)


# fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))


# for i in range (7):
#     axs.plot(df2_uv['Time'],media_h[i],c=colors[i],label=labels[i],lw=0.5)

# axs.plot(df_h['Time'],media_h[0],c=colors[0],label=labels[0],lw=0.5)
# axs.plot(df_h['Time'],media_h[4],c=colors[4],label=labels[4],lw=0.5)
# axs.plot(df_h['Time'],media_h[5],c=colors[5],label=labels[5],lw=0.5)
# axs.plot(df_h['Time'],media_h[2],c=colors[2],label=labels[2],lw=0.5)
# axs.plot(df_h['Time'],media_h[7],c=colors[7],label=labels[7],lw=0.5)
# axs.plot(df_h['Time'],media_h[8],c=colors[8],label=labels[8],lw=0.5)
# axs.plot(df_h['Time'],media_h[1],c=colors[1],label=labels[1],lw=0.5)
# axs.plot(df_h['Time'],media_h2,c='darkgoldenrod',label='Roots 100 µM 2 day',lw=0.5)
# axs.plot(df_h['Time'],media_h[6],c=colors[6],label=labels[6],lw=0.5)
# axs.plot(df_h['Time'],media_h[3],c=colors[3],label=labels[3],lw=0.5)
# axs.plot(df_h['Time'],media_h[9],c=colors[9],label=labels[9],lw=0.5)
# axs.plot(df_h['Time'],media_h[10],c=colors[10],label=labels[10],lw=0.5)
label_size=6
axs.set_xlim(3.5,35)
# axs.set_ylabel(r'Absorbance (280 nm)')
# axs.set_xlabel(r'Retention time')
axs.legend(fontsize=label_size, loc = "upper right",  ncol=1,
#            bbox_to_anchor = (0.25, 0.99), 
            fancybox=False,frameon=False)
# axs.yaxis.get_major_formatter()._usetex = False
# axs.xaxis.get_major_formatter()._usetex = False
plt.savefig('h2_diff.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 


label_size=6
# colors1=['aquamarine','palegreen','C2','darkgreen','antiquewhite','tan','chocolate','C5']

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))

# axs.plot(df_h['Time'],media_h[8],c=colors[0],label=r'CT leaves T1',lw=0.5)
axs.plot(df_h['Time'],media_h[1]-media_h[0],c='aquamarine',label=r'Leaves T1',lw=0.5)
# axs.plot(df_h['Time'],media_h[9],c=colors[3],label=r'CT leaves T2',lw=0.5)
axs.plot(df_h['Time'],media_h[2]-media_h[0],c='palegreen',label=r'Leaves T2',lw=0.5)
# axs.plot(df_h['Time'],media_h[10],c=colors[5],label=r'CT Leaves T3',lw=0.5)
axs.plot(df_h['Time'],media_h[3]-media_h[0],c='C2',label=r'Leaves T3',lw=0.5)

# axs.plot(df_h['Time'],media_h[11],c=colors[7],label=r'CT Roots T1',lw=0.5)
axs.plot(df_h['Time'],media_h[5]-media_h[4],c='antiquewhite',label=r'Roots T1',lw=0.5)
# axs.plot(df_h['Time'],media_h[12],c=colors[10],label=r'CT Roots T2',lw=0.5)
axs.plot(df_h['Time'],media_h[6]-media_h[4],c='tan',label=r'Roots T2',lw=0.5)
# axs.plot(df_h['Time'],media_h[13],c=colors[10],label=r'CT Roots T3',lw=0.5)
axs.plot(df_h['Time'],media_h[7]-media_h[4],c='C5',label=r'Roots T3',lw=0.5)

axs.set_xlim(3.5,35)
axs.legend(fontsize=label_size, loc = "upper right",  ncol=1,
#            bbox_to_anchor = (0.25, 0.99), 
            fancybox=False,frameon=False)

plt.savefig('h0_diff.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 
plt.close(fig)


# In[76]:


label_size=5.5
plots_em_x=3
plots_em_y=3

fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(3.5*plots_em_x, 2.5*plots_em_y))

axs[0,0].plot(df_T['Time'],media_T[1]-media_T[0],c='C2',label='Leaves 50°C',lw=0.5)
# axs.plot(df_T['Time'],,c='darkgreen',label='Leaves 50°C',lw=0.5)
axs[0,0].plot(df_T['Time'],media_T[3]-media_T[2],c='C5',label='Roots 50°C',lw=0.5)


labels1=['Leaves 24h',
        'Leaves 48h',
        'Roots 24h',
        'Roots 48h']

colors1=['springgreen','C2','chocolate','C5']
axs[0,1].plot(df2_uv['Time'],media_UV[4]-media_UV[0],c=colors1[0],label=labels1[0],lw=0.5)
# axs.plot(df2_uv['Time'],,c=colors[4],label=labels[4],lw=0.5)
axs[0,1].plot(df2_uv['Time'],media_UV[5]-media_UV[2],c=colors1[1],label=labels1[1],lw=0.5)
# axs.plot(df2_uv['Time'],,c=colors[5],label=labels[5],lw=0.5)
axs[0,1].plot(df2_uv['Time'],media_UV2-media_UV[1],c=colors1[2],label=labels1[2],lw=0.5)
# axs.plot(df2_uv['Time'],,c='#8b7355ff',label='Roots 24h',lw=0.5)
axs[0,1].plot(df2_uv['Time'],media_UV[6]-media_UV[3],c=colors1[3],label=labels1[3],lw=0.5)



colors1=['aquamarine','palegreen','C2','darkgreen','antiquewhite','tan','chocolate','C5']
# axs.plot(df_meja['Time'],media_meja[0],c='#00979299',label='CT leaves 2 day',lw=0.5)
axs[0,2].plot(df_meja['Time'],media_meja[4]-media_meja[0],c=colors1[0],label='Leaves 40 µM 2d',lw=0.5)
axs[0,2].plot(df_meja['Time'],media_meja[5]-media_meja[0],c=colors1[1],label='Leaves 100 µM 2d',lw=0.5)
# axs.plot(df_meja['Time'],media_meja[1],c='#efda0596',label='CT roots 2 day',lw=0.5)
# axs.plot(df_meja['Time'],media_meja[2],c='#009792fd',label='CT leaves 4 day',lw=0.5)
axs[0,2].plot(df_meja['Time'],media_meja[8]-media_meja[2],c=colors1[2],label='Leaves 40 µM 4d',lw=0.5)
axs[0,2].plot(df_meja['Time'],media_meja[9]-media_meja[2],c=colors1[3],label='Leaves 100 µM 4d',lw=0.5)
axs[0,2].plot(df_meja['Time'],media_meja[6]-media_meja[1],c=colors1[4],label='Roots 40 µM 2d',lw=0.5)
axs[0,2].plot(df_meja['Time'],media_meja[7]-media_meja[1],c=colors1[5],label='Roots 100 µM 2d',lw=0.5)
# axs.plot(df_meja['Time'],media_meja[3],c='#fcd000ff',label='CT roots 4 day',lw=0.5)
axs[0,2].plot(df_meja['Time'],media_meja[10]-media_meja[3],c=colors1[6],label='Roots 40 µM 4d',lw=0.5)
axs[0,2].plot(df_meja['Time'],media_meja[11]-media_meja[3],c=colors1[7],label='Roots 100 µM 4d',lw=0.5)




colors1=['aquamarine','palegreen','C2','darkgreen','antiquewhite','tan','chocolate','C5']

# axs.plot(df_as['Time'],media_as[0],c='#00979299',label='CT leaves 2 day',lw=0.5)
axs[1,0].plot(df_as['Time'],media_as[4]-media_as[0],c=colors1[0],label='Leaves 1 mM 2d',lw=0.5)
axs[1,0].plot(df_as['Time'],media_as[5]-media_as[0],c=colors1[1],label='Leaves 2 mM 2d',lw=0.5)
axs[1,0].plot(df_as['Time'],media_as[8]-media_as[2],c=colors1[2],label='Leaves 1 mM 4d',lw=0.5)
axs[1,0].plot(df_as['Time'],media_as[9]-media_as[2],c=colors1[3],label='Leaves 2 mM 4d',lw=0.5)
# axs.plot(df_as['Time'],media_as[1],c='#efda0596',label='CT roots 2 day',lw=0.5)
axs[1,0].plot(df_as['Time'],media_as[6]-media_as[1],c=colors1[4],label='Roots 1 mM 2d',lw=0.5)
axs[1,0].plot(df_as['Time'],media_as[7]-media_as[1],c=colors1[5],label='Roots 2 mM 2d',lw=0.5)
# axs.plot(df_as['Time'],media_as[2],c='#009792fd',label='CT leaves 4 day',lw=0.5)
# axs.plot(df_as['Time'],media_as[3],c='#fcd000ff',label='CT roots 4 day',lw=0.5)
axs[1,0].plot(df_as['Time'],media_as[10]-media_as[3],c=colors1[6],label='Roots 1 mM 4d',lw=0.5)
axs[1,0].plot(df_as['Time'],media_as[11]-media_as[3],c=colors1[7],label='Roots 2 mM 4d',lw=0.5)


colors=['#009792fd','tan','lime','lightcoral',
         'aqua','teal','orange',
         'mediumseagreen','darkgreen','chocolate','sienna']

labels=['CT leaves 2d','CT roots 2d','CT leaves 4d','CT roots 4d',
        'Leaves 100 µM 2d','Leaves 200 µM 2d','Roots 200 µM 2d',
        'Leaves 100 µM 4d','Leaves 200 µM 4d','Roots 100 µM 4d','Roots 200 µM 4d']
# axs.plot(df2_snp['Time'],media_snp[0],c=colors[0],label=labels[0],lw=0.5)
axs[1,1].plot(df2_snp['Time'],media_snp[4]-media_snp[0],c=colors[4],label=labels[4],lw=0.5)
axs[1,1].plot(df2_snp['Time'],media_snp[5]-media_snp[0],c=colors[5],label=labels[5],lw=0.5)
# axs.plot(df2_snp['Time'],media_snp[2],c=colors[2],label=labels[2],lw=0.5)
axs[1,1].plot(df2_snp['Time'],media_snp[7]-media_snp[2],c=colors[7],label=labels[7],lw=0.5)
axs[1,1].plot(df2_snp['Time'],media_snp[8]-media_snp[2],c=colors[8],label=labels[8],lw=0.5)
# axs.plot(df2_snp['Time'],media_snp[1],c=colors[1],label=labels[1],lw=0.5)
axs[1,1].plot(df2_snp['Time'],media_snp2-media_snp[1],c='darkgoldenrod',label='Roots 100 µM 2d',lw=0.5)
axs[1,1].plot(df2_snp['Time'],media_snp[6]-media_snp[1],c=colors[6],label=labels[6],lw=0.5)
# axs.plot(df2_snp['Time'],media_snp[3],c=colors[3],label=labels[3],lw=0.5)
axs[1,1].plot(df2_snp['Time'],media_snp[9]-media_snp[3],c=colors[9],label=labels[9],lw=0.5)
axs[1,1].plot(df2_snp['Time'],media_snp[10]-media_snp[3],c=colors[10],label=labels[10],lw=0.5)


# axs.plot(df_dm['Time'],media_dm[0],c=colors[0],label='CT leaves 2d',lw=0.5)
axs[1,2].plot(df_dm['Time'],media_dm[4]-media_dm[0],c='aquamarine',label='Leaves 2d 25\%',lw=0.5)
axs[1,2].plot(df_dm['Time'],media_dm[5]-media_dm[0],c='palegreen',label='Leaves 2d 75\%',lw=0.5)
# axs.plot(df_dm['Time'],media_dm[2],c=colors[3],label='CT leaves 4d',lw=0.5)
axs[1,2].plot(df_dm['Time'],media_dm[8]-media_dm[2],c='C2',label='Leaves 4d 25\%',lw=0.5)
axs[1,2].plot(df_dm['Time'],media_dm[9]-media_dm[2],c='darkgreen',label='Leaves 4d 75\%',lw=0.5)
# axs.plot(df_dm['Time'],media_dm[1],c=colors[6],label='CT roots 2d',lw=0.5)
axs[1,2].plot(df_dm['Time'],media_dm[6]-media_dm[1],c='antiquewhite',label='Roots 2d 25\%',lw=0.5)
axs[1,2].plot(df_dm['Time'],media_dm[7]-media_dm[1],c='tan',label='Roots 2d 75\%',lw=0.5)
# axs.plot(df_dm['Time'],media_dm[3],c=colors[9],label='CT roots 4d',lw=0.5)
axs[1,2].plot(df_dm['Time'],media_dm[10]-media_dm[3],c='chocolate',label='Roots 4d 25\%',lw=0.5)
axs[1,2].plot(df_dm['Time'],media_dm[11]-media_dm[3],c='C5',label='Roots 4d 75\%',lw=0.5)



# axs.plot(df2_snp['Time'],media_nacl[0],c=colors[0],label='CT leaves 2d',lw=0.5)
axs[2,0].plot(df2_snp['Time'],media_nacl2-media_nacl[0],c='aquamarine',label='Leaves 2d 0,25M',lw=0.5)
axs[2,0].plot(df2_snp['Time'],media_nacl[4]-media_nacl[0],c='palegreen',label='Leaves 2d 0,50M',lw=0.5)
# axs.plot(df2_snp['Time'],media_nacl[2],c=colors[5],label='CT leaves 4d',lw=0.5)
axs[2,0].plot(df2_snp['Time'],media_nacl[6]-media_nacl[2],c='C2',label='Leaves 4d 0,25M',lw=0.5)
axs[2,0].plot(df2_snp['Time'],media_nacl[7]-media_nacl[2],c='darkgreen',label='Leaves 4d 0,50M',lw=0.5)

# axs.plot(df2_snp['Time'],media_nacl[1],c=colors[0],label='CT roots 2d',lw=0.5)
axs[2,0].plot(df2_snp['Time'],media_nacl3-media_nacl[1],c='antiquewhite',label='Roots 2d 0,25M',lw=0.5)
axs[2,0].plot(df2_snp['Time'],media_nacl[5]-media_nacl[1],c='tan',label='Roots 2d 0,50M',lw=0.5)
# axs.plot(df2_snp['Time'],media_nacl[3],c=colors[5],label='CT roots 4d',lw=0.5)
axs[2,0].plot(df2_snp['Time'],media_nacl[8]-media_nacl[3],c='chocolate',label='Roots 4d 0,25M',lw=0.5)
axs[2,0].plot(df2_snp['Time'],media_nacl[9]-media_nacl[3],c='C5',label='Roots 4d 0,50M',lw=0.5)


# axs.plot(df_aba['Time'],media_aba[0],c=colors[0],label=r'CT leaves 2d',lw=0.5)
axs[2,1].plot(df_aba['Time'],media_aba[4]-media_aba[0],c='aquamarine',label=r'Leaves 2d 25 mg/mL',lw=0.5)
axs[2,1].plot(df_aba['Time'],media_aba[5]-media_aba[0],c='palegreen',label=r'Leaves 2d 50 mg/mL',lw=0.5)
# axs.plot(df_aba['Time'],media_aba[2],c=colors[3],label=r'CT leaves 4d',lw=0.5)
axs[2,1].plot(df_aba['Time'],media_aba[8]-media_aba[2],c='C2',label=r'Leaves 4d 25 mg/mL',lw=0.5)
axs[2,1].plot(df_aba['Time'],media_aba[9]-media_aba[2],c='darkgreen',label=r'Leaves 4d 50 mg/mL',lw=0.5)
# axs.plot(df_aba['Time'],media_aba[1],c=colors[6],label=r'CT roots 2d',lw=0.5)
axs[2,1].plot(df_aba['Time'],media_aba[6]-media_aba[1],c='antiquewhite',label=r'Roots 2d 25 mg/mL',lw=0.5)
axs[2,1].plot(df_aba['Time'],media_aba[7]-media_aba[1],c='tan',label=r'Roots 2d 50 mg/mL',lw=0.5)
# axs.plot(df_aba['Time'],media_aba[3],c=colors[9],label=r'CT roots 4d',lw=0.5)
axs[2,1].plot(df_aba['Time'],media_aba[10]-media_aba[3],c='chocolate',label=r'Roots 4d 25 mg/mL',lw=0.5)
axs[2,1].plot(df_aba['Time'],media_aba[11]-media_aba[3],c='C5',label=r'Roots 4d 50 mg/mL',lw=0.5)


# axs.plot(df_h['Time'],media_h[8],c=colors[0],label=r'CT leaves T1',lw=0.5)
axs[2,2].plot(df_h['Time'],media_h[1]-media_h[8],c='aquamarine',label=r'Leaves T1',lw=0.5)
# axs.plot(df_h['Time'],media_h[9],c=colors[3],label=r'CT leaves T2',lw=0.5)
axs[2,2].plot(df_h['Time'],media_h[2]-media_h[9],c='palegreen',label=r'Leaves T2',lw=0.5)
# axs.plot(df_h['Time'],media_h[10],c=colors[5],label=r'CT Leaves T3',lw=0.5)
axs[2,2].plot(df_h['Time'],media_h[3]-media_h[10],c='C2',label=r'Leaves T3',lw=0.5)

# axs.plot(df_h['Time'],media_h[11],c=colors[7],label=r'CT Roots T1',lw=0.5)
axs[2,2].plot(df_h['Time'],media_h[5]-media_h[11],c='antiquewhite',label=r'Roots T1',lw=0.5)
# axs.plot(df_h['Time'],media_h[12],c=colors[10],label=r'CT Roots T2',lw=0.5)
axs[2,2].plot(df_h['Time'],media_h[6]-media_h[12],c='tan',label=r'Roots T2',lw=0.5)
# axs.plot(df_h['Time'],media_h[13],c=colors[10],label=r'CT Roots T3',lw=0.5)
axs[2,2].plot(df_h['Time'],media_h[7]-media_h[13],c='C5',label=r'Roots T3',lw=0.5)








axs[0,0].set_ylabel(r'Absorbance difference')
axs[1,0].set_ylabel(r'Absorbance difference')
axs[2,0].set_ylabel(r'Absorbance difference')
axs[2,0].set_xlabel(r'Retention time')
axs[2,1].set_xlabel(r'Retention time')
axs[2,2].set_xlabel(r'Retention time')


axs[0,0].set_xlim(3,35)
axs[0,1].set_xlim(3,35)
axs[0,2].set_xlim(3,35)
axs[1,0].set_xlim(3,35)
axs[1,1].set_xlim(3,35)
axs[1,2].set_xlim(3,35)
axs[2,0].set_xlim(3,35)
axs[2,1].set_xlim(3,35)
axs[2,2].set_xlim(3,35)


# axs[0,0].set_ylim(-0.5,2.5)
# axs[0,1].set_ylim(-0.5,2.5)
# axs[0,2].set_ylim(-0.5,2.5)
# axs[1,0].set_ylim(-0.5,2.5)
# axs[1,1].set_ylim(-0.5,2.5)
# axs[1,2].set_ylim(-0.5,2.5)
# axs[2,0].set_ylim(-0.5,2.5)
# axs[2,1].set_ylim(-0.5,2.5)
# axs[2,2].set_ylim(-0.5,2.5)

axs[0,0].legend(fontsize=5.6, loc = "upper right",  
           fancybox=False,frameon=False)
axs[0,1].legend(fontsize=5.6, loc = "upper right",  
           fancybox=False,frameon=False)
axs[0,2].legend(fontsize=5.6, loc = "upper right",  
           fancybox=False,frameon=False)
axs[1,0].legend(fontsize=5.6, loc = "upper right",  
           fancybox=False,frameon=False)
axs[1,1].legend(fontsize=5.6, loc = "upper right",  #fontsize=label_size
           fancybox=False,frameon=False)
axs[1,2].legend(fontsize=5.6, loc = "upper right",  
           fancybox=False,frameon=False)
axs[2,0].legend(fontsize=5.6, loc = "upper right",  
           fancybox=False,frameon=False)
axs[2,1].legend(fontsize=5.6, loc = "upper right",  
           fancybox=False,frameon=False)
axs[2,2].legend(fontsize=5.6, loc = "upper right",  
           fancybox=False,frameon=False)



axs[0,0].annotate('a)', xy=(0.03, 0.95),xycoords='axes fraction',
                      horizontalalignment='left', verticalalignment='top')
axs[0,1].annotate('b)', xy=(0.03, 0.95),xycoords='axes fraction',
                      horizontalalignment='left', verticalalignment='top')
axs[0,2].annotate('c)', xy=(0.03, 0.95),xycoords='axes fraction',
                      horizontalalignment='left', verticalalignment='top')
axs[1,0].annotate('d)', xy=(0.03, 0.95),xycoords='axes fraction',
                      horizontalalignment='left', verticalalignment='top')
axs[1,1].annotate('e)', xy=(0.03, 0.95),xycoords='axes fraction',
                       horizontalalignment='left', verticalalignment='top')
axs[1,2].annotate('f)', xy=(0.03, 0.95),xycoords='axes fraction',
                      horizontalalignment='left', verticalalignment='top')
axs[2,0].annotate('g)', xy=(0.03, 0.95),xycoords='axes fraction',
                      horizontalalignment='left', verticalalignment='top')
axs[2,1].annotate('h)', xy=(0.03, 0.95),xycoords='axes fraction',
                       horizontalalignment='left', verticalalignment='top')
axs[2,2].annotate('i)', xy=(0.03, 0.95),xycoords='axes fraction',
                      horizontalalignment='left', verticalalignment='top')

axs[0,0].yaxis.get_major_formatter()._usetex = False
axs[1,0].yaxis.get_major_formatter()._usetex = False
axs[2,0].yaxis.get_major_formatter()._usetex = False
axs[2,0].xaxis.get_major_formatter()._usetex = False
axs[2,1].xaxis.get_major_formatter()._usetex = False
axs[2,2].xaxis.get_major_formatter()._usetex = False
   
    
axs[0,0].tick_params(labelbottom=False)
axs[0,1].tick_params(labelbottom=False)
axs[0,2].tick_params(labelbottom=False)
axs[1,0].tick_params(labelbottom=False)
axs[1,1].tick_params(labelbottom=False)
axs[1,2].tick_params(labelbottom=False)
# axs[2,1].tick_params(labelbottom=False)
# axs[2,1].tick_params(labelbottom=False)
# axs[2,1].tick_params(labelbottom=False)
# axs[2,1].tick_params(labelbottom=False)
#     axs[0,1].tick_params(labelleft=False)
#     axs[1,1].tick_params(labelleft=False)





axs[0,0].annotate('Temperature', xy=(0.03, 0.1),xycoords='axes fraction',
                      horizontalalignment='left', verticalalignment='top')
axs[0,1].annotate('UV', xy=(0.03, 0.1),xycoords='axes fraction',
                      horizontalalignment='left', verticalalignment='top')
axs[0,2].annotate('MeJA', xy=(0.03, 0.1),xycoords='axes fraction',
                      horizontalalignment='left', verticalalignment='top')
axs[1,0].annotate('SA', xy=(0.03, 0.1),xycoords='axes fraction',
                      horizontalalignment='left', verticalalignment='top')
axs[1,1].annotate('SNP', xy=(0.03, 0.1),xycoords='axes fraction',
                       horizontalalignment='left', verticalalignment='top')
axs[1,2].annotate('MD', xy=(0.03, 0.1),xycoords='axes fraction',
                      horizontalalignment='left', verticalalignment='top')
axs[2,0].annotate('NaCl', xy=(0.03, 0.1),xycoords='axes fraction',
                      horizontalalignment='left', verticalalignment='top')
axs[2,1].annotate('ABA', xy=(0.03, 0.1),xycoords='axes fraction',
                       horizontalalignment='left', verticalalignment='top')
axs[2,2].annotate('Water stress', xy=(0.03, 0.1),xycoords='axes fraction',
                      horizontalalignment='left', verticalalignment='top')


axs[0,0].set_xticks([5,10,15,20,25,30,35])
axs[0,1].set_xticks([5,10,15,20,25,30,35])
axs[0,2].set_xticks([5,10,15,20,25,30,35])
axs[1,0].set_xticks([5,10,15,20,25,30,35])
axs[1,1].set_xticks([5,10,15,20,25,30,35])
axs[1,2].set_xticks([5,10,15,20,25,30,35])
axs[2,0].set_xticks([5,10,15,20,25,30,35])
axs[2,1].set_xticks([5,10,15,20,25,30,35])
axs[2,2].set_xticks([5,10,15,20,25,30,35])

axs[0,0].set_ylim(-0.3, 0.8)
axs[0,1].set_ylim(-0.3, 0.8)
axs[0,2].set_ylim(None, 0.8)
axs[1,0].set_ylim(None, 0.8)
axs[1,1].set_ylim(None, 2.5)
axs[1,2].set_ylim(None, 0.8)
axs[2,0].set_ylim(None, 0.8)
axs[2,1].set_ylim(None, 0.8)
axs[2,2].set_ylim(None, 0.8)


plt.savefig('all.pdf',bbox_inches='tight',pad_inches=0.1, transparent=True, dpi=500) 


# In[ ]:




