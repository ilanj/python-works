import pandas as pd

df = pd.read_excel("guggug.xlsx")
column_names = df["Document Type"].value_counts().to_dict()
output_path = "frvdf/dfdb/gb/g/"
for column_name in column_names.keys():
    _temp_df = df[df["Document Type"] == column_name]
    _temp_df.to_excel(output_path + column_name + ".xlsx", index=False)
    del _temp_df
