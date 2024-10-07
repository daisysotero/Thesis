#!/usr/bin/env python
# coding: utf-8

# In[ ]:

###############################  IMPORTS #####################################

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


###############################  FUNCTION #####################################


def function_fig_chromatogram_v2(plots_em_x, plots_em_y, h_size, v_size, 
                              tempo, lista_plots, lista_label, cores, linhas_por_painel,
                              alpha, lw, xlim_max, xlim_min, xticks, xticks_label, yticks, yticks_label,
                              ylabel, xlabel, dpi,
                              variacao_pontos, tempo_controle_asterisco, fontsize_asterisco,prominence,
                              loc, fontsize_legenda, fontsize_label, fontsize_letra, letra_painel,flag2,save_fig,formats):
    
    fig, axs = plt.subplots(plots_em_y,plots_em_x, figsize=(h_size*plots_em_x, v_size*plots_em_y),layout='constrained')
    
    if plots_em_x == 1 or plots_em_y == 1: #se tiver uma coluna ou linha
        numero_plot        = max(plots_em_x,plots_em_y)
        contador           = 0 
        contador_asterisco = 0
        
        for i in range (numero_plot):
            lista_media_painel = []
            contador_asterisco += 1
            for j in range(linhas_por_painel[i]):
                axs[i].plot(tempo, lista_plots[contador], label=lista_label[contador], 
                            lw=lw, alpha=alpha,c=cores[contador])
                contador+=1
                
            for l in range(1,linhas_por_painel[i] ):
                media_ct_tr = np.average([np.average(lista_plots[(contador_asterisco-1)*linhas_por_painel[i]]),
                                        np.average(lista_plots[(contador_asterisco-1)*linhas_por_painel[i] + l])])
                
                peaks, _    = find_peaks(lista_plots[(contador_asterisco-1)*linhas_por_painel[i] + l], prominence=prominence)  
