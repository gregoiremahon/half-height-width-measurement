#!/usr/bin/env python
# coding: utf-8

# In[1]:


##importing dependencies 
import os 
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np


# In[4]:


os.chdir("C:/Users/gregm/OneDrive/iUMTEK/Mesures laser/Mesures shutter/Traces")   # path to the files 


# In[5]:


# loading files 
data = []
 
for root, dirs, files in os.walk("C:/Users/gregm/OneDrive/iUMTEK/Mesures laser/Mesures shutter/Traces"):
    for name in files:
        print(os.path.join(root, name))
        M = pd.read_csv(os.path.join(root, name) ).values 
        data.append(M)
data = np.array(data)


# In[10]:


plt.figure(figsize = (15,15))
for i in range(len(data)):
    plt.subplot(len(data)//4+1, 4,i+1)
    plt.plot(data[0][:,0], data[i][:,1])
    plt.xlim(min(data[0][:,0]), max(data[0][:,0]))
    plt.ylim(min(data[i][:,1]) , max(data[i][:,1]))


# In[11]:


### pour etre plus précis on utilise une fonction qui génère plus de données représentative de l'allure.
def regression(a,fa,b,fb,n):
    # n is the number of points 
    pente = (fa-fb)/(a-b)
    intercept = (a*fb-b*fa)/(a-b)
    return ([pente*i + intercept  for i in np.linspace(a,b,n)], [i for i in np.linspace(a,b,n) ])


# In[12]:


### calcul de la moyenne:
moyenne = np.mean([data[i][:,1] for i in range(len(data))] , axis = 0)


# In[13]:


times = data[0][:,0] ## vecteur temps 

# génération de plus de données représentatives de l'allure (100 points générés entre 2 points consécutifs de l'allure)

points_moyenne =[]
timess = []
for i in range(len(moyenne)-1):
    points_moyenne.append(regression(times[i], moyenne[i] , times[i+1], moyenne[i+1] , 100)[0] )
    timess.append(regression(times[i], moyenne[i] , times[i+1], moyenne[i+1] , 100)[1])
points_moyenne = np.array(points_moyenne).ravel()
timess = np.array(timess).ravel()


# In[22]:


## calcul largeur à la mi-hauteur
def larg_2_haut(list_):
    
    inter_value = max(list_) # la valeur maximale
    min_val =  min(list_)
    value = inter_value - min_val
    indx = np.argmax(list_)
    list1 , list2 = list_[:indx] , list_[indx:]
    value = value/2
    index1 =0
    index2 = 0
    
    while list1[index1]<value:
        index1+=1
        
        
    while list2[index2]>value:
        index2+=1    
    index2 = index2 + indx
    
    
    return timess [index2] - timess[index1]
        
        
    


# In[23]:


##visualisation de la résultats
def larg_2_haut_viz(list_):
    
    inter_value = max(list_) # la valeur maximale
    min_val =  min(list_)
    value = inter_value - min_val
    indx = np.argmax(list_)
    list1 , list2 = list_[:indx] , list_[indx:]
    value = value/2
    index1 =0
    index2 = 0
    
    while list1[index1]<value:
        index1+=1
        
        
    while list2[index2]>value:
        index2+=1    
    index2 = index2 + indx
    
    
    plt.scatter(timess , points_moyenne)
    plt.plot(timess[index1:index2] , [value]*len(timess[index1:index2]) , color = "r")
    return timess [index2] - timess[index1]
        


# In[24]:


larg_2_haut_viz(points_moyenne)


# In[25]:


print(max(points_moyenne))


# In[26]:


print(min(points_moyenne))


# In[ ]:




