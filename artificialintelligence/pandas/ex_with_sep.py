import pandas as pd

colnames=['rowno','age','gender','role','empid']
data=pd.read_table("G:\workspace\pythontutorial\io_files/ex.txt",sep="|",names=colnames)
column=data.head()
print(data)
print(column)
print(data.describe())
print(data.dtypes)
print(data.describe(include=['object']))