# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 13:26:01 2021

@author: ilyur
"""

#%% import libraries

import pandas as pd

#%% import data

data = pd.read_csv("gender_classifier.csv",encoding = "latin1")

#%% specify which ones are will be used

data = pd.concat([data.gender,data.description],axis=1)
data.dropna(axis=0,inplace=True)

data.gender = [1 if each == "female" else 0 for each in data.gender]
#%% regular expression [^a-zA-z] ^ this means don't take the a-zA-Z interval

import re

first_description = data.description[4]

description = re.sub("[^a-zA-z]", " ", first_description) # search pattern,repl,input

#%% preprocessing
description = description.lower()

#%% stop words (irrevelant words)

import nltk
nltk.download("stopwords")

#%% tokenize
nltk.download('punkt') # i don't know now 
from nltk.corpus import stopwords

description = nltk.word_tokenize(description)

#%% let's discard irrelevant words
 
description = [word for word in description if not word in set(stopwords.words("english"))]

#%% lemmatization loved -> love

import nltk as nlp 
nltk.download('wordnet')

lemma = nlp.WordNetLemmatizer()
description = [lemma.lemmatize(word) for word in description]

description = " ".join(description)

#%% data cleaning methods all be using for our data

description_list = []

for description in data.description:
    description = re.sub("[^a-zA-z]", " ", description)
    description = description.lower()
    description = nltk.word_tokenize(description)
    lemma = nlp.WordNetLemmatizer()
    description = [lemma.lemmatize(word) for word in description]
    description = " ".join(description)
    description_list.append(description)

#%% bag of words

from sklearn.feature_extraction.text import CountVectorizer # bag of words
max_features = 500

count_vectorized = CountVectorizer(max_features=max_features,stop_words="english")

sparce_matrix = count_vectorized.fit_transform(description_list).toarray() # x

print("the most used {} words {} ".format(max_features,count_vectorized.get_feature_names()))
    
y = data.iloc[:,0].values.reshape(-1,1) # male or female    
x = sparce_matrix
#%% train test split

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.1, random_state = 42)

#%% naive bayes

from sklearn.naive_bayes import GaussianNB
nb = GaussianNB()
nb.fit(x_train,x_test)

#%% prediction
print("accuracy:",nb.score(x_test,y_test))