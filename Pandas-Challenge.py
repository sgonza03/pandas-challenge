#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Import packages we need 
import os
import csv
import numpy as np
import pandas as pd


# In[11]:


df = pd.read_csv(r'C:\Users\gonza\Desktop\du-den-data-pt-08-2020-u-c\04-Pandas\Homework\Instructions\HeroesOfPymoli\Resources\purchase_data.csv', low_memory = False,)
df.head()


# In[14]:


#first part of assignment is to find total number of players
ds = pd.DataFrame(df)
ds.nunique()
#SN represents players, so we have 576 unique players
#Number of total purchases will be given by Purchase IDs so 780
#total number of unique items will be 179 (Unique item names)


# In[25]:


#Average purchase price
print('Number of total purchases will be given by Purchase IDs so 780')
print('total number of unique items will be 179 (Unique item names)')
average =ds['Price'].mean()
print(f'the average purchase price is {average}')
total = ds['Price'].sum()
print(f'The total avenue is {total},')


# In[35]:


#To find percentage and count of male players
g = ds.loc[:,'Gender']
group = pd.DataFrame(g)
group.head(25)
groups = group.apply(pd.Series.value_counts, axis=0)
print(groups)
print(f'We see that the counts are male = 652, female = 113, undisclosed = 15')
groups2 = group.apply(pd.Series.value_counts, normalize = True, axis=0)
print(f'The relative frequencies are {groups2}')


# In[59]:


#Purchase Analysis
#We need to find total purchases counts per Gender
male_purchase_count = ds['Gender'].value_counts()['Male']
female_purchase_count = ds['Gender'].value_counts()['Female']
y = (780 - 652) - 113
print(f'The purchase count for others is {y}, for males its {male_purchase_count}, and for females its {female_purchase_count}')
#didnt assign original purchase accounts a variable so had to work aorund it


# In[63]:


#For average purchase male
male = ds.loc[ds['Gender'] == 'Male', :]
male_avg_price = male['Price'].mean()
#Female average purchase
female = ds.loc[ds['Gender'] == 'Female', :]
female_avg_price = female['Price'].mean()
#Others
other = ds.loc[ds['Gender'] != 'Female', :]
other_purchase = other.loc[ds['Gender'] != 'Male', :]
other_avg_price = other_purchase['Price'].mean()
print(f'average purchase for males was {male_avg_price}')
print(f'average purchase for females was {female_avg_price}')
print(f'average purchase for others was {other_avg_price}')


# In[65]:


#For totals we use sum
male_total_purchase = male.sum()["Price"]
female_total_purchase = female.sum()["Price"]
other_total_purchase = other_purchase.sum()["Price"]
print(f'total sales for men were {male_total_purchase}')
print(f'total sales for females were {female_total_purchase}')
print(f'total sales for others were {other_total_purchase}')


# In[70]:


#Age Demographics... We first need to create bins 
bin = [0, 9.9, 14.9, 19.9, 100]
names = ['<10','10-14','15-20','>20']
#Now we cut our data into the created bins
demographics = ds.loc[:, ["Gender", "SN", "Age","Price"]]
demographics["Age ranges"] = pd.cut(demographics["Age"], bin, labels=names)
demographics.head()


# In[74]:


#Now that we have our data we can do the analysis on age groups
demographics_total = demographics["Age ranges"].value_counts()
print(f'The purchase count per age group is {demographics_total}')
demographics_ave = demographics["Price"].mean()
print(f'The average purchase price per age group is {demographics_ave}')
demographics_total_sum = demographics["Price"].sum()
print(f'The total count per age group is {demographics_total_sum}')


# In[77]:


#Average Purchase Total per Person by Age Group
#Finding top spenders, spenders = sn, purch value = price. use groupby
player_total_purchase = ds.groupby(["SN"]).sum()["Price"]
player_average = ds.groupby(["SN"]).mean()["Price"]
player_count = ds.groupby(["SN"]).count()["Price"]
player_total_purchase.describe()
player_average.describe()
player_count.describe()


# In[ ]:


#for most popular items we use groupby, and change the column names
item_total_purchase = ds.groupby(["Item ID"]).sum()["Price"]
item_average = ds.groupby(["Item ID"]).mean()["Price"]
item_count = ds.groupby(["Item ID"]).count()["Price"]

