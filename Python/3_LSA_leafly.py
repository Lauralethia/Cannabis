# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

import pickle
import matplotlib.pyplot as plt


data = pickle.load( open( ".../PrePro_df.p", "rb" ) )
strain = list(data['strain'])   # droga - strain
#raices = list(' '.join(data['raices']))   # raices - palabras
roots = list(data['raices']) 
roots2=[None]*len(data['raices'])
zz=-1
for s in range(0,len(roots)):
    
    if not(roots[s] is None):
        zz=zz+1
        roots2[zz]=roots[s]
        
vectorizer = TfidfVectorizer(ngram_range=(1, 1), min_df=0.05, max_df=0.95)

X = vectorizer.fit_transform(roots2).toarray()

feature_names = vectorizer.get_feature_names()
thefile = open('vocabulario_leaflt_a_guardar.txt', 'w')
thefile.write("\n".join(feature_names))

leafly3 = {'words': feature_names}

pickle.dump(leafly3,  open('.../terms.p', 'wb') )        
feature_names2 = pd.DataFrame(feature_names)
#feature_names2.to_csv('..../Vocabulario_leafly_....txt')           



                        
### aplica SVD para tener LSA

dimension = np.arange(10,150)  ### elegi el rango de dimensiones / valores singulares retenidos

for nd in dimension:

    print(nd)
    
    freq_matrix =  np.transpose(X)       
    U, s, V = np.linalg.svd(freq_matrix, full_matrices=True)        
    Ubis = U[:,0:nd]     
    Vbis = V[0:nd, :]
    S = np.zeros((nd, nd))
    S[:nd, :nd] = np.diag(s[0:nd])
    freq_low_rank = np.dot(Ubis, np.dot(S, Vbis))
    correlacion = np.corrcoef(np.transpose(freq_low_rank))

    np.savetxt(".../tf_idf_freq_low_rank_nd_"+str(nd)+".csv", freq_low_rank,delimiter=',')
    
    np.savetxt(".../tf_idf_correlacion_nd_"+str(nd)+".csv", correlacion,delimiter=',')

