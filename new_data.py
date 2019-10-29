# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 10:27:49 2019

@author: ea027_0c3qbph
"""
'''
Data preparation
'''
import pandas as pd
data_dir = "D:/DMLAB/DM19-Lab1/DM19-Lab1-Homework1/sentiment labelled sentences/sentiment labelled sentences/"

f=open(data_dir + 'amazon_cells_labelled.txt', "r")
amazon =f.readlines()
f.close()

f=open(data_dir + 'imdb_labelled.txt', "r", encoding="utf-8")
imbd =f.readlines()
f.close()

f=open(data_dir + 'yelp_labelled.txt', "r")
yelp =f.readlines()
f.close()


def prepare(data):
    sentence = []
    sentiment = []
    for d in data:
        sentiment.append(d.split()[-1])
        sentence.append(d[0:-3])
    return sentence, sentiment

df_ama = pd.DataFrame()
df_im  = pd.DataFrame()
df_yelp = pd.DataFrame()

df_ama['sentence'], df_ama['sentiment'] = prepare(amazon)   
df_im['sentence'], df_im['sentiment'] = prepare(imbd)    
df_yelp['sentence'], df_yelp['sentiment'] = prepare(yelp)
import numpy as np
len(np.where(df_ama.sentiment=='0')[0])           

#import re
## define a function that cleans the data
## input : a = list(df_ama['sentence'])
#def clean_data(a):
#    for i in range(len(a)):
#        a[i].replace("-", " ")
#        a[i].replace("_", " ")
#        a[i] = re.sub(r'[^\w\s\r]',' ',a[i])
#    return a
#df_ama.sentence = clean_data(df_ama.sentence)
#df_im.sentence = clean_data(df_im.sentence)
#df_yelp.sentence = clean_data(df_yelp.sentence)
#print(df_ama.sentence[0:5])

#import matplotlib.pyplot as plt
#%matplotlib inline
#col = ['coral', 'blue']
#categories = ['0','1']
#def plot_2d(col, categories, X_reduced, X):
#    fig = plt.figure(figsize = (25,10))
#    ax = fig.subplots()
#    for c, category in zip(col, categories):
#        xs = X_reduced[X['sentiment'] == category].T[0]
#        ys = X_reduced[X['sentiment'] == category].T[1]   
#        ax.scatter(xs, ys, c = c, marker='o')
#    ax.grid(color='gray', linestyle=':', linewidth=2, alpha=0.2)
#    ax.set_xlabel('\nX Label')
#    ax.set_ylabel('\nY Label')
#    plt.show()
#plot_2d(col, categories, ama_reduced, df_ama)
#plot_2d(col, categories, im_reduced, df_im)
#plot_2d(col, categories, yelp_reduced, df_yelp)

def to_lower(df):
    all_positive = list(df.sentence[np.where(df.sentiment=='1')[0]])
    all_negative = list(df.sentence[np.where(df.sentiment=='0')[0]])
    for i in range(len(all_positive)):
        all_positive[i] = all_positive[i].lower()
    for i in range(len(all_negative)):
        all_negative[i] = all_negative[i].lower()
    return all_positive, all_negative
    
all_p_ama, all_n_ama = to_lower(df_ama)