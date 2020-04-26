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
JkDPh = "~/Data/rating_thc_Jikomesetal.csv"

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


formmethod = ['Flower', 'Concentrated', 'Smoke', 'Vaporize']

effects = ['Aroused', 'Creative', 'Energetic', 'Euphoric', 'Focused', 'Giggly', 'Happy', 'Hungry', 'Relaxed', 'Sleepy', 'Talkative', 'Tingly', 'Uplifted', 'Anxious', 'Dizzy', 'Dry Eyes', 'Dry Mouth', 'Headache', 'Paranoid']

symptoms = ['Cramps', 'Depression', 'Eye Pressure', 'Fatigue', 'Headaches', 'Inflammation' , 'Insomnia', 'Lack of Appetite' , 'Muscle Spasms', 'Nausea', 'Pain', 'Seizures', 'Spasticity', 'Stress']

conditions = ["ADD/ADHD", "Alzheimer's", "Anorexia", "Anxiety", "Arthritis", "Asthma", "Bipolar Disorder", "Cachexia", "Cancer", "Crohn's Disease", "Epilepsy", "Fibromyalgia", "Gastrointestinal Disorder", "Glaucoma", "HIV/AIDS", "Hypertension", "Migraines", "Multiple Sclerosis", "Muscular Dystrophy", "Parkinson's", "Phantom Limb Pain",  "PMS", "PTSD", "Spinal Cord Injury", "Tinnitus", "Tourette's Syndrome"]

flavors = ['Ammonia', 'Apple', 'Apricot', 'Berry', 'Blue Cheese', 'Blueberry', 'Butter', 'Cheese', 'Chemical', 'Chestnut', 'Citrus', 'Coffee', 'Diesel', 'Earthy', 'Flowery', 'Grape', 'Grapefruit', 'Honey', 'Lavender', 'Lemon', 'Lime', 'Mango', 'Menthol', 'Mint', 'Nutty', 'Orange', 'Peach', 'Pear', 'Pepper', 'Pine', 'Pineapple', 'Plum', 'Pungent', 'Rose', 'Sage', 'Skunk', 'Spicy/Herbal', 'Strawberry', 'Sweet', 'Tar', 'Tea', 'Tobacco', 'Tree', 'Fruit', 'Tropical', 'Vanilla', 'Violet', 'Woody']

effects = effects + symptoms + conditions

tabladatos_ef =  np.zeros((len(strains),len(effects)))
tabladatos_fl =  np.zeros((len(strains),len(flavors)))

categorias_st = []
categorias_ca = []
categorias_nreps = []

for s in range(0,len(strains)):
    
    data = pickle.load( open(str( strainsDPh+strains[s]), "rb" ) )
    
    categorias_st.append(data["strain"])
    categorias_ca.append(data["categorias"][0])

    TablaEffects = np.zeros(len(effects))
    TablaFlavor = np.zeros(len(flavors))  
    resef = 0
    resfl = 0
    categorias_nreps.append(len(data["data_strain"]))

    if len(data["data_strain"])>0:
        for n in range(0,len(data["data_strain"])):
            ef = []
            fl = []
            ef = data["data_strain"][n]["efectos"]
            if not ef:
                resef += 1
            fl = data["data_strain"][n]["sabores"]
            if not fl:
                resfl += 1
            indx = 0
            jndx = 0
            for i in effects:
                
                if i in ef:
                    TablaEffects[indx] += 1
                indx += 1
                    
            for j in flavors:
                
                if j in fl:
                    TablaFlavor[jndx] += 1
                jndx += 1
        divef = (len(data["data_strain"])-resef)
        if divef:
            tabladatos_ef[s] = TablaEffects/divef
               
        divst = (len(data["data_strain"])-resfl)
        if divst:
            tabladatos_fl[s] = TablaFlavor/divst
        
        
df1 = pd.DataFrame(tabladatos_ef, columns=effects)
df2 = pd.DataFrame(tabladatos_fl, columns=flavors)

datain = list(zip(categorias_st,categorias_ca,categorias_nreps))
df3 = pd.DataFrame(data = datain,columns = ['straine','categoria','nreportes'])

df_porro = pd.concat([df1, df2,df3], axis=1)

#df_porro.to_csv('dfporro.txt', sep='\t', index=False)

df_porro.set_index('straine',inplace=True)

df_thc = df = pd.read_csv(JkDPh, delimiter=';')
df_thc.set_index('LeaflyStrain',inplace=True)

df_thccbd = df_thc[df_thc.columns[:4]]

datos_porro = pd.merge(df_porro,df_thccbd,'left',left_index=True, right_index=True)
datos_porro.head()
datos_porro_f = datos_porro[datos_porro["nreportes"]>10]
logicvector = datos_porro["nreportes"]>10
#logicvector.to_csv('logicvector.txt', sep='\t', index=False)

datos_porrito_effectos = datos_porro_f.loc[:, :'Paranoid']
datos_porrito_sabores = datos_porro_f.loc[:, 'Ammonia':'THCmax_std']
datos_porrito_sabores = datos_porrito_sabores.loc[:, :'Woody']

#datos_porrito_effectos.to_pickle("./datos_porrito_effectos.pkl")
#datos_porrito_sabores.to_pickle("./datos_porrito_sabores.pkl")

datos_porrito = pd.concat([datos_porrito_effectos,datos_porrito_sabores], axis=1)

#datos_porrito_effectos = pd.concat([datos_porrito_effectos,datos_porrito_sabores.loc[:, 'nreportes':'THCmax_std']], axis=1)

datos_porrito['strians'] = datos_porrito.index
#datos_porrito.to_csv('datos_porrito.txt', sep='\t', index=False)


corr_ef = datos_porrito_effectos.corr()
sns.heatmap(corr_ef,  
            xticklabels=corr_ef.columns.values,
            yticklabels=corr_ef.columns.values)

transefectstrice =datos_porrito_effectos.transpose()
corr_stideef = transefectstrice.corr()
sns.heatmap(corr_stideef,  
            xticklabels=corr_stideef.columns.values,
            yticklabels=corr_stideef.columns.values)

corr_sabor = datos_porrito_sabores.corr()
sns.heatmap(corr_sabor,  
            xticklabels=corr_sabor.columns.values,
            yticklabels=corr_sabor.columns.values)

transsaborstrice =datos_porrito_sabores.transpose()
#transsaborstrice = transsaborstrice.loc[:, 'woody':'THCmax_std']
corr_stidesab = transsaborstrice.corr()
sns.heatmap(corr_stidesab,  
            xticklabels=corr_stidesab.columns.values,
            yticklabels=corr_stidesab.columns.values)


# Para sride efectos
X = transefectstrice.corr().values
d = sch.distance.pdist(X)   # vector of ('55' choose 2) pairwise distances
L = sch.linkage(d, method='complete')
ind = sch.fcluster(L, 0.5*d.max(), 'distance')
columns = [transefectstrice.columns.tolist()[i] for i in list((np.argsort(ind)))]
df = transefectstrice.reindex_axis(columns, axis=1)
#%matplotlib qt5
plot_corr(df, size=18)

# Para sride sabores
X = transsaborstrice.corr().values
d = sch.distance.pdist(X)   # vector of ('55' choose 2) pairwise distances
L = sch.linkage(d, method='complete')
ind = sch.fcluster(L, 0.5*d.max(), 'distance')
columns = [transsaborstrice.columns.tolist()[i] for i in list((np.argsort(ind)))]
df = transsaborstrice.reindex(columns, axis=1)

#%matplotlib qt5
plot_corr(df, size=18)

# Para efectos
X = datos_porrito_effectos.corr().values
d = sch.distance.pdist(X)   # vector of ('55' choose 2) pairwise distances
L = sch.linkage(d, method='complete')
ind = sch.fcluster(L, 0.5*d.max(), 'distance')
columns = [datos_porrito_effectos.columns.tolist()[i] for i in list((np.argsort(ind)))]
df = datos_porrito_effectos.reindex(columns, axis=1)
sns.clustermap(datos_porrito_effectos)

#%matplotlib qt5
plot_corr(df, size=18)

# Para sabores
X = datos_porrito_sabores.corr().values
d = sch.distance.pdist(X)   # vector of ('55' choose 2) pairwise distances
L = sch.linkage(d, method='complete')
ind = sch.fcluster(L, 0.5*d.max(), 'distance')
columns = [datos_porrito_sabores.columns.tolist()[i] for i in list((np.argsort(ind)))]
df = datos_porrito_sabores.reindex(columns, axis=1)
sns.clustermap(datos_porrito_sabores)

#%matplotlib qt5
plot_corr(df, size=18)

# Analisis teniendo en cuenta los valores de THC y CBD
datos_porrito_effectos_alcaloides = datos_porro_f.loc[:, :'Paranoid']
datos_porrito_sabores_alcaloides = datos_porro_f.loc[:, 'Ammonia':'THCmax_std']

datos_porrito_effectos_alcaloides = pd.concat([datos_porrito_effectos_alcaloides,datos_porrito_sabores_alcaloides.loc[:, 'categoria':'THCmax_std']], axis=1)

#datos_porrito_effectos_alcaloides.to_pickle("./ddatos_porrito_effectos_alcaloides.pkl")
#datos_porrito_sabores_alcaloides.to_pickle("./datos_porrito_sabores_alcaloides.pkl")

