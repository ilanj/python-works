import pandas as pd

data = pd.read_csv(
    "/home/ila/PycharmProjects/pythonworks/artificialintelligence/pandas/files/CausesOfDeath_France_2001-2008.csv"
)
print(data)
print(data.dtypes)
# droping a single column
data.drop("ICD10", axis=1, inplace=True)  # axis=1 denotes column
print(data.head)
# dropping multiple columns
data.drop(["Value", "AGE"], axis=1, inplace=True)
print(data.head())

# drop first 2 rows, here axis=0 represents column
data.drop([0, 1], axis=0, inplace=True)
print("after clipping first 2" + data.head())
