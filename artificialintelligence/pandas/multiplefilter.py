import pandas as pd
col_names=['sl_no','age','gender','role','id']
data=pd.read_table("G:\workspace\pythontutorial\io_files//ex.txt",sep="|",names=col_names)#not sure ahy header=0 is used
print(data.head())
print(data[data.age>25])