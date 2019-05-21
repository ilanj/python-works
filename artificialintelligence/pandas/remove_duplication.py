import pandas as pd
colnames=['slno','age','sex','role','zipcode']
data=pd.read_table('G:\workspace\pythontutorial\io_files\duplicaterows.txt',sep='|',names=colnames,index_col='slno',header=None)
print(data.head())
print(data.zipcode.duplicated())
print(data.zipcode.duplicated().sum())

print(data.duplicated().sum())
print(data.loc[data.duplicated(),:])
print(data.loc[data.duplicated(keep='last'),:])
print(data.loc[data.duplicated(keep=False),:])
#remove duplicates
print(data.shape)
print((data.drop_duplicates(keep='first')).shape)
print((data.drop_duplicates(keep=False)).shape)#drops all duplicates

print(data.duplicated(subset=['age','zipcode']).sum())
print(data.drop_duplicates(subset=['age','zipcode']).sum())
print(data.drop_duplicates(subset=['age','zipcode']).shape)
