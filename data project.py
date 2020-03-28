#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[32]:


url="https://cocl.us/datascience_survey_data"
TS_data=pd.read_csv(url,index_col=0)


# In[33]:


TS_data.head(5)

TS_data.dtypes


# In[34]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.style.use('ggplot')


# In[35]:



TS_data.sort_values(['Very interested'], ascending=False, axis=0, inplace=True)

TS_data


# In[38]:


r=2233

TS_data_surveypct = ((TS_data / r) *100).round(2)


# In[40]:


ax = TS_data_surveypct.plot(kind='bar',
                       figsize = (20, 8),
                       width = 0.8,
                       color = ['#5cb85c', '#5bc0de', '#d9534f'],
                       fontsize = 14)

plt.title('Percentage of Respondents Interests\''' in Data Science Areas', fontsize=16) 
for p in ax.patches:
    ax.annotate(str(p.get_height()) + '%', (p.get_x() * 1.005, p.get_height() * 1.03))
    
#https://stackoverflow.com/questions/25447700/annotate-bars-with-values-on-pandas-bar-plots 
#used to assist in annotating columns


# In[46]:


crime_data = pd.read_csv("https://cocl.us/sanfran_crime_dataset")


# In[47]:


crime_data.head(5)


# In[50]:


crime_dis = crime_data.groupby(['PdDistrict']).count().reset_index()
crime_dis.drop(['Category','Descript','DayOfWeek','Date','Time', 'Resolution','Address','X','Y','Location','PdId'], axis=1, inplace=True)


# In[52]:


crime_dis.rename(columns={'PdDistrict':'Neighborhood', 'IncidntNum':'Count'}, inplace=True)


# In[53]:


crime_dis


# In[54]:


#https://cocl.us/sanfran_geojson

get_ipython().system('wget --quiet https://cocl.us/sanfran_geojson -O sanfran_geo.json    ')


# In[55]:


get_ipython().system('conda install -c conda-forge folium=0.5.0 --yes')
import folium


# In[56]:


san_fran_map = r'sanfran_geo.json'


# In[59]:


san_fran = folium.Map(location=[37.773972, -122.431297], zoom_start=12) #, tiles='Mapbox Bright')
san_fran.choropleth(
    geo_data=san_fran_map,
    data=crime_dis,
    columns=['Neighborhood','Count'],
    key_on='feature.properties.DISTRICT',
    fill_color='YlOrRd', 
    fill_opacity=0.7, 
    line_opacity=0.2,
    legend_name='SF Crimes'
)


# In[60]:


san_fran


# In[ ]:




