# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 11:15:09 2021

@author: ilyur
"""

# import data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# create data

#class1

x1 = np.random.normal(25,5,1000)
y1 = np.random.normal(25,5,1000)

#class2

x2 = np.random.normal(55,5,1000)
y2 = np.random.normal(60,5,1000)

#class3

x3 = np.random.normal(55,5,1000)
y3 = np.random.normal(15,5,1000)

#%%
x = np.concatenate((x1,x2,x3), axis=0)
y = np.concatenate((y1,y2,y3), axis=0)

#%% create dataframe

dictionary = {"x":x,"y":y}

data = pd.DataFrame(dictionary)

#%% visualize data

plt.scatter(x1,y1)
plt.scatter(x2,y2)
plt.scatter(x3,y3)
plt.show()

#Kmeans algorithm will see our data with no classes(it means that all color will be black)
#%% Kmeans

from sklearn.cluster import KMeans
wcss = []

for k in range(1,15):
    kmeans = KMeans(n_clusters = k)
    kmeans.fit(data)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1,15),wcss)
plt.xlabel("number of k value:")
plt.ylabel("wcss")
plt.show()
#%% for k = 3 

kmeans2 = KMeans(n_clusters = 3)
clusters = kmeans2.fit_predict(data)

data["label"] = clusters

plt.scatter(data.x[data.label == 0],data.y[data.label == 0],color ="red" )
plt.scatter(data.x[data.label == 1],data.y[data.label == 1],color ="green" )
plt.scatter(data.x[data.label == 2],data.y[data.label == 2],color ="blue" )
plt.show()
