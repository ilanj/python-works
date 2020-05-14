#svc, decisiontree, knearest_neighbor works well
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, Lasso, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

data=pd.read_csv("squares.csv")

X=data[["no"]]
Y=data[["sq"]]
# prediction=train.predict(np.array([[20]]))
# prediction=train.predict(data[["no"]])
# train.fit(data[["no"]],data[["sq"]])
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
# train=LogisticRegression()
# train=SVC()
train=GaussianNB()
# train=DecisionTreeClassifier()
# train=KNeighborsClassifier()
train.fit(data[["no"]],data[["sq"]])
y_pred = train.predict(np.array([[6]]))
print(y_pred)