#                 axs[i].scatter(tempo[peaks],lista_plots[(contador_asterisco-1)*linhas_por_painel[i] + l][peaks],s=2)
                sel = lista_plots[(contador_asterisco-1)*linhas_por_painel[i] + l][peaks] > media_ct_tr #selecionar os picos acima da média 
                for p in range (len(peaks[sel])):
                    maior_valor_controle = max(lista_plots[(contador_asterisco-1)*linhas_por_painel[i]][peaks[sel][p]-variacao_pontos:peaks[sel][p]+variacao_pontos]) #75 
                    razao = (lista_plots[(contador_asterisco-1)*linhas_por_painel[i] + l][peaks[sel][p]]) / (maior_valor_controle) #Fold Change
                    if razao >= 1.5 and tempo[peaks[sel][p]] < xlim_max: #limiar do fold - colcor o *
                        axs[i].text(tempo[peaks[sel][p]-tempo_controle_asterisco],
                                        1.01*lista_plots[(contador_asterisco-1)*linhas_por_painel[i] + l][peaks[sel][p]],
                                        '*',c=cores[l],fontsize=fontsize_asterisco) 
                    
            axs[i].set_ylabel(ylabel, fontsize = fontsize_label)
            axs[i].set_xlabel(xlabel, fontsize = fontsize_label)
            if len(xticks) > 0:
                axs[i].set_xticks(xticks, xticks_label, fontsize = fontsize_label)
            else:
                axs[i].tick_params(axis='x', labelsize=fontsize_label)
                
            if len(yticks[i]) > 0:
                axs[i].set_yticks(yticks[i], yticks_label[i], fontsize = fontsize_label)
            else:
                axs[i].tick_params(axis='y', labelsize=fontsize_label)
            axs[i].set_xlim(xlim_min, xlim_max)
            axs[i].legend(fontsize = fontsize_legenda, loc = "upper right", fancybox=False, frameon=False)
            axs[i].annotate(letra_painel[i], xy=(0.03, 0.95), xycoords='axes fraction', 
                            fontsize=fontsize_letra, horizontalalignment='left', verticalalignment='top')
            
    else:#se n tiver uma coluna ou linha
        contador_plot      = 0
        contador_letra     = 0
        contador_asterisco = 0
        for j in range (plots_em_y):
            for i in range (plots_em_x):
                contador_asterisco += 1
                if j == 3 and i == 0:
                    ax1 = axs[j,i].inset_axes([0.677, 0.17, 0.3, 0.53]) 
                if j == 4 and i == 0:
                    ax2 = axs[j,i].inset_axes([0.677, 0.17, 0.3, 0.53])
                for k in range(linhas_por_painel[contador_letra]):
                    axs[j,i].plot(tempo, lista_plots[contador_plot], label=lista_label[contador_plot],
                                  c=cores[contador_plot], lw=lw, alpha=alpha)
                    if j == 3 and i == 0:
                        ax1.plot(tempo, lista_plots[contador_plot], label=lista_label[contador_plot],
                                  c=cores[contador_plot], lw=lw, alpha=alpha)
                        ax1.set_xlim(10,22)
                        ax1.set_ylim(0.0,0.3) 
                        ax1.tick_params(axis='x', labelsize=6)
                        ax1.tick_params(axis='y', labelsize=6)
                        ax1.set_xticks([10, 15, 20]) 
                        ax1.set_xticklabels([10, 15, 20])
                        ax1.set_yticks([0.0, 0.1, 0.2,0.3])
                        ax1.set_yticklabels([0.0, 0.1, 0.2,0.3])
                    if j == 4 and i == 0:
                        ax2.plot(tempo, lista_plots[contador_plot], label=lista_label[contador_plot],
                                  c=cores[contador_plot], lw=lw, alpha=alpha)
                        ax2.set_xlim(10,22)
                        ax2.set_ylim(0.0,0.25) 
                        ax2.tick_params(axis='x', labelsize=6)
                        ax2.tick_params(axis='y', labelsize=6)
                        ax2.set_xticks([10, 15, 20]) 
                        ax2.set_xticklabels([10, 15, 20])
                        ax2.set_yticks([0.0, 0.1, 0.2])
                        ax2.set_yticklabels([0.0, 0.1, 0.2])
                    contador_plot += 1
                if i ==1 and flag2==True:
                    for l in range(1,linhas_por_painel[contador_letra]):
                        print(contador_plot - linhas_por_painel[contador_letra],cores[contador_plot-linhas_por_painel[contador_letra]],
                             contador_plot - linhas_por_painel[contador_letra]+l,cores[contador_plot-linhas_por_painel[contador_letra]+l])
                        media_ct_tr = np.average([np.average(lista_plots[contador_plot - linhas_por_painel[contador_letra]]),
                                                np.average(lista_plots[contador_plot - linhas_por_painel[contador_letra]+l])])              

                        peaks, _    = find_peaks(lista_plots[contador_plot - linhas_por_painel[contador_letra]+l], prominence=prominence)  
