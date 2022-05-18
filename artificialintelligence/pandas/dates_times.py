import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('/home/ila/PycharmProjects/pythonworks/artificialintelligence/pandas/files/uforeports.txt')
print(data.head())

#time column to pandas special date time column-gonna replace
data.Time=pd.to_datetime(data.Time)
print(data.head())
print(data.dtypes)
print((data.Time.dt.weekday_name).head())
print((data.Time.dt.hour).head())
print((data.Time.dt.dayofyear).head())

timestamp=pd.to_datetime('1/1/1998')
print(data.loc[data.Time>=timestamp,:].head())

print(data.Time.max())
print(data.Time.max()-data.Time.min())
data['Year']=data.Time.dt.year
print(data.head())#year column is appended
# data.Year.value_counts().sort_index().plot
plt.plot(data.Year.value_counts())
plt.show()

plt.plot(data.Year)
plt.show()

