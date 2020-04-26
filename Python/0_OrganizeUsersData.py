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

strainsDPh = "~/Data/strains/"

def plot_corr(df,size=10):
    '''Plot a graphical correlation matrix for a dataframe.

    Input:
        df: pandas DataFrame
        size: vertical and horizontal size of the plot'''
    
#    %matplotlib inline
#    import matplotlib.pyplot as plt

    # Compute the correlation matrix for the received dataframe
    corr = df.corr()
    
    # Plot the correlation matrix
    fig, ax = plt.subplots(figsize=(size, size))
    cax = ax.matshow(corr, cmap='RdYlGn')
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90);
    plt.yticks(range(len(corr.columns)), corr.columns);
    
    # Add the colorbar legend
    cbar = fig.colorbar(cax, ticks=[-1, 0, 1], aspect=40, shrink=.8)

sns.set(style="ticks", color_codes=True)
strains=   os.listdir(strainsDPh)  

#data = pd.read_csv("C:/Users/Amelie/Documents/Cursos/3Datosconpython/Clase3/Parte2/breast-cancer.csv")# here header 0 means the 0 th row is our coloumn 

formmethod = ['Flower', 'Concentrated', 'Smoke', 'Vaporize']

categorias_st = []
categorias_ca = []
tabladatos_us =  []

categorias_nreps = []

for s in range(0,len(strains)):
    
    data = pickle.load( open(str( strainsDPh+strains[s]), "rb" ) )
    
    if len(data["data_strain"])>10:
        
        for n in range(0,len(data["data_strain"])):
            us = []
            us = data["data_strain"][n]["usuario"]
            tabladatos_us.append(us)
            categorias_st.append(data["strain"])
            categorias_ca.append(data["categorias"][0])
            categorias_nreps.append(len(data["data_strain"]))
            
 
d = { 'strain': pd.Series(categorias_st),
      'specie': pd.Series(categorias_ca),
      'nreps': pd.Series(categorias_nreps),
      'user': pd.Series(tabladatos_us)
     }       
dusers = pd.DataFrame(d)

#dusers.to_csv('dusers.txt', sep='\t', index=False)