#                         axs[j,i].scatter(tempo[peaks],lista_plots[contador_plot - linhas_por_painel[contador_letra]+l][peaks],s=2)
                        sel         = lista_plots[contador_plot - linhas_por_painel[contador_letra]+l][peaks] > media_ct_tr #selecionar os picos acima da média 
                        for p in range (len(peaks[sel])):
                            maior_valor_controle = max(lista_plots[contador_plot - linhas_por_painel[contador_letra]][peaks[sel][p]-variacao_pontos:peaks[sel][p]+variacao_pontos]) #75 
                            razao = (lista_plots[contador_plot - linhas_por_painel[contador_letra]+l][peaks[sel][p]]) / (maior_valor_controle) #Fold Change
                            if razao >= 1.5 and tempo[peaks[sel][p]] < xlim_max: #limiar do fold - colcor o *
                                axs[j,i].text(tempo[peaks[sel][p]-tempo_controle_asterisco],
                                                1.01*lista_plots[contador_plot - linhas_por_painel[contador_letra]+l][peaks[sel][p]],
                                                '*',c=cores[contador_plot - linhas_por_painel[contador_letra]+l], fontsize=fontsize_asterisco) 
                            
                axs[j,i].set_ylabel(ylabel[contador_letra], fontsize = fontsize_label)
                axs[j,i].set_xlabel(xlabel, fontsize = fontsize_label)
                if len(xticks) > 0:
                    axs[j,i].set_xticks(xticks, xticks_label, fontsize = fontsize_label)
                else:
                    axs[j,i].tick_params(axis='x', labelsize=fontsize_label)
                if len(yticks[contador_letra]) > 0:
                    axs[j,i].set_yticks(yticks[contador_letra], yticks_label[contador_letra], fontsize = fontsize_label)
                else:
                    axs[j,i].tick_params(axis='y', labelsize=fontsize_label)
                axs[j,i].set_xlim(xlim_min, xlim_max)
                axs[j,i].legend(fontsize=fontsize_legenda, loc = loc[contador_letra], fancybox=False,frameon=False)
                axs[j,i].annotate(letra_painel[contador_letra], xy=(0.03, 0.95),xycoords='axes fraction',
                                  fontsize=fontsize_letra, horizontalalignment='left', verticalalignment='top')
                contador_letra+=1    
                
    for i in range(len(formats)):
        plt.savefig(save_fig+formats[i], bbox_inches='tight', pad_inches=0.1, transparent=True, dpi=dpi)     
#     plt.close()
    return None


###############################  PLOT #####################################
###############################  EXEMPLE: TEMPERATURE #####################################



tempo         = temp_ori_normalizado_media['Time']
lista_plots   = [temp_ori_normalizado_media['FT50']-temp_ori_normalizado_media['FT24'],
                 temp_ori_normalizado_media['RT50']-temp_ori_normalizado_media['RT24'],
                
                temp_ori_normalizado_media['FT24'],temp_ori_normalizado_media['FT50'],
                
                uv_ori_normalizado_media['FUV24']-uv_ori_normalizado_media['FCUV24'],
                uv_ori_normalizado_media['FUV48']-uv_ori_normalizado_media['FCUV48'],
                uv_ori_normalizado_media['RUV24']-uv_ori_normalizado_media['RCUV24'],
                uv_ori_normalizado_media['RUV48']-uv_ori_normalizado_media['RCUV48'],

                uv_ori_normalizado_media['FCUV48'],uv_ori_normalizado_media['FUV48'],
                
                hidrico_ori_normalizado_media['FTH1']-hidrico_ori_normalizado_media['FCTH1'],
                hidrico_ori_normalizado_media['FTH2']-hidrico_ori_normalizado_media['FCTH2'],
                hidrico_ori_normalizado_media['FTH3']-hidrico_ori_normalizado_media['FCTH3'],
                hidrico_ori_normalizado_media['RTH1']-hidrico_ori_normalizado_media['RCTH1'],
                hidrico_ori_normalizado_media['RTH2']-hidrico_ori_normalizado_media['RCTH2'],
                hidrico_ori_normalizado_media['RTH3']-hidrico_ori_normalizado_media['RCTH3'],
                
                hidrico_ori_normalizado_media['FCTH3'],hidrico_ori_normalizado_media['FTH3'],
                
                nacl_ori_normalizado_media['FS252']-nacl_ori_normalizado_media['FC242'],
                nacl_ori_normalizado_media['FS502']-nacl_ori_normalizado_media['FC242'],
                nacl_ori_normalizado_media['FS254']-nacl_ori_normalizado_media['FC244'],
                nacl_ori_normalizado_media['FS504']-nacl_ori_normalizado_media['FC244'],
                nacl_ori_normalizado_media['RS252']-nacl_ori_normalizado_media['RC242'],
                nacl_ori_normalizado_media['RS502']-nacl_ori_normalizado_media['RC242'],
                nacl_ori_normalizado_media['RS254']-nacl_ori_normalizado_media['RC244'],
                nacl_ori_normalizado_media['RS504']-nacl_ori_normalizado_media['RC244'],
                
                nacl_ori_normalizado_media['RC242'],nacl_ori_normalizado_media['RS252'],
                                                              nacl_ori_normalizado_media['RS502'],
                 
                
                dm_ori_normalizado_media['FDM12']-dm_ori_normalizado_media['FC242'],
                dm_ori_normalizado_media['FDM32']-dm_ori_normalizado_media['FC242'],
                dm_ori_normalizado_media['FDM14']-dm_ori_normalizado_media['FC244'],
                dm_ori_normalizado_media['FDM34']-dm_ori_normalizado_media['FC244'],
                dm_ori_normalizado_media['RDM12']-dm_ori_normalizado_media['RC242'],
                dm_ori_normalizado_media['RDM32']-dm_ori_normalizado_media['RC242'],
                dm_ori_normalizado_media['RDM14']-dm_ori_normalizado_media['RC244'],
                dm_ori_normalizado_media['RDM34']-dm_ori_normalizado_media['RC244'],
                 
                
                
                dm_ori_normalizado_media['FC242'],dm_ori_normalizado_media['FDM12'],
                                                        dm_ori_normalizado_media['FDM32']]



