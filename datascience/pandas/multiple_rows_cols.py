#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

data=pd.read_table("G:\workspace\pythontutorial\io_files\orders.txt")


# In[4]:


data.head(3)


# In[9]:


data.loc[0,:]# : means all columns


# In[10]:


data.loc[[0,1,2],:]


# In[13]:


data.loc[0:2,:]


# In[14]:


data.loc[0:2]


# In[19]:


data.loc[0:3,'quantity':'item_price']


# In[20]:


data.head(3).drop('item_price',axis=1)


# In[22]:


data.loc[data.quantity==1,'item_name']


# In[28]:


data.iloc[:,0:2]


# In[34]:


data.ix[data.index,0]


# In[ ]:





# In[ ]:




