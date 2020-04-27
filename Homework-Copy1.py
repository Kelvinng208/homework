
# coding: utf-8

# In[1]:


import pandas as pd    #A

url=https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/d546eaee765268bf2f487608c537c05e22e4b221/iris.csv    #B

 

iris_dataframe=pd.read_csv(url)    #C

iris_dataframe.head()    #D


# In[2]:


import pandas as pd

url = 'https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.csv'
df = pd.read_csv(url, index_col=0)
print(df.head(5))


# In[17]:


import pandas as pd

url = 'https://github.com/sayakpaul/Manning-Phishing-Websites-Detection/blob/master/Phishing.csv'
df = pd.read_csv(url, header='infer', delimiter=None, names=None, index_col=None, usecols=None, error_bad_lines=False)
print(df.head(5))


# In[15]:


pd.show_versions() 