lista_label   = ['Leaves 50$^{\circ}$C',
                 'Roots 50$^{\circ}$C',
                
                'Leaves 24$^{\circ}$C',
                'Leaves 50$^{\circ}$C',
                
                 'Leaves 24h','Leaves 48h','Roots 24h', 'Roots 48h',
                
                 'Leaves CT 48h','Leaves 48h',
                 
                 'Leaves T1','Leaves T2','Leaves T3','Roots T1','Roots T2','Roots T3',
                 
                 'Leaves CT3','Leaves T3',
                 
                 'Leaves 2d 0.25 M','Leaves 2d 0.50 M','Leaves 4d 0.25 M','Leaves 4d 0.50 M',
                 'Roots 2d 0.25 M','Roots 2d 0.50 M','Roots 4d 0.25 M','Roots 4d 0.50 M',
                
                 'Roots CT 2d','Roots 2d 0.25 M','Roots 2d 0.50 M',
                 
                 'Leaves 2d 25%','Leaves 2d 75%','Leaves 4d 25%','Leaves 4d 75%',
                 'Roots 2d 25%','Roots 2d 75%','Roots 4d 25%','Roots 4d 75%',
                
                  'Leaves CT 2d', 'Leaves 2d 25%','Leaves 2d 75%']


lista_cores   = ['C2', 'C5',
                 'C0','C1',
                 'springgreen','C2','chocolate','C5',
                 'C0','C1',
                 'aquamarine','palegreen','C2','#E89C40','tan','C5',
                 'C0','C1',
                 'aquamarine','palegreen','C2','darkgreen','#F0CD9A','tan','chocolate','C5',
                 'C0','C1','C2',
                 'aquamarine','palegreen','C2','darkgreen','#F0CD9A','tan','chocolate','C5',
                 'C0','C1','C2']

linhas_por_painel = [2,2,
                     4,2,
                     6,2,
                     8,3,
                     8,3]

plots_em_x = 2
plots_em_y = 5
h_size     = 3.2 #tamanho horizontal do painel em polegadas
v_size     = 2.0 #tamanho vertical do painel em polegadas #h_size/1.618  #2.5

alpha        = 0.8
lw           = 0.5 #grossura da linha
xlim_max     = 35
xlim_min     = 2.5
xticks       = [5, 10, 15, 20, 25, 30, 35]  #se lista vazia, python escolhe os numeros
xticks_label = ['5','10','15','20','25','30','35'] #se lista vazia, python escolhe os numeros
xticks_label = ['5','10','15','20','25','30','35'] #se lista vazia, python escolhe os numeros
yticks       = [ [-0.4,-0.2,0.0,0.2,0.4,0.6,0.8,1.0],
                 [0.0,0.2,0.4,0.6,0.8,1.0],
                 [-0.4,-0.2,0.0,0.2,0.4,0.6,0.8,1.0],
                 [0.0,0.2,0.4,0.6,0.8,1.0],
                 [-0.4,-0.2,0.0,0.2,0.4,0.6,0.8,1.0],
                 [0.0,0.2,0.4,0.6,0.8,1.0,1.2],
                 [-4.0,-3.0,-2.0,-1.0,0.0, 1.0],
                 [0.0,0.1,0.2,0.3,0.4],
                 [-4.0,-3.0,-2.0,-1.0,0.0, 1.0],
                 [0.0,0.1,0.2,0.3,0.4]] #se lista vazia, python escolhe os numeros
yticks_label = [['-0.4','-0.2','0.0','0.2','0.4','0.6','0.8','1.0'],
                ['0.0','0.2','0.4','0.6','0.8','1.0'],
                ['-0.4','-0.2','0.0','0.2','0.4','0.6','0.8','1.0'],
                ['0.0','0.2','0.4','0.6','0.8','1.0'],
                ['-0.4','-0.2','0.0','0.2','0.4','0.6','0.8','1.0'],
                ['0.0','0.2','0.4','0.6','0.8','1.0','1.2'],
                ['-4.0','-3.0','-2.0','-1.0','0.0', '1.0'],
                ['0.0','0.1','0.2','0.3','0.4'],
                ['-4.0','-3.0','-2.0','-1.0','0.0', '1.0'],
                ['0.0','0.1','0.2','0.3','0.4']] #se lista vazia, python escolhe os numeros

ylabel       = [r"$\bf{TEMPERATURE}$" + "\n" + "Absorbance (280 nm)",'',  
               r"$\bf{ULTRAVIOLET\ LIGTH}$" + "\n" + "Absorbance (280 nm)", '', #(r"$\bf{ABSCISIC\ ACID}$" + "\n" + "Absorbance (280 nm)")
               r"$\bf{WATER\ STRESS}$" + "\n" + "Absorbance (280 nm)", '',
               r"$\bf{SALINE\ STRESS}$" + "\n" + "Absorbance (280 nm)", '',
               r"$\bf{MECHANICAL\ DAMAGE}$" + "\n" + "Absorbance (280 nm)", '']
xlabel       = r'Retention time'

loc                =  ["upper right", "upper right",
                      "upper right", "upper right",
                      "upper right", "upper right",
                      "lower left", "upper right",
                      "lower left", "upper right"]
fontsize_legenda   = 5.5
fontsize_label     = 8 # tamanho das legendas e dos números do eixo
fontsize_letra     = 8 # tamanho da letra do painel
fontsize_asterisco = 5

variacao_pontos          = 75 #andar 75 pontos pra trás e e frente
tempo_controle_asterisco = 100 #mover o * para esquerda ou direita
prominence               = 0.01 #numero que identifica o pico, valores altos identifica poucos

letra_painel2 = ['a)','b)']
letra_painel4 = ['a)','b)','c)','d)']
letra_painel6 = ['a)','b)','c)','d)','e)','f)']
letra_painel10 = ['a)','b)','c)','d)','e)','f)','g)','h)','i)','j)']

dpi     = 500
caminho = r'E:\Doc\Cap 2 - Tratadas_HPLC_Evelu\Analise_HPLC\RESULTADOS_PROCESSADOS\Manuscrito\Plant_Biology\Re-submission\Final_figures\new\Figures'
file    = r'\f2_norm_final'
formats = ['.pdf','.jpg','.tiff']
flag2=True

###############################  PLOT USING THE FUNCTION #####################################

function_fig_chromatogram_v2(plots_em_x, plots_em_y, h_size, v_size,
                          tempo, lista_plots, lista_label, lista_cores, linhas_por_painel,
                          alpha, lw, xlim_max, xlim_min, xticks, xticks_label, yticks, yticks_label, ylabel, xlabel, dpi,
                          variacao_pontos, tempo_controle_asterisco, fontsize_asterisco, prominence,
                          loc, fontsize_legenda, fontsize_label, fontsize_letra, letra_painel10, flag2,caminho+file, formats)

