import pandas as pd
import numpy as np
import requests
import re
from random import randint
from time import sleep
import pickle



def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext
  
def whichinlist(inputstring, inputlist):
    output = []
    for i in inputlist:
        if i in inputstring:
            output.append(i)
    return output
        
  
  
df = pd.read_csv('/Users/mac/Documents/leafly/strains_data.csv')

strains = []
data = []
multiple_category = []
exceptions = []
review_strain = []
categoria_strain = []

formmethod = ['Flower', 'Concentrated', 'Smoke', 'Vaporize']

effects = ['Aroused', 'Creative', 'Energetic', 'Euphoric', 'Focused', 'Giggly', 'Happy', 'Hungry', 'Relaxed', 'Sleepy', 'Talkative', 'Tingly', 'Uplifted', 'Anxious', 'Dizzy', 'Dry Eyes', 'Dry Mouth', 'Headache', 'Paranoid']

symptoms = ['Cramps', 'Depression', 'Eye Pressure', 'Fatigue', 'Headaches', 'Inflammation' , 'Insomnia', 'Lack of Appetite' , 'Muscle Spasms', 'Nausea', 'Pain', 'Seizures', 'Spasticity', 'Stress']

conditions = ["ADD/ADHD", "Alzheimer's", "Anorexia", "Anxiety", "Arthritis", "Asthma", "Bipolar Disorder", "Cachexia", "Cancer", "Crohn's Disease", "Epilepsy", "Fibromyalgia", "Gastrointestinal Disorder", "Glaucoma", "HIV/AIDS", "Hypertension", "Migraines", "Multiple Sclerosis", "Muscular Dystrophy", "Parkinson's", "Phantom Limb Pain",  "PMS", "PTSD", "Spinal Cord Injury", "Tinnitus", "Tourette's Syndrome"]

flavors = ['Ammonia', 'Apple', 'Apricot', 'Berry', 'Blue Cheese', 'Blueberry', 'Butter', 'Cheese', 'Chemical', 'Chestnut', 'Citrus', 'Coffee', 'Diesel', 'Earthy', 'Flowery', 'Grape', 'Grapefruit', 'Honey', 'Lavender', 'Lemon', 'Lime', 'Mango', 'Menthol', 'Mint', 'Nutty', 'Orange', 'Peach', 'Pear', 'Pepper', 'Pine', 'Pineapple', 'Plum', 'Pungent', 'Rose', 'Sage', 'Skunk', 'Spicy/Herbal', 'Strawberry', 'Sweet', 'Tar', 'Tea', 'Tobacco', 'Tree', 'Fruit', 'Tropical', 'Vanilla', 'Violet', 'Woody']

effects = effects + symptoms + conditions

# iterar por strain

errores = []


for strain in df['LeaflyStrain'].unique():
    
    
    
    
    strains.append(strain)
    
    print(strain)
    
    
    # encontrar categoria de strain
    
    categorias = df['Category'][ df['LeaflyStrain'] == strain].unique()
    
    if len(categorias)>1:
        multiple_category.append('si')
    if len(categorias)==1:
        multiple_category.append('no')
        
    categoria = categorias[0]
    
    pagnum = 1
    
    categoria_strain.append(categoria)
    

    data_strain = []
    
    
    try:

        while 'Read Full Review' in requests.get('https://www.leafly.com/'+categoria+'/'+strain+'/reviews?page='+str(pagnum)+'&sort=rating').text:
        
            print(pagnum)
        
            scrap_url = 'https://www.leafly.com/'+categoria.lower()+'/'+strain+'/reviews?page='+str(pagnum)+'&sort=rating'
    
            pagnum = pagnum + 1
            r = requests.get(scrap_url) 
            sleep(randint(0,2))
    
            codigo =  r.text
            
            # primer corte
            
            split1 = codigo.split('<a href="/'+categoria.lower()+'/'+strain+'/reviews/')
        
            for s in split1[1:]:
                
                reviewid = s.split('" class')[0]
                
                review_url = 'https://www.leafly.com/'+categoria.lower()+'/'+strain+'/reviews/' + reviewid
                
                r2 = requests.get(review_url) 
                sleep(randint(0,2))
    
                review = r2.text
                
                name = review.split('[ reviewer-info reviewer-name]">')[1].split('</div>')[0]
                texto = review.split('<div class="copy--md copy-md--xl padding-rowItem--xl notranslate">')[1].split('</div>')[0]
                metodos = whichinlist(review.split('Form &amp; Method')[1].split('<div class="divider bottom padding-listItem">\r\n')[0],formmethod)
                efectos = whichinlist(review.split('Effects')[1].split('<div class="divider bottom padding-listItem">\r\n')[0],effects)
                sabores = whichinlist(review.split('Flavor Profile')[1].split('</ul>\r\n')[0],flavors)
                
                print(name)
        
                thisdict = {"usuario": name, "reporte": texto, "efectos": efectos, "sabores": sabores}
                data_strain.append(thisdict)
                
        review_strain.append(data_strain)
        
        data2save = {"strain": strain, "data_strain": data_strain, "categorias": categorias}
        
        pickle.dump( data2save ,open( ".../strains/"+strain+".p", "wb"))
        
    except Exception as ex:
        
        print(ex)
        errores.append( (strain,ex) )
         
        
datafinal =  {"strains": strains, "review_strain": review_strain, "exceptions ": exceptions , "categoria_strain": categoria_strain, "multiple_category":multiple_category}
#pickle.dump( datafinal ,open( ".../todos_strains.p", "wb"))
  