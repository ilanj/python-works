import pandas as pd
data=pd.read_csv("G:\workspace\pythontutorial\io_files\kaggletrain.txt")
train=data.sample(frac=0.75,random_state=99)
test=data.loc[~data.index.isin(train.index),:]
print(train.count)
print(test.count)
print()