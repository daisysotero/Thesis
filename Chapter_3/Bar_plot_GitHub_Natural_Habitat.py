#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import pandas as pd
import os


# In[ ]:


arq1=r'E:\Doc\Cap 3 - GR_Evelu\Resultados_PCRs\Serrapilheira\housekeeping_salvo_no_area_trabalho\Figuras\scatter_pairwise_normfinder_serrapilheira.xlsx'
df1 = pd.read_excel(arq1)


# In[ ]:


plots_em_x=1
plots_em_y=1
label_size=10
ticksize=8.3
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(5*plots_em_x, 2*plots_em_y))

x=[0,1,2,3,4,5,6,7,8,9]
   
plt.bar(x,df1['Stability'],label='Stability', color='C0', width=0.8, edgecolor='black')#,lw=0.5,marker='o',ms=5,mew=0, fillstyle='full',markerfacecolor='C0')
#plt.plot(df1['NormFinder'],label='NormFinder',lw=0.5,marker='o',ms=5,mew=0, fillstyle='full',markerfacecolor='C1')
axs.set_xticks([0,1,2,3,4,5,6,7,8,9])
# axs.set_yticks([0.5,1])
AA=['CSTF64\nNLE',
'OAT\nRAB7',
'26S\nCSTF64',
'CSTF64\nOAT',
'26S\nNLE',
'NLE\nRAB7',
'26S\nRAB7',
'NLE\nOAT',
'26S\nOAT',
'CSTF64\nRAB7']
axs.set_xticklabels(AA,rotation=45,fontsize=ticksize)
# axs.set_yticks(fontsize=ticksize)
axs.set_xlabel(r'Transcript',fontsize=label_size)
axs.set_ylabel(r'Stability',fontsize=label_size)
#axs.annotate('a)', xy=(0.03, 0.95),xycoords='axes fraction',
 #                     horizontalalignment='left', verticalalignment='top')
#axs.legend(fontsize=label_size, frameon=False)#,bbox_to_anchor=(0.5, 0.4))#loc= 'lower right' )#, )
#plt.savefig(r'C:\Users\daisy\Desktop\housekeeping\Figuras\bar_plot_pairwise.pdf',bbox_inches='tight',pad_inches=0.02, transparent=True, dpi=700)

