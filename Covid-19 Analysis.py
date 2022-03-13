#!/usr/bin/env python
# coding: utf-8

# ##  Covid-19 Data Analysis 

# In[6]:


# Importing the needed modules
import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
print('Modules are imported.')


# ## Task 2

# ### Task 2.1: Importing Covid-19 Dataset
# importing "time_series_covid19_confirmed_global.csv" from "./datasets" folder. 

# In[7]:


corona_dataset_csv = pd.read_csv("datasets/time_series_covid19_confirmed_global.csv")
corona_dataset_csv.head(10)


# #### Let's check the shape of the dataframe

# In[3]:


corona_dataset_csv.shape


# ### Task 2.2: Delete the useless columns

# In[4]:


# Axis = 0 is the default value, axis 0 is the X-axis while axis 1 is the Y-axis
# inplace=True to apply the change directly and store it in the same value
# .drop is to remove the unwanted columns
corona_dataset_csv.drop(["Lat","Long"],axis=1,inplace=True)


# In[5]:


corona_dataset_csv.head(10)


# ### Task 2.3: Aggregating the rows by the country

# In[6]:


# Aggregating with Country as the START, instead of numbers and sum is used to aggregate all of them not just one
corona_dataset_aggregated = corona_dataset_csv.groupby("Country/Region").sum()


# In[7]:


corona_dataset_aggregated.head()


# In[8]:


corona_dataset_aggregated.shape


# ### Task 2.4: Visualizing data related to a country for example China
# visualization always helps for better understanding of our data.

# In[9]:


#corona_dataset_aggregated.loc["China"].plot()
#corona_dataset_aggregated.loc["Italy"].plot()
#corona_dataset_aggregated.loc["Turkey"].plot()
#corona_dataset_aggregated.loc["Spain"].plot()
#corona_dataset_aggregated.loc["Mauritania"].plot()
corona_dataset_aggregated.loc["Morocco"].plot()
corona_dataset_aggregated.loc["Algeria"].plot()
corona_dataset_aggregated.loc["Tunisia"].plot()
corona_dataset_aggregated.loc["Libya"].plot()
#corona_dataset_aggregated.loc["US"].plot()
#corona_dataset_aggregated.loc["Egypt"].plot()
#corona_dataset_aggregated.loc["Sudan"].plot()
# To cleariify which colour belongs to which country
plt.legend()


# ### Covid-19 Cases in North Africa

# In[10]:


North_Africa_Region = corona_dataset_aggregated.loc["Morocco"]+corona_dataset_aggregated.loc["Algeria"]+corona_dataset_aggregated.loc["Tunisia"]+corona_dataset_aggregated.loc["Libya"]+corona_dataset_aggregated.loc["Mauritania"]+corona_dataset_aggregated.loc["Egypt"]+corona_dataset_aggregated.loc["Sudan"]
North_Africa_Region.plot()


# ### Task3: Calculating a good measure 
# we need to find a good measure reperestend as a number, describing the spread of the virus in a country. 

# In[11]:


corona_dataset_aggregated.loc["China"].plot()


# In[12]:


corona_dataset_aggregated.loc["China"][:3].plot()


# ### task 3.1: caculating the first derivative of the curve

# In[13]:


corona_dataset_aggregated.loc["China"].diff().plot()


# ### task 3.2: find maximum infection rate for China

# In[14]:


corona_dataset_aggregated.loc["China"].diff().max()


# In[15]:


corona_dataset_aggregated.loc["Libya"].diff().max()


# In[16]:


corona_dataset_aggregated.loc["Tunisia"].diff().max()


# In[17]:


corona_dataset_aggregated.loc["Algeria"].diff().max()


# In[18]:


corona_dataset_aggregated.loc["Morocco"].diff().max()


# ### Task 3.3: find maximum infection rate for all of the countries

# In[19]:


countries = list(corona_dataset_aggregated.index)
max_infection_rate = []
for c in countries:
    max_infection_rate.append(corona_dataset_aggregated.loc[c].diff().max())
corona_dataset_aggregated["Max Infection Rate"] = max_infection_rate


# In[20]:


corona_dataset_aggregated.head()


# ### Task 3.4: Create a new dataframe with only needed column

# In[21]:


corona_data = pd.DataFrame(corona_dataset_aggregated["Max Infection Rate"])


# In[22]:


corona_data.head()


# ### Task 4: 
# - Importing the WorldHappinessReport.csv dataset
# - selecting needed columns for our analysis 
# - join the datasets 
# - calculate the correlations as the result of our analysis

# In[23]:


happiness_report_csv = pd.read_csv("Datasets/2019.csv")


# In[24]:


happiness_report_csv.head()


# ### Task 4.2: let's drop the useless columns

# In[25]:


useless_columns = ["Overall rank", "Score", "Generosity", "Perceptions of corruption"]


# In[26]:


happiness_report_csv.drop(useless_columns, axis=1, inplace=True)
happiness_report_csv.head()


# ### Task 4.3: Changing the indices of the dataframe

# In[27]:


happiness_report_csv.set_index("Country or region", inplace=True)


# In[28]:


happiness_report_csv.head()


# ### Task 4.4: join the two datasets that we prapared

# #### Corona Dataset:

# In[29]:


corona_data.head()


# In[30]:


corona_data.shape


# #### World Happiness Dataset:

# In[31]:


happiness_report_csv.head()


# In[32]:


happiness_report_csv.shape


# In[33]:


data = corona_data.join(happiness_report_csv, how="inner")


# In[34]:


data.head(10)


# ### Task 4.5: Correlation Matrix

# In[35]:


data.corr()


# ### Task 5: Visualization of the results
# our Analysis is not finished unless we visualize the results in terms figures and graphs so that everyone can understand what you get out of our analysis

# In[36]:


data.head()


# ### Task 5.1: Plotting GDP vs Maximum Infection Rate

# In[37]:


x = data["GDP per capita"]
y = data["Max Infection Rate"]
# Infection rate number is high so we used np.log to make more understandable graph
d = np.log(y)
# For analysis with dots using the seaborn library
sns.scatterplot(x, d)


# In[38]:


# for analysis with dots and a line to make it clearer
sns.regplot(x, d)


# ### Task 5.2: Plotting Social Support vs Maximum Infection Rate

# In[39]:


s = data["Social support"]
sns.scatterplot(s, d)


# In[40]:


sns.regplot(s, d)


# ### Task 5.3: Plotting Healthy life expectancy vs Maximum Infection Rate

# In[70]:


h = data["Healthy life expectancy"]
sns.scatterplot(h, d)


# In[71]:


sns.regplot(h, d)


# ### Task 5.3: Plotting Freedom to make life choices vs Maximum Infection Rate

# In[72]:


f = data["Freedom to make life choices"]
sns.scatterplot(f, d)


# In[73]:


sns.regplot(f, d)


# In[ ]:




