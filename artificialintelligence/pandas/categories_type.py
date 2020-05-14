'''if there are only 6 unique continents, but there are 1000000 rows, even this takes same space
we can store continents in a list, can pass index, so that it occupes less space
this is available readymade in pandas, called CATEGORY.
but if we are going to store country as category, it is going to store same no of strings and small integers.
so size increases substantially bur speeds up computations.
'''
import pandas as pd
col_names=['sl_no','age','gender','role','id']
data=pd.read_table("/home/ila/PycharmProjects/pythonworks/artificialintelligence/pandas/files/ex.txt",sep="|",names=col_names)#not sure ahy header=0 is used
print(data.columns)
print(data.info())#at the end shows in + in memory. object type stores string, and not counted
print(data.info(memory_usage='deep'))#now original size is displayed

print(data.memory_usage())#size in bytes
print(data.memory_usage(deep=True))
print(data.memory_usage(deep=True).sum())
print(data.head())

data['role']=data.role.astype('category')
print(data.dtypes)
print(data.memory_usage(deep=True))#size of roles is reduxed from 61400 to 2952

#if we wanna c the index
print(data.role.cat.codes)
print(data.role.cat.categories)

cache=pd.DataFrame({'ID':[100,101,102,103], 'quality': ['good','very good','good','excellent']})
print(cache)
print(type(cache))
print(type(cache.ID))
print(cache.sort_values('quality'))

