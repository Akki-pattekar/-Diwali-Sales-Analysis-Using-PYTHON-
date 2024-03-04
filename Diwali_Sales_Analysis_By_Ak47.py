#!/usr/bin/env python
# coding: utf-8

# # Diwali_Sales_Analysis_By_Akshay Pattekar
# 

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # visualizing data
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


# import csv file
df = pd.read_csv(r'C:\Users\Admin\Downloads\Python_Diwali_Sales_Analysis\Diwali Sales Data.csv', encoding= 'unicode_escape')


# In[3]:


df.shape


# In[4]:


df.head()


# # Data_Cleaning

# In[5]:


df.info()


# In[6]:


#drop unrelated /blank columns
df.drop(['Status','unnamed1'],axis=1, inplace=True)


# In[7]:


#check for null values
pd.isnull(df).sum()


# In[8]:


#drop null values
df.dropna(inplace=True)


# In[9]:


df.shape


# In[10]:


pd.isnull(df).sum()


# In[11]:


#change data type
df['Amount'] = df['Amount'].astype(int)


# In[12]:


df['Amount'].dtypes


# In[13]:


df.info()


# In[14]:


df.columns


# In[15]:


#reanme column
df.rename(columns = {'Marital_Status':'Shadi'})


# In[16]:


#describe()Method returns descriptionof the data in the Dataframe(i.e. count, mean,std,Percentile, min, max, etc)
df.describe()


# In[17]:


#use describe () for specific columns
df[['Age','Orders','Amount']].describe()


# # Exploratory Data Analysis [EDA]
# 
# Gender

# In[ ]:





# In[18]:


sns.countplot(x = 'Gender',data = df)


# In[19]:


ax = sns.countplot(x = 'Gender',data = df)
    
for bars in ax.containers:
     ax.bar_label(bars)


# In[20]:


df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)


# In[21]:


sales_gen = df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x = 'Gender',y='Amount', data = sales_gen)


# ##### for above graphs we can see that most of the buyers are females and even the purchasing of famales are grater than man

# # Age

# In[22]:


df.columns


# In[23]:


ax=sns.countplot(data = df, x = 'Age Group',hue = 'Gender')
for bars in ax.containers:
    ax.bar_label(bars)


# In[24]:


#total amount vs Age Group
sales_age = df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by = 'Amount',ascending=False)

sns.barplot(x = 'Age Group', y = 'Amount',data = sales_age)


# #### from above graphs we can see that most of the buyers are of agegroup between 26-35years female

# ### State

# In[25]:


sales_age = df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by = 'Orders',ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(x = 'State', y = 'Orders',data = sales_age)


# In[26]:


sales_age = df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by = 'Amount',ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(x = 'State', y = 'Amount',data = sales_age)


# ##### from above graph we can see that most of the otders & total sales/amount are from Utter Pradesh, Maharashtra and Karnataka respectively

# ### Marital Status

# In[27]:


ax=sns.countplot(data = df, x = 'Marital_Status')
sns.set(rc={'figure.figsize':(4,2)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[28]:


sales_state = df.groupby(['Marital_Status' ,'Gender'],as_index=False)['Amount'].sum().sort_values(by = 'Amount',ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status', y = 'Amount',hue='Gender')


# ##### from above graphs we can see that most of the buyers are married(women) and they have high purchesing power

# # Occupation

# In[29]:


sns.set(rc={'figure.figsize':(20,5)})
ax=sns.countplot(data = df, x = 'Occupation')
for bars in ax.containers:
    ax.bar_label(bars)


# In[30]:


sales_state = df.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by = 'Amount',ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(x = 'Occupation', y = 'Amount',data = sales_state)


# ### from above graphs we can see that most of the uyers are working in IT Sector, Healtcare, Aviation etc. 

# In[31]:


df.columns


# ## Product Category

# In[32]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df,x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[33]:


sales_state = df.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by = 'Amount',ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(x = 'Product_Category', y = 'Amount',data = sales_state)


# #### from above graphs we can see that most of the sold products are from food clothing and Electronics category etc.

# In[34]:


sales_state = df.groupby(['Product_ID'],as_index=False)['Orders'].sum().sort_values(by = 'Orders',ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(x = 'Product_ID', y = 'Orders',data = sales_state)


# In[35]:


#top 10 most sold products (same thing as above)

fig, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# # Conclusion:

# ##### Married women age group 26-35 yrs from uttar Pradesh, Maharashtra and Karnataka working in IT, Healthcare and aviation are more likely to buy product from food clothing and Electronics Category

# # By: Akshay Pattekar
# 
# 

# ### Thank You...!

# In[ ]:




