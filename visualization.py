#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display, IFrame


# In[2]:


df = pd.read_csv('/Users/prarthanabahuriya/Downloads/us_states_covid19_daily.csv')


# In[9]:


plot_state_positive_cases(df)


# In[13]:


get_ipython().run_line_magic('run', 'my_package.ipynb')


# In[14]:


plot_state_hospitalized(df)


# In[16]:


get_ipython().run_line_magic('run', 'my_package.ipynb')


# In[17]:


plot_state_test_results_increase(df)


# In[ ]:




