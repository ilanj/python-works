import pandas as pd
col_names=['sl_no','age','gender','role','id']
data=pd.read_table("G:\workspace\pythontutorial\io_files//ex.txt",sep="|",names=col_names)
print(data.columns)
#if i want to drop columns
data.drop('sl_no',axis=1,inplace=True)
print(data.columns)

#can drop a row by
data.drop(2,axis=0)
print(data.drop([0,3],axis=0))
print(data.drop([0,3],axis=0).head())
print(data.dtypes)
print(data.mean())
print(data.mean(axis=0))#mean of each column-same as above can also use axis='index'
print(data.mean(axis=1))#mean of each row-can also use axis='columns'

print(data.mean(axis=1).shape)



