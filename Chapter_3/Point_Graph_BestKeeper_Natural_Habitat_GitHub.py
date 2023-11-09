#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import pandas as pd
import os


# In[ ]:


arq1=r'E:\Doc\Cap 3 - GR_Evelu\Resultados_PCRs\Serrapilheira\housekeeping_salvo_no_area_trabalho\Figuras\grapico2.xlsx'
df1 = pd.read_excel(arq1)
print(df1)


# In[ ]:


X=[0,1,2,3,4,5,6,7,8,9,10]

plots_em_x=1
plots_em_y=1
label_size=10
ticksize=10
fig, axs= plt.subplots(plots_em_y,plots_em_x, figsize=(4*plots_em_x, 3*plots_em_y))
   
# plt.errorbar(X,df1['AM[Cq]'],df1['SD[+/- x-fold]'],marker='o',fmt=' ', ms=5,capsize=3,label=' ')
# plt.errorbar(X,df1['AM[Cq]'],df1['SD[+/- Cq]'],marker='o')#,fmt=' ', ms=5,capsize=3,label=' ')
axs.plot(X,df1['SD[+/- Cq]'],lw=0.5,marker='o',label='SD [+/- Cq]')
axs.plot(X,df1['SD[+/- x-fold]'],lw=0.5,marker='o',label='SD [+/- x-fold]')
axs.set_ylim(0,4)

#Segundo eixo = ax2
ax2 = axs.twinx()
ax2.plot(X,df1['CV[%Cq]'],lw=0.5,marker='X',ms=5,c='C2',label='CV [%Cq]')
ax2.set_ylim(0,5.2)

ax2.set_ylabel("Coefficient of variation [%Cq]", c='C2', fontsize=10)
ax2.tick_params(axis="y", labelcolor='C2')
ax2.spines['right'].set_color('C2')

axs.set_xticks([0,1,2,3,4,5,6,7,8,9,10]) #colocar o risquinho do eixo em todos esses números

#Colcoar a legenda do eixo x rotacionado
axs.set_xticklabels(df1['Transcript'],rotation=45,fontsize=ticksize)
# axs.set_yticks(fontsize=ticksize)
#Legenda dos eixos
axs.set_xlabel(r'Transcript',fontsize=label_size)
axs.set_ylabel(r'Standard deviation (SD)',fontsize=label_size)

#legenda dentro da figura
axs.legend(fontsize=label_size, frameon=False,loc= 'upper left')
ax2.legend(fontsize=label_size, frameon=False,loc= 'upper left',bbox_to_anchor=(0.004, 0.82))#,bbox_to_anchor=(0.5, 0.4))#loc= 'lower right' )#, )
#plt.savefig(r'C:\Users\daisy\Desktop\housekeeping\Figuras\point_plot.pdf',bbox_inches='tight',pad_inches=0.02, transparent=True, dpi=700)

