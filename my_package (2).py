#!/usr/bin/env python
# coding: utf-8

# #Introduction
# COVID-19 has been the defining global health crisis of our time. This report delves into the pandemic's varying impact across select U.S. states. We'll explore how the number of positive cases correlates with hospitalizations and fatalities.
# 

# In[8]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# #**Data Summary
# 
# *Our data comes from the COVID-19 Tracking Project and covers a range of variables from 15,633 records across 55 attributes. This rich dataset offers an opportunity to assess the pandemic's impact through multiple lenses. For this report, we focus on the number of positive cases, hospitalizations, and deaths.
# Python Code:
# df = pd.read_csv('us_states_covid19_daily.csv')
# df.describe()
# 

# In[2]:


df = pd.read_csv('/Users/prarthanabahuriya/Downloads/us_states_covid19_daily.csv')


# In[3]:


df.head()


# #THE INFORMATION OF THE DATA TAKEN IS PROVIDED BELOW

# In[4]:


df.info


# # EDA (exploratory data analysis)

# 
# **Using summary statistics and graphical analyses, we can tease out patterns and correlations. For instance, the average number of positive cases across the selected states stands at around 100,487. delcaring the functions for the research questions
# 
# 

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


# This function creates a bar graph showing the total number of positive COVID-19 instances broken down by state using a Pandas DataFrame as input.
# 
# The function determines the maximum positive case count for each state after first grouping the DataFrame by state. Next, based on the total number of affirmative cases in each state, a color is assigned to each state using the plt.cm.viridis() colormap. The color intensity increases with the total positive case count.
# 
# Using the colors allocated in the previous phase, the program then builds a new figure and draws a bar chart of the total positive cases by state. The rotation, title, and labels for the x and y axes are also set by this function. Lastly, it displays the figure and adds a colorbar to the plot.

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


# This program produces a bar graph of the COVID-19 patients who are currently hospitalized by state using a Pandas DataFrame as input.
# 
# The plot_state_positive_cases() function that you previously provided and this function are extremely similar. The primary distinction is that, as opposed to calculating the maximum positive case count, the plot_state_hospitalized() method determines the mean number of patients who are hospitalized at any given time for each state.

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


# The code you submitted uses plot_state_test_results_increase(), a Python function. This program creates a bar graph showing the overall test results rise by state using a Pandas DataFrame as input.
# 
# The plot_state_positive_cases() and plot_state_hospitalized() functions that you previously gave are comparable to this function. Nevertheless, rather than calculating the maximum positive case count or the mean number of patients currently hospitalized, the plot_state_test_results_increase() method determines the maximum total test results rise for each state.
# 
# 
# 
