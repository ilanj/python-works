import pandas as pd
col_names=['sl_no','age','gender','role','id']
data=pd.read_table("G:\workspace\pythontutorial\io_files//ex.txt",sep="|",names=col_names)
print(data.dtypes)
print(data.head())

print(data.age.describe())
print(data.role.describe())
print(data.role.value_counts())
print(data.role.value_counts(normalize=True))
#value_counts is itself a series
print(type(data.role.value_counts()))
print(data.role.unique())
print(data.role.nunique())#nunique will no of uniques
print(pd.crosstab(data.role,data.age))




