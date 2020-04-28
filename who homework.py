
# coding: utf-8

# In[1]:


import geonamescache

gc = geonamescache.GeonamesCache()
countries = gc.get_countries()
# print countries dictionary
print(countries)
# you really wanna do something more useful with the data...


# In[2]:


headline_file = open('headlines.txt','r')
headlines = [line.strip()
             for line in headline_file.readlines()]
num_headlines = len(headlines)
print(f"{num_headlines} headines have been loaded")


# In[5]:


import regex as re

def name_to_regex(name):
    decoded_name = unidecode(name)
    if name != decoded_name:
        regex = fr'\b({name}|{decoded_name})\b'
    else:
        regex = fr'\b{name}\b'
    return re.compile(regex, flags=re.IGNORECASE)


# In[6]:


import geonamescache

gc = geonamescache.GeonamesCache()
countries = gc.get_countries()
# print countries dictionary
print(countries)
# you really wanna do something more useful with the data...

from unidecode import unidecode
unidecode(u'ko\u017eu\u0161\u010dek')



countries = [country['name']
             for country in gc.get_countries().values()]
country_to_name = {name_to_regex(name): name
                   for name in countries}

cities = [city['name'] for city in gc.get_cities().values()]
city_to_name = {name_to_regex(name): name for name in cities}


# In[7]:


import pandas as pd

matched_countries = [get_name_in_text(headline, country_to_name)
                     for headline in headlines]
matched_cities = [get_name_in_text(headline, city_to_name)
                  for headline in headlines]
data = {'Headline': headlines, 'City': matched_cities,
        'Country': matched_countries}
df = pd.DataFrame(data)


# In[8]:


summary = df[['City', 'Country']].describe()
print(summary)

