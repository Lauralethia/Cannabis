# -*- coding: utf-8 -*-
"""
Created on Thu May 23 12:53:43 2019

@author: Amelie
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 10:11:31 2019

@author: Amelie
"""

dir_to_files = '~Data\\'
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

exceldatos = dir_to_files + 'All.xlsx'
df_subj = pd.read_excel(exceldatos,header = 0,index_col=0,sheet_name="All")

g = sns.clustermap(df_subj, cmap="bwr", xticklabels=1, yticklabels=1)


df_subj = pd.read_excel(exceldatos,header = 0,index_col=0,sheet_name="Allmas")

g = sns.clustermap(df_subj, cmap="Reds", xticklabels=1, yticklabels=1)

df_subj = pd.read_excel(exceldatos,header = 0,index_col=0,sheet_name="Allmenos")

g = sns.clustermap(df_subj, cmap="Blues", xticklabels=1, yticklabels=1)

df_subj = pd.read_excel(exceldatos,header = 0,index_col=0,sheet_name="Adj")

g = sns.clustermap(df_subj, cmap="jet", xticklabels=1, yticklabels=1,vmin=-0.5, vmax=0.5)

df_subj = pd.read_excel(exceldatos,header = 0,index_col=0,sheet_name="Admas")

g = sns.clustermap(df_subj, cmap="Reds", xticklabels=1, yticklabels=1)

df_subj = pd.read_excel(exceldatos,header = 0,index_col=0,sheet_name="Admenos")

g = sns.clustermap(df_subj, cmap="Blues", xticklabels=1, yticklabels=1)

