import pandas as pd
import numpy as np

col_names = ["sl_no", "age", "gender", "role", "id"]
data = pd.read_table(
    "/home/ila/PycharmProjects/pythonworks/artificialintelligence/pandas/files/ex.txt",
    sep="|",
    names=col_names,
)
print(data.columns)
select_data = pd.read_table(
    "/home/ila/PycharmProjects/pythonworks/artificialintelligence/pandas/files/ex.txt",
    sep="|",
    names=col_names,
    usecols=[0, 1, 4],
)
print(select_data.columns)
# read n rows fast
select_rows = pd.read_table(
    "/home/ila/PycharmProjects/pythonworks/artificialintelligence/pandas/files/ex.txt",
    sep="|",
    names=col_names,
    usecols=[0, 1, 4],
    nrows=3,
)
print(select_rows)

for x in data.role:
    print(x)

for i, x in data.iterrows():
    print(i, x.age, x.role)

# select columns which are numbers
select_columns_bytypes = data.select_dtypes(include=[np.number])
print(select_columns_bytypes.dtypes)
print(select_columns_bytypes.describe())
# selection
print(data.describe(include="all"))  # will get NaN for non numbers
print(data.describe(include=["object", "int64"]))  # will get NaN for non numbers
