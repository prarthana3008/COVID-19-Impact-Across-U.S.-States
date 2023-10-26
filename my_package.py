#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


df = pd.read_csv('/Users/prarthanabahuriya/Downloads/us_states_covid19_daily.csv')


# In[3]:


df.head()


# In[4]:


df.info


# In[5]:


def plot_state_positive_cases(data):
    state_positive_cases = data.groupby('state')['positive'].max()
    colors = plt.cm.viridis(state_positive_cases / state_positive_cases.max())

    plt.figure(figsize=(12, 6))
    plt.bar(state_positive_cases.index, state_positive_cases, color=colors)
    plt.xlabel('State')
    plt.ylabel('Total Positive Cases')
    plt.title('Total Positive Cases by State')
    plt.xticks(rotation=45)
    plt.colorbar(plt.cm.ScalarMappable(cmap=plt.cm.viridis), label='Total Positive Cases', orientation='vertical')
    plt.show()


# In[6]:


def plot_state_hospitalized(data):
    state_hospitalized = data.groupby('state')['hospitalizedCurrently'].mean()
    colors = plt.cm.coolwarm(state_hospitalized / state_hospitalized.max())

    plt.figure(figsize=(12, 6))
    plt.bar(state_hospitalized.index, state_hospitalized, color=colors)
    plt.xlabel('State')
    plt.ylabel('Currently Hospitalized')
    plt.title('Currently Hospitalized by State')
    plt.xticks(rotation=45)
    plt.colorbar(plt.cm.ScalarMappable(cmap=plt.cm.coolwarm), label='Currently Hospitalized', orientation='vertical')
    plt.show()


# In[7]:


def plot_state_test_results_increase(data):
    state_test_results_increase = data.groupby('state')['totalTestResultsIncrease'].max()
    colors = plt.cm.YlGnBu(state_test_results_increase / state_test_results_increase.max())

    plt.figure(figsize=(12, 6))
    plt.bar(state_test_results_increase.index, state_test_results_increase, color=colors)
    plt.xlabel('State')
    plt.ylabel('Total Test Results Increase')
    plt.title('Total Test Results Increase by State')
    plt.xticks(rotation=45)
    plt.colorbar(plt.cm.ScalarMappable(cmap=plt.cm.YlGnBu), label='Total Test Results Increase', orientation='vertical')
    plt.show()


# In[ ]:




