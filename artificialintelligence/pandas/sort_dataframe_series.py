import pandas as pd
col_names=['sl_no','age','gender','role','id']
data=pd.read_table("/home/ila/PycharmProjects/pythonworks/artificialintelligence/pandas/files/ex.txt",sep="|",names=col_names)#not sure ahy header=0 is used
print(data.head())
print(data.dtypes)
# print(data.role.sort_values())#sorts in asc order
print(data['age'].sort_values(ascending=False))#sorts in asc order, but only prescried rows are displayed
#to display the whole dataframe
data.sort_values('age',inplace=True)
print(data)
print(data.sort_values(['gender','age']))#priority is left to right
print(data.age.head())

