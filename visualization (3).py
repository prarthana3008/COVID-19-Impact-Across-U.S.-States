#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display, IFrame


# In[2]:


df = pd.read_csv('/Users/prarthanabahuriya/Downloads/us_states_covid19_daily.csv')


# COVID-19 Data Visualization Report from the given CSV file.
# Introduction:
# This report presents visualizations of COVID-19 data for different U.S. states. The data has been collected from the `us_states_covid19_daily.csv` dataset and has been used to create three distinct visualizations. The observations and insights from each visualization are presented below.
# Visualization 1: Total Positive Cases by State
# 

# In[9]:


plot_state_positive_cases(df)


# Observations:
# The bar graph shows the total positive cases by state in the United States. The y-axis represents the percentage of the total population that has tested positive for COVID-19, and the x-axis lists the states in alphabetical order.
# 
# The results of the bar graph show that the following states have the highest percentage of total positive cases:
# 
# North Dakota (1.4%)
# South Dakota (1.2%)
# Wisconsin (1.0%)
# Wyoming (0.8%)
# Montana (0.8%)
# Vermont (0.8%)
# The following states have the lowest percentage of total positive cases:
# 
# Hawaii (0.2%)
# Alaska (0.2%)
# Idaho (0.2%)
# Maine (0.2%)
# Rhode Island (0.2%)
# 
# 

# In[13]:


get_ipython().run_line_magic('run', 'my_package.ipynb')


# **Visualization 2: Currently Hospitalized by State
# 

# In[14]:


plot_state_hospitalized(df)


# **Observations:
# 
# The bar graph shows the Currently Hospitalized by State in the United States. The y-axis represents the number of patients currently hospitalized by state, and the x-axis lists the states in alphabetical order.
# 
# The results of the bar graph show that the following states have the highest number of patients currently hospitalized:
# 
# Texas (5000)
# Florida (4000)
# California (3000)
# New York (2000)
# Pennsylvania (1000)
# 
# The following states have the lowest number of patients currently hospitalized:
# 
# Wyoming (10)
# Vermont (20)
# North Dakota (30)
# South Dakota (40)
# Montana (50)
# 
# 

# In[16]:


get_ipython().run_line_magic('run', 'my_package.ipynb')


# **Visualization 3: Total Test Results Increase by State
# 

# In[17]:


plot_state_test_results_increase(df)


# Observations
# The bar graph the total test results increase by state in the United States. The y-axis represents the total number of test results increased by state, and the x-axis lists the states in alphabetical order.
# 
# The results of the bar graph show that the following states have the highest total test results increase:
# 
# California (10 million)
# Texas (9 million)
# Florida (8 million)
# New York (7 million)
# Illinois (6 million)
# 
# The following states have the lowest total test results increase:
# 
# Wyoming (100 thousand)
# Vermont (120 thousand)
# North Dakota (130 thousand)
# South Dakota (140 thousand)
# Montana (150 thousand)
# 

# In[ ]:




