#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import pandas as pd
import os


# In[3]:


arq1=r'E:\Doc\Cap 3 - GR_Evelu\Resultados_PCRs\Serrapilheira\housekeeping_salvo_no_area_trabalho\Figuras\scatter_plot.xlsx'
arq2=r'E:\Doc\Cap 3 - GR_Evelu\Resultados_PCRs\Serrapilheira\housekeeping_salvo_no_area_trabalho\Figuras\grapico2.xlsx'
df1 = pd.read_excel(arq1)
df2 = pd.read_excel(arq2)


# In[4]:


plots_em_x=1
plots_em_y=1
label_size=10
ticksize=10
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(4*plots_em_x, 3*plots_em_y))
   
plt.plot(df1['geNorm'],label='geNorm (field)',lw=0.5,marker='o',ms=5,mew=0, fillstyle='full',markerfacecolor='#008a45ff')
plt.plot(df1['NormFinder'],label='NormFinder (field)',lw=0.5,marker='o',ms=5,mew=0, fillstyle='full',markerfacecolor='#ee7500ff')
axs.set_xticks([0,1,2,3,4,5,6,7,8,9,10])
plt.plot((0,10),(0.5,0.5), color='black',lw=1,alpha=0.6)
# axs.set_yticks([0.5,1])
axs.set_xticklabels(df2['Transcript'],rotation=45,fontsize=ticksize)
# axs.set_yticks(fontsize=ticksize)
axs.set_xlabel(r'Transcript',fontsize=label_size)
axs.set_ylabel(r'Stability M',fontsize=label_size)
#axs.annotate('a)', xy=(0.03, 0.95),xycoords='axes fraction',
 #                     horizontalalignment='left', verticalalignment='top')
axs.legend(fontsize=label_size, frameon=False)#,bbox_to_anchor=(0.5, 0.4))#loc= 'lower right' )#, )
#plt.savefig(r'D:\Doc\Cap 3 - GR_Evelu\Resultados_PCRs\Serrapilheira\housekeeping_salvo_no_area_trabalho\Figuras\scatter_plot.pdf',bbox_inches='tight',pad_inches=0.02, transparent=True, dpi=700)


# In[ ]:




