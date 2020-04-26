import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os, sys
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="ticks", color_codes=True)

strainsDPh = "~/Data/strains/"

strains=   os.listdir(strainsDPh)  
lista_filtro_0 = pd.read_csv("~Data/filter_words.txt")


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
reportes = [None]*len(strains)
 
for s in range(0,len(strains)):
    
    data = pickle.load(open((strainsDPh + strains[s]), "rb" ) )
    
    categorias_st.append(data["strain"])
    categorias_ca.append(data["categorias"])

    TablaEffects = np.zeros(len(effects))
    TablaFlavor = np.zeros(len(flavors))  
    
    resef = 0
    resfl = 0
    categorias_nreps.append(len(data["data_strain"]))

    if len(data["data_strain"])>0:
        reportes[s] = '.' 
        for n in range(0,len(data["data_strain"])):
            ef = []
            fl = []
            reportes[s]=str(reportes[s] + data["data_strain"][n]["reporte"])
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
            
Nreps=np.asarray(categorias_nreps)
Nreps2=np.where(Nreps>10)

repo = pd.DataFrame(reportes)
repo2 = repo.iloc[Nreps2] 

reportes2 = repo2[0].tolist()
#logicvector = reports["nreportes"]>10
#logicvector.to_csv('logicvector.txt', sep='\t', index=False)
selected =pd.DataFrame(strains).iloc[Nreps2][0].tolist() 
cat_selected =pd.DataFrame(categorias_ca).iloc[Nreps2][0].tolist() 
nresp_selected =pd.DataFrame(categorias_nreps).iloc[Nreps2][0].tolist() 

                                             
leaflysave1 = {'reports': reportes2, 'Effects_norm': tabladatos_ef[Nreps2,:], 'Flav_norm': tabladatos_fl[Nreps2,:], 'Effects_count': TablaEffects, 'Flavor_count': TablaFlavor, 'Strain': selected, 'categoria': cat_selected, 'N': nresp_selected}

#pickle.dump(leaflysave1,  open('.../DataReports.p', 'wb') )

        
