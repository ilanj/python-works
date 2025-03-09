import pandas as pd

col_names = ["sl_no", "age", "gender", "role", "id"]
data = pd.read_table(
    "G:\workspace\pythontutorial\io_files//ex.txt", sep="|", names=col_names
)
print(data.dtypes)
print(data.head())
# avg age across
print(data.age.mean())
# if u wanna find mean with gender
print(data.groupby("gender").age.mean())
print(data[data.gender == "M"].age.mean())

print(data.groupby("gender").age.max())
print(data.groupby("gender").age.agg(["count", "min", "max", "mean"]))

print(data[data.gender == "M"].mean())
data.groupby("age").mean().plot(kind="bar")
