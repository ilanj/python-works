import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

data=pd.read_csv('train_riyaz.csv')
data = data.as_matrix()

inputdata = data[:,0:40]
output = data[:,40]
X_train, X_test, y_train, y_test = train_test_split(inputdata, output, test_size=0.2, random_state=0)

models = []
models.append(('LinearRegression', LinearRegression()))
models.append(('LogisticRegression', LogisticRegression()))
models.append(('KNeighborsClassifier', KNeighborsClassifier()))
models.append(('DecisionTreeClassifier', DecisionTreeClassifier()))
models.append(('GaussianNB', GaussianNB()))
models.append(('SVC', SVC()))


# Loop through models and identify the best model to predict square
for name, model in models:
    model.fit(X_train, y_train)
    predict=model.predict(acc)
print()