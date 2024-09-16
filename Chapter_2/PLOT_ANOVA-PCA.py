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


def confidence_ellipse(x, y, ax, n_std=1.645, facecolor='none', edgecolor='black', **kwargs):
    if x.size != y.size:
        raise ValueError("x and y must be the same size")

    cov = np.cov(x, y)
    pearson = cov[0, 1] / np.sqrt(cov[0, 0] * cov[1, 1])
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
    ellipse = Ellipse((0, 0),
                      width=ell_radius_x * 2,
                      height=ell_radius_y * 2,
                      facecolor=facecolor,
                      edgecolor=edgecolor,
                      **kwargs)

    scale_x = np.sqrt(cov[0, 0]) * n_std
    scale_y = np.sqrt(cov[1, 1]) * n_std

    transf = transforms.Affine2D()         .rotate_deg(45)         .scale(scale_x, scale_y)         .translate(np.mean(x), np.mean(y))

    ellipse.set_transform(transf + ax.transData)
    return ax.add_patch(ellipse)


# In[ ]:



###### FOLHAS ######

scores_leaves = pd.read_csv(r"..\Temp_Leaves_scoresRobPCA.csv")
loadings_leaves = pd.read_csv(r"..\Temp_Leaves_loadingsRobPCA.csv")

scores_leaves['samples'] = scores_leaves['samples'].str.split('_').str[:2].str.join('_')
scores_leaves

s_leaves_24 = scores_leaves[scores_leaves['samples'].str.contains("Leaves_24h")]
s_leaves_50 = scores_leaves[scores_leaves['samples'].str.contains("Leaves_48h")]
s_leaves_24


# ###### RAÍZES ######

scores_roots = pd.read_csv(r"..\Temp_Roots_scoresRobPCA.csv")
loadings_roots = pd.read_csv(r"..\Temp_Roots_loadingsRobPCA.csv")

scores_roots['samples'] = scores_roots['samples'].str.split('_').str[:2].str.join('_')
scores_roots

s_roots_24 = scores_roots[scores_roots['samples'].str.contains("Roots_24h")]
s_roots_50 = scores_roots[scores_roots['samples'].str.contains("Roots_48h")]
s_roots_50


# In[ ]:


label_size=8
plots_em_x=2
plots_em_y=2

fig, axs= plt.subplots(plots_em_y,plots_em_x, 
                       figsize=(3*plots_em_x, 1.8*plots_em_y),
                       constrained_layout=True)

axs[0,0].axhline(y=0, color='gray', linestyle='--',lw=0.2, alpha=0.7)
axs[0,0].axvline(x=0, color='gray', linestyle='--',lw=0.2, alpha=0.7)

axs[0,0].scatter(s_leaves_24['PC1'],s_leaves_24['PC2'],c='#1b9e77',s=4,alpha=0.8,label='Leaves 24$^{\circ}$C')
axs[0,0].scatter(s_leaves_50['PC1'],s_leaves_50['PC2'],c='#d95f02',s=4,alpha=0.8,label='Leaves 50$^{\circ}$C')

axs[0,0].set_xlabel(r'PC1',fontsize=5.5)
axs[0,0].set_ylabel(r'PC2',fontsize=5.5)

axs[0,0].set_xticks([-4,-2,0,2,4,6],['-4','-2','0','2','4','6'])
axs[0,0].set_yticks([-2,0,2,4],['-2','0','2','4'])

# Ajuste os limites dos eixos
axs[0,0].set_xlim(-5, 6.5)
axs[0,0].set_ylim(-3, 5)

axs[0,0].legend(frameon=False,bbox_to_anchor=(1, 1),
                loc='upper right', fontsize=5)
 
            
axs[0,0].annotate('a)', xy=(0.03, 0.95),xycoords='axes fraction',fontsize=6.5,
                      horizontalalignment='left', verticalalignment='top')



# Adicionando elipses de confiança aos dados com cores
confidence_ellipse(s_leaves_24['PC1'], s_leaves_24['PC2'], axs[0,0], n_std=2.0, 
                   facecolor='#1b9e77', edgecolor='#1b9e77', alpha=0.2)

confidence_ellipse(s_leaves_50['PC1'], s_leaves_50['PC2'], axs[0,0], n_std=2.0, 
                   facecolor='#d95f02', edgecolor='#d95f02', alpha=0.2)

    
#######################################################################################################

axs[0,1].plot(loadings_leaves['time'],loadings_leaves['PC1'],label='PC1',lw=0.5,alpha=0.7, c='C0')
axs[0,1].plot(loadings_leaves['time'],loadings_leaves['PC2'],label='PC2',lw=0.5,c='C3')

axs[0,1].set_xlim(3,35)
axs[0,1].set_xticks([5,10,15,20,25,30,35],['5','10','15','20','25','30','35'])
axs[0,1].set_yticks([-0.05,0,0.05,0.1,0.15],['-0.05','0.0','0.05','0.10','0.15'])

