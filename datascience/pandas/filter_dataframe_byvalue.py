import pandas as pd
col_names=['sl_no','age','gender','role','id']
data=pd.read_table("G:\workspace\pythontutorial\io_files//ex.txt",sep="|",names=col_names)#not sure ahy header=0 is used
print(data.head())
# print(data.dtypes)
# print(data.shape)
# print(type(data.dtypes))
age_gt_25=[]
for x in data.age:
    if x > 25:
        age_gt_25.append(True)
    else:
        age_gt_25.append(False)

age_25=pd.Series(age_gt_25)# this is now just a series, but not a series inside table
print(type(age_25))
print(age_25)
print(data[age_25])#only age > 25 is displayed
'''
the above thing can be simplified as age_gt_25=data.age>25
'''
print(data[data.gender=='F'])#printing only gender f
print(data[data.gender=='F'].role)#printing only gender f
print(data[data.gender=='F']['role'])
print(data.loc[data.gender=='F','role'])#first param is a condition
