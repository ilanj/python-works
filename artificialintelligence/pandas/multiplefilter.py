import pandas as pd

col_names = ["sl_no", "age", "gender", "role", "id"]
data = pd.read_table(
    "/home/ila/PycharmProjects/pythonworks/artificialintelligence/pandas/files/ex.txt",
    sep="|",
    names=col_names,
)  # not sure ahy header=0 is used
print(data.head())
print(data[data.age > 25])