axs[0,1].set_ylabel(r'Variable',fontsize=5)
axs[0,1].set_xlabel(r'Retention time',fontsize=5)

# Adicione a legenda e ajuste o tamanho do texto
# axs[1].legend(bbox_to_anchor=(0.76, 0.95), loc='upper left', fontsize=9, title_fontsize=12)
axs[0,1].legend(frameon=False,fontsize=5,
               bbox_to_anchor=(1,1), loc='upper right')

axs[0,1].grid(False)

            
axs[0,1].annotate('b)', xy=(0.03, 0.95),xycoords='axes fraction',fontsize=6.5,
                      horizontalalignment='left', verticalalignment='top')



#######################################################################################################

axs[1,0].axhline(y=0, color='gray', linestyle='--',lw=0.2, alpha=0.7)
axs[1,0].axvline(x=0, color='gray', linestyle='--',lw=0.2, alpha=0.7)

axs[1,0].scatter(s_roots_24['PC1'],s_roots_24['PC2'],c='#1b9e77',s=4,alpha=0.8,label='Roots 24$^{\circ}$C')
axs[1,0].scatter(s_roots_50['PC1'],s_roots_50['PC2'],c='#d95f02',s=4,alpha=0.8,label='Roots 50$^{\circ}$C')


axs[1,0].set_xlabel(r'PC1',fontsize=5.5)
axs[1,0].set_ylabel(r'PC2',fontsize=5.5)

axs[1,0].set_xticks([-4,-2,0,2,4],['-4','-2','0','2','4'])
axs[1,0].set_yticks([-2,-1,0,1,2],['-2','-1','0','1','2'])

# Ajuste os limites dos eixos
axs[1,0].set_xlim(-5, 5.5)
axs[1,0].set_ylim(-2, 3)

axs[1,0].legend(frameon=False,bbox_to_anchor=(1,1), 
                loc='upper right', fontsize=5)

# # Adicione grades cinzas mais claras
axs[1,0].grid(False)

           
axs[1,0].annotate('c)', xy=(0.03, 0.95),xycoords='axes fraction',fontsize=6.5,
                      horizontalalignment='left', verticalalignment='top')



# Adicionando elipses de confiança aos dados com cores
confidence_ellipse(s_roots_24['PC1'], s_roots_24['PC2'], axs[1,0], n_std=2.0, 
                   facecolor='#1b9e77', edgecolor='#1b9e77', alpha=0.2)

confidence_ellipse(s_roots_50['PC1'], s_roots_50['PC2'], axs[1,0], n_std=2.0, 
                   facecolor='#d95f02', edgecolor='#d95f02', alpha=0.2)

    
#######################################################################################################   

axs[1,1].plot(loadings_roots['time'],loadings_roots['PC1'],label='PC1',lw=0.5,alpha=0.7, c='C0')
axs[1,1].plot(loadings_roots['time'],loadings_roots['PC2'],label='PC2',lw=0.5,c='C3')

axs[1,1].set_xlim(3,35)
axs[1,1].set_xticks([5,10,15,20,25,30,35])
axs[1,1].set_yticks([-0.10,-0.05,0,0.05,0.10],['-0.10','-0.05','0.0','0.05','0.10'])

axs[1,1].set_xlabel(r'Retention time',fontsize=5)
axs[1,1].set_ylabel(r'Variable',fontsize=5)

# Adicione a legenda e ajuste o tamanho do texto
# axs[1].legend(bbox_to_anchor=(0.76, 0.95), loc='upper left', fontsize=9, title_fontsize=12)
axs[1,1].legend(frameon=False,fontsize=5,
                bbox_to_anchor=(1,1), loc='upper right')

   
axs[1,1].grid(False)

            
axs[1,1].annotate('d)', xy=(0.03, 0.95),xycoords='axes fraction',fontsize=6.5,
                      horizontalalignment='left', verticalalignment='top')


plt.savefig(r'E:\Doc\Cap 2 - Tratadas_HPLC_Evelu\Analise_HPLC\RESULTADOS_PROCESSADOS\Manuscrito\Plant_Biology\Re-submission\Final_figures\new\Figures\new_anova_pca_final\ANOVA-PC_05_09_2024\temp.pdf',bbox_inches='tight',pad_inches=0.02, transparent=True, dpi=700)
plt.savefig(r'E:\Doc\Cap 2 - Tratadas_HPLC_Evelu\Analise_HPLC\RESULTADOS_PROCESSADOS\Manuscrito\Plant_Biology\Re-submission\Final_figures\new\Figures\new_anova_pca_final\ANOVA-PC_05_09_2024\temp.png',bbox_inches='tight',pad_inches=0.02, transparent=True, dpi=700)

