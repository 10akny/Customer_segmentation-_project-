#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Import our wrangling and visualization library
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
from scipy.stats import iqr
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans



df = pd.read_csv("D:\downloads2\marketing_campaign.csv", sep="\t")
df.head()


# In[9]:


#Exploratory Data Analysis
df["TotalAmountSpent"] = df["MntFishProducts"] + df["MntFruits"] + df["MntGoldProds"] + df["MntSweetProducts"] + df["MntMeatProducts"] + df["MntWines"]


# In[10]:


#Year Birth ,We need to convert year birth to an age feature
from datetime import datetime


# In[11]:


df["Age"] = df["Year_Birth"].apply(lambda x : datetime.now().year - x)


# In[12]:


df["Age"].describe()


# In[13]:


sns.histplot(data=df, x="Age", bins = list(range(10, 150, 10)))
plt.title("Distribution of Customer's Age")
plt.savefig("Age.png");


# In[14]:


df["Education"] = df["Education"].replace({"Graduation":"Graduate", "PhD":"Postgraduate", "Master":"Postgraduate", "2n Cycle":"Postgraduate", "Basic":"Undergraduate"})


# In[15]:


df["Education"].value_counts()


# In[16]:


df["Education"].unique()


# In[17]:


df["Education"].value_counts(normalize=True).plot.bar(figsize=(8, 6))
plt.xticks(rotation=45)
plt.title("Frequency of Customer's Education [proportion]");


# In[18]:


df["Marital_Status"].unique()


# In[ ]:




