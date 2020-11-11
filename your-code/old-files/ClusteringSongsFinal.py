#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os


# In[2]:


os.chdir("C:\\Users\\GiantsV3\\Documents\\Ironhack\\Week3\\Project-Week-3-Song-Recommender")


# In[3]:


playlist = pd.read_csv("data/complete_playlist.csv", index_col=0)
playlist.drop(labels=["Song", "Artist"], axis=1, inplace=True)


# In[5]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
playlist_scaled = scaler.fit_transform(playlist)
pd.DataFrame(playlist_scaled)


# In[10]:


from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=7)


# In[11]:


kmeans.fit(playlist_scaled)


# In[12]:


clusters = kmeans.predict(playlist_scaled)


# In[15]:


clusters


# In[17]:


pd.Series(clusters).value_counts()


# In[18]:


playlist["Cluster"] = clusters


# In[19]:


playlist.groupby(by="Cluster").mean()

