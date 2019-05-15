import pandas as pd
col_names=['sl_no','age','gender','role','id']
data=pd.read_table("G:\workspace\pythontutorial\io_files//ex.txt",sep="|",names=col_names)
print(data.head())
print(data['role'].str.upper())
print(data.role.str.lower())
print(data.role.str.contains('or'))#will only display boolean result
print(data[data.role.str.contains('or')])#will display as a table(roles educator and administrator will be displayed)

