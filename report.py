#!/usr/bin/env python
# coding: utf-8

# # A Deep Dive into the COVID-19 Impact Across U.S. States
# 

# **INTRODUCTION:-
# 
# *COVID-19 has been the defining global health crisis of our time. This report delves into the pandemic's varying impact across select U.S. states.
# **We'll explore how the number of positive cases correlates with hospitalizations and fatalities.
# 

#  **Data Summary
#  
# *Our data comes from the COVID-19 Tracking Project and covers a range of variables from 15,633 records across 55 attributes. This rich dataset offers an opportunity to assess the pandemic's impact through multiple lenses. For this report, we focus on the number of positive cases, hospitalizations, and deaths.
# Python Code:
# df = pd.read_csv('us_states_covid19_daily.csv')
# df.describe()
# 

# **Exploratory Data Analysis (EDA)
# 
# *Using summary statistics and graphical analyses, we can tease out patterns and correlations. For instance, the average number of positive cases across the selected states stands at around 100,487.
# 

# **Inference
# 
# Our analysis unveils a strong correlation between positive cases and the strain on healthcare systems. This is crucial for healthcare planning, resource allocation, and policy formulation.
# 

# **Conclusion
# 
# The COVID-19 pandemic’s impact varies significantly across states. The insights from this report can guide healthcare policies and interventions, providing a data-driven foundation for tackling the crisis.The states with the highest percentage of total positive cases are generally located in the Midwest and Great Plains regions.
# The states with the lowest percentage of total positive cases are generally located in the Northeast and West Coast regions.
# There are a few exceptions to this trend, such as Hawaii, which has a very low percentage of total positive cases despite being located in the West Coast region.
# The states with the highest number of patients currently hospitalized are generally located in the South and Southwest regions.
# The states with the lowest number of patients currently hospitalized are generally located in the Mountain West and Great Plains regions.
# There are a few exceptions to this trend, such as New York, which has a relatively high number of patients currently hospitalized despite being located in the Northeast region.
# The states with the highest total test results increase are generally located in the West, South, and Midwest regions.
# The states with the lowest total test results increase are generally located in the Mountain West and Great Plains regions.
# There are a few exceptions to this trend, such as New York, which has a relatively high total test results increase despite being located in the Northeast region.
# 
# 

# **References:-
# 
# youtube videos (https://www.youtube.com/watch?v=Liv6eeb1VfE&t=999s&ab_channel=AlexTheAnalyst)
# (https://www.youtube.com/watch?v=xi0vhXFPegw&ab_channel=RobMulla)
