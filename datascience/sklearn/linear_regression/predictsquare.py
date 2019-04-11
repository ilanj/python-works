import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data=pd.read_csv("G:\workspace\pythontutorial\datascience\linear_regression\squares.csv")

X=data[["no"]]
Y=data[["sq"]]
# prediction=train.predict(np.array([[20]]))
# prediction=train.predict(data[["no"]])
# train.fit(data[["no"]],data[["sq"]])
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
train=LinearRegression()
train.fit(data[["no"]],data[["sq"]])
y_pred = train.predict(np.array([[10]]))
print(y_pred)