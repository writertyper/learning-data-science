#!/usr/bin/env python
# coding: utf-8

# ## Data Normalizing

# 
# Descriptive Statistics
# GroupBy
# Correlation
# Correlation - Statistics

# In[1]:


import pandas as pd


# You can summarize the categorical data by using the value_counts() method

# In[ ]:





# In[2]:


import altair as alt
from vega_datasets import data

source = data.cars()

alt.Chart(source).mark_circle(size=60).encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
    tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
).interactive()


# In[3]:


alt.Chart(source).mark_circle(size=60).encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
    tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
)


# In[ ]:





# ## Data Normalizing
# import pandas as pd
# df = pd.DataFrame( {
#     "length": [168.8, 168.8, 171.2, 176.6, 176.6, 177.3, 192.7, 192.7, 192.7],
#     "width": [64.1, 64.1, 65.5, 66.2, 66.4, 66.3, 71.4, 71.4, 71.4],
#     "height": [48.8, 48.8, 52.4, 54.3, 54.3, 53.1, 55.7, 55.7, 55.9],
# 
# })
# df
# 
# ## Importance of Data Normalization
# 
# It will be interesting to see what happens without data normalizing.
# 
# 1. Simple Feature scaling
# 2. Min-Max
# 3. Z-score
# 
# ### Simple Feature Scaling 
# 
# x new = x old / x max
# 
# 
# 
# df["length"] = df["length"]/df["length"].max()
# df
# ### Min-Max
# 
# x new = xold - x min / x max - x min
# 
# df["length"] = (df["length"]-df["length"].min())/(df["length"].max()-df["length"].min())
# df
# ### Standard Deviation
# 
# x new = x old - mu / sigma
# 
# df["length"] = (df["length"]-df["length"].mean())/df["length"].std()
# df
# A gas
# B diesel
# C gas
# D gas
# 
# 
# 
# df = pd.DataFrame( {
#     "fuel": ["gas", "diesel", "gas", "gas"],
# })
# df
# pd.get_dummies(df['fuel'])
# 
# height: 170, 180, 170
# income: 100000, 20000, 50000
# 
# height and income are in different ranges, and it may be hard to compare.
# Without normalization, income will influence the result more. 
# 
# 
# 
# sepalLength	sepalWidth	petalLength	petalWidth	species
# 0	5.1	3.5	1.4	0.2	setosa
# 1	4.9	3.0	1.4	0.2	setosa
# 2	4.7	3.2	1.3	0.2	setosa
# 3	4.6	3.1	1.5	0.2	setosa
# 4	5.0	3.6	1.4	0.2	setosa
# Name	Miles_per_Gallon	Cylinders	Displacement	Horsepower	Weight_in_lbs	Acceleration	Year	Origin
# 0	chevrolet chevelle malibu	18.0	8	307.0	130.0	3504	12.0	1970-01-01	USA
# 1	buick skylark 320	15.0	8	350.0	165.0	3693	11.5	1970-01-01	USA
# 2	plymouth satellite	18.0	8	318.0	150.0	3436	11.0	1970-01-01	USA
# 3	amc rebel sst	16.0	8	304.0	150.0	3433	12.0	1970-01-01	USA
# 4	ford torino	17.0	8	302.0	140.0	3449	10.5	1970-01-01	USA
# ...	...	...	...	...	...	...	...	...	...
# 401	ford mustang gl	27.0	4	140.0	86.0	2790	15.6	1982-01-01	USA
# 402	vw pickup	44.0	4	97.0	52.0	2130	24.6	1982-01-01	Europe
# 403	dodge rampage	32.0	4	135.0	84.0	2295	11.6	1982-01-01	USA
# 404	ford ranger	28.0	4	120.0	79.0	2625	18.6	1982-01-01	USA
# 405	chevy s-10	31.0	4	119.0	82.0	2720	19.4	1982-01-01	USA
# 406 rows × 9 columns
# 
# Index(['Name', 'Miles_per_Gallon', 'Cylinders', 'Displacement', 'Horsepower',
#        'Weight_in_lbs', 'Acceleration', 'Year', 'Origin'],
#       dtype='object')
# Miles_per_Gallon	Cylinders	Displacement
# 0	9.0	8	304.00
# 1	10.0	8	333.50
# 2	11.0	8	374.25
# 3	12.0	8	394.50
# 4	13.0	8	353.00
# ...	...	...	...
# 154	43.4	4	90.00
# 155	44.0	4	97.00
# 156	44.3	4	90.00
# 157	44.6	4	91.00
# 158	46.6	4	86.00
# 159 rows × 3 columns
# 
# Cylinders	Miles_per_Gallon
# 0	3	20.550000
# 1	4	29.286765
# 2	5	27.366667
# 3	6	19.985714
# 4	8	14.963107
# Miles_per_Gallon
# 14.963107
# 19.985714
# 20.550000
# 27.366667
# 29.286765

# In[ ]:





# In[ ]:




