#!/usr/bin/env python
# coding: utf-8

# ## Rename

# In[1]:


import pandas as pd


# In[2]:


df.rename(columns={”city_mpg”: “city-L/100km”}, inplace=True)

