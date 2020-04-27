
# coding: utf-8

# In[1]:


# Filter the uneccesary warnings
import warnings
warnings.filterwarnings("ignore")


# In[2]:


# Import pandas and numpy
import pandas as pd
import numpy as np

# Fix the random seed
np.random.seed(7)


# In[23]:


# Load the dataset

url = 'https://raw.githubusercontent.com/sayakpaul/Manning-Phishing-Websites-Detection/master/Phishing.csv'
data = pd.read_csv(url)
data.head(100)


# In[22]:


data.sample(10)


# In[24]:


data.sample(10).T


# In[25]:


# Data dimension
data.shape


# In[26]:


# Data columns
data.columns


# In[27]:


data["Result"].unique()

