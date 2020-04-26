# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 10:11:31 2019

@author: Amelie
"""

dir_to_files = 'Data\\'

#SET DIRECTORY
import os
os.chdir(dir_to_files)

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os, sys
import seaborn as sns
import matplotlib.pyplot as plt
import scipy
import scipy.cluster.hierarchy as sch

datos_porrito_effectos = pd.read_pickle("datos_porrito_effectos.pkl")
datos_porrito_sabores = pd.read_pickle("datos_porrito_sabores.pkl")

datos_porrito_effectos_alcaloides = pd.read_pickle("ddatos_porrito_effectos_alcaloides.pkl")
datos_porrito_sabores_alcaloides = pd.read_pickle("datos_porrito_sabores_alcaloides.pkl")

labels = pd.read_excel('Labels_Especies_flavourtag.xlsx', index_col='label')
labelFlavor = labels.loc[:,'label3']
datos_porrito_sabores4 = datos_porrito_sabores.join(labels)
datos_porrito_sabores4.at['1024', 'label2'] = "Sativa"
datos_porrito_sabores4.at['1024', 'id'] = 1

network_pal = sns.husl_palette(len(labelFlavor.unique()), s=1)

lut = dict(zip(labelFlavor.unique(), network_pal))
row_colors = labelFlavor.map(lut)

g = sns.clustermap(datos_porrito_sabores, row_colors=row_colors)

for label in labelFlavor.unique():
    g.ax_col_dendrogram.bar(0, 0, color=lut[label],
                            label=label, linewidth=0)
g.ax_col_dendrogram.legend(loc="center", ncol=6)

g.cax.set_position([.15, .2, .03, .45])
g.savefig("clustermapSabores.png")

h = sns.clustermap(datos_porrito_effectos, row_colors=row_colors)
