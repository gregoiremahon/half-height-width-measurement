##importing dependencies 
import os 
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np


def proceed():
    # loading files 
    data = []

    for root, dirs, files in os.walk("FILES_DIR"):
        for name in files:
            M = pd.read_csv(os.path.join(root, name) ).values 
            data.append(M)
    data = np.array(data)
    
    times = data[0][:,0] ## vecteur temps
    
    ### calcul de la moyenne:
    moyenne = np.mean([data[i][:,1] for i in range(len(data))] , axis = 0)
    
    ### pour etre plus précis on utilise une fonction qui génère plus de données représentative de l'allure.
    def regression(a,fa,b,fb,n):
        # n is the number of points 
        pente = (fa-fb)/(a-b)
        intercept = (a*fb-b*fa)/(a-b)
        return ([pente*i + intercept  for i in np.linspace(a,b,n)], [i for i in np.linspace(a,b,n) ])
    
    times_list = []
    for i in range(len(moyenne)-1):
        times_list.append(regression(times[i], moyenne[i] , times[i+1], moyenne[i+1] , 100)[1])
    times_list = np.array(times_list).ravel()




    def regression_list(list_):
        points_=[]
        for i in range(len(list_)-1):
            points_.append(regression(times[i], list_[i] , times[i+1], list_[i+1] , 100)[0] )
        points_ = np.array(points_).ravel()
        return points_
    
    
    moyenne_list = regression_list(moyenne)
    
    
    ## calcul largeur à la mi-hauteur
    def larg_2_haut(list_):

        inter_value = max(list_) # la valeur maximale
        indx = np.argmax(list_)
        list1 , list2 = list_[:indx] , list_[indx:]
        value = inter_value/2
        index1 =0
        index2 = 0

        while list1[index1]<value:
            index1+=1


        while list2[index2]>value:
            index2+=1    
        index2 = index2 + indx


        return times_list [index2] - times_list[index1]
    
    ## liste des largeurs à mi-hauteur des différentes points
    
    list_moyenne_mi_hauteur = [larg_2_haut(regression_list(data[i][:,1])) for i in range(len(data))]
    
    moyenne = np.mean(list_moyenne_mi_hauteur) 
    médiane = np.median(list_moyenne_mi_hauteur) 
    écart_type = np.std(list_moyenne_mi_hauteur)
    print("La moyenne est de :", moyenne,"s")
    print("La médiane est de :", médiane,"s")
    print("L'écart type est de :", écart_type,"s")

proceed()


