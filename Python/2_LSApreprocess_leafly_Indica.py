# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import requests
import re
import nltk
import pickle
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer=WordNetLemmatizer()
from nltk.corpus import wordnet
from nltk.corpus import stopwords
# from __future__ import division
import nltk, re, pprint

strainsDPh = "~/Data/strains/"
ExDfInd = "~/Data/Indica.p"

lista_filtro_0 = pd.read_csv("~/Data/filter_words.txt")

lista_filtro = lista_filtro_0["Palabras"].tolist()

data = pickle.load(open((ExDfInd), "rb" ) )
strains = list(data['Strain'])
tokens = []
roots=[None]*len(data['reports'])
reportes = list(data['reports'])
z = -1
for s in range(0,len(reportes)):
    
    if not(reportes[s] is None):
        z = z+1
        print(s)
        
    #def cleanhtml(raw_html):
    #cleanr = re.compile('<.*?>')
    #cleantext = re.sub(cleanr, '', raw_html)
    #return cleantext
        
        # reports --> el conjunto de reportes por strain (string largo con la suma de todos los reportes de un strain)
        
        
        reportes[s] = reportes[s].replace('\n', '').replace('\t', '')
        
        reportes[s] = re.sub('\W+',' ', reportes[s])            # remueve \*
        
        reportes[s] = re.sub(r'\d+', '', reportes[s]).lower()   # remueve puntuacion
        
        reportes[s] = reportes[s].split(' ')
        
        
        
        
        i=0
        j=0
        
      
        
        i=i+1
            
            #### remover stopwords 
        filtered_words_0 = [word for word in reportes[s] if word not in stopwords.words('english')]
        filtered_words = [word for word in filtered_words_0 if word not in lista_filtro]
      
            ### chequear solo agregar palabras que tengan que sean ingles
            
        for word in filtered_words:
            root_individual = " "
            if j == 0:
                roots[z]= " "
            j = j+1
            if wordnet.synsets(word):
         #       print('ok')
            
                tokens=word_tokenize(word)
                tipo=nltk.pos_tag(tokens) #clasifica que tipo de palabra es
                if len(tipo) > 0:
                    for m in np.arange(0,len(tipo)): #traduce los tag al tag usado en lemmatize
                        if tipo[m][1][0]=='V':
                            tag='v'
                        elif tipo[m][1][0]=='J':
                            tag='a'
                        elif tipo[m][1][0]=='R' and tipo[m][1][1]=='B':
                            tag='r'
                        else:
                            tag='n'
                        
                    #roots[s].append(wordnet_lemmatizer.lemmatize(tipo[m][0],pos=tag))
                    root_individual=str(root_individual + wordnet_lemmatizer.lemmatize(tipo[m][0],pos=tag)+ " " )
                    
                    guardar = {'StrainRoot': root_individual}
                  #  pickle.dump(guardar,  open( "C:/Leafly\LSA\Preprocesado/"+strains[s], "wb") )        

                    
                    roots[z]=str(roots[z] + wordnet_lemmatizer.lemmatize(tipo[m][0],pos=tag)+ " " )
                
        
leafly2 = {'raices': roots, 'data_anterior': data, 'strain': strains}

#pickle.dump(leafly2,  open('.../PrePro_Indica.p', 'wb') )        
            
