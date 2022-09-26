#!/usr/bin/env python
# coding: utf-8

# In[45]:


#pip install streamlit


# In[46]:


#!pip install plotly


# In[47]:


import streamlit as st
import pandas as pd
import numpy as np
from matplotlib.pyplot import scatter
import plotly.express as px 
import plotly.graph_objects as go
from joblib import dump, load
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import pydeck as pdk
import altair as alt
from datetime import datetime


# In[48]:


st.title("Using Streamlit for World Population Visualizations")


# In[55]:


agree1 = st.checkbox('I agree')

if agree1:
    st.write('Welcome to World Population Visualizations!')


# In[56]:


df = pd.read_csv("/Users/jose/Desktop/MSBA 325- Data Visualization & Communication/2- Visualizations in Context/Submission- Practicing on Visualizing with Python & Plotly/JosephineKaadou_jjk25_PracticingonVisualizingwithPython&Plotly/world_population.csv")


# In[57]:


st.write(df.head())


# In[69]:


st.subheader('Map showing 2022 Population by Continent')

fig1 = px.choropleth(df,
                     locations='Country',
                     locationmode='country names',
                     color='2022 Population',
                     color_continuous_scale=px.colors.sequential.Sunset)
st.plotly_chart(fig1)


# In[70]:


st.subheader('Piecharts showing Population by Continent for a specified year')

year_options = st.selectbox('Select Year', ['2000 Population', '2022 Population'])

populationx=df.groupby(by='Continent')[year_options].sum()
fig3=px.pie(values=populationx.values,
          names=populationx.index,
          color_discrete_sequence=px.colors.sequential.Peach)
fig3.update_traces(textinfo='label+percent+value', textfont_size=13,
                  marker=dict(line=dict(color='#100000', width=0.2)))

fig3.data[0].marker.line.width = 2
fig3.data[0].marker.line.color='gray'
st.plotly_chart(fig3)


# In[71]:


st.subheader('BarChart showing Number of Countries By Continent')

country=df['Continent'].value_counts()
fig6=px.bar(x=country.index,
          y=country.values,
          color=country.index,
          color_discrete_sequence=px.colors.sequential.Aggrnyl,
          text=country.values)

fig6.update_layout(xaxis_title="Countries",
                 yaxis_title="Count",
                 font=dict(size=15, family="Arial"))
st.plotly_chart(fig6)


# In[72]:


# population_features = ['2022 Population','2020 Population','2015 Population','2010 Population','2000 Population','1990 Population','1980 Population','1970 Population']


# In[73]:


# population_features.reverse()
# plt.figure(figsize=(25,10))
# for feature in population_features:
#     plt.plot(continent[feature],label = feature)
# plt.legend()
# plt.title('Year-to-year population change of continents', size=25);
# plt.show();


# In[74]:


st.subheader('Scatter Plot showing relationship between Area and chosen variable')

plot2_options = st.selectbox('Which variable to plot against Area?', ["Density (per km²)","Rank"])

fig7= px.scatter(df, x="Area (km²)", 
           y=plot2_options, 
           color="Continent", 
           size="2022 Population", 
           size_max=60, hover_name="Country")

fig7.update_layout(width=800)
st.plotly_chart(fig7)


# In[75]:


st.subheader('Scatter Plot showing relationship between Growth Rate and chosen variable')

plot3_options = st.selectbox('Which variable to plot against Growth Rate?', ["Density (per km²)","Rank"])

fig8= px.scatter(df, x="Growth Rate", 
           y=plot3_options, 
           color="Continent", 
           size="2022 Population", 
           size_max=60, hover_name="Country" )

fig8.update_layout(width=800)
st.plotly_chart(fig8)

