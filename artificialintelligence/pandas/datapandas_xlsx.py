#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import xlrd



# In[9]:

my_sheet = 'Sheet1'
file_name = 'D://dsddws.xlsx' # name of your excel file
df = pd.read_excel(file_name)
print(df) # shows headers with top 5 rows

# In[ ]:




