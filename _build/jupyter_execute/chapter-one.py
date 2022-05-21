#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.DataFrame( {
    "length": [168.8, 168.8, 171.2, 176.6, 176.6, 177.3, 192.7, 192.7, 192.7],
    "width": [64.1, 64.1, 65.5, 66.2, 66.4, 66.3, 71.4, 71.4, 71.4],
    "height": [48.8, 48.8, 52.4, 54.3, 54.3, 53.1, 55.7, 55.7, 55.9],

})
df


# # Test GitHub Actions - Test two three four
# ## Importance of Data Normalization 
# 
# It will be interesting to see what happens without data normalizing.
# 
# 1. Simple Feature scaling
# 2. Min-Max
# 3. Z-score
# 

# ### Simple Feature Scaling 

# In[3]:


df["length"] = df["length"]/df["length"].max()
df


# ### Min-Max

# In[4]:


df["length"] = (df["length"]-df["length"].min())/(df["length"].max()-df["length"].min())
df


# ### Standard Deviation

# In[5]:


df["length"] = (df["length"]-df["length"].mean())/df["length"].std()
df

