from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

import pandas as pd
import numpy as np

data = np.asarray(pd.read_csv('dectree_data.txt', header=None, sep=','))
X = data[:, 0:2]
y = data[:, 2]

model = DecisionTreeClassifier()
model.fit(X, y)
# y_pred = model.predict(np.array([[2.0,2.1]]))
y_pred = model.predict(X)

# TODO: Calculate the accuracy and assign it to the variable acc.
acc = accuracy_score(y, y_pred)
print(y_pred)
print(acc)
