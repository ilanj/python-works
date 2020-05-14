#predict survival based on other features
#these are survivors of titanic
import pandas as pd
data=pd.read_csv('/home/ila/PycharmProjects/pythonworks/artificialintelligence/pandas/files/kaggletrain.txt')
print(data.head())
feature_cols=['Pclass','Parch']#Passesnger class, parents and children

x=data.loc[:,feature_cols]#selecting all rows and feature columns
print(x.shape)

y=data.Survived
print(y.shape)

#scikit learn
from sklearn.linear_model import LogisticRegression
logreg=LogisticRegression()
logreg.fit(x,y)

test_predict=pd.read_csv("/home/ila/PycharmProjects/pythonworks/artificialintelligence/pandas/files/kaggletest.txt")#no survival comumns
print(test_predict.head())
x_test=test_predict.loc[:,feature_cols]
print(x_test.head())

new_pred_class=logreg.predict(x_test)
print(new_pred_class)

pd.DataFrame({'PassengerId':test_predict.PassengerId,'Survived':new_pred_class}).set_index('PassengerId').to_csv('kagglepredict.csv')

#save df to disk with pickle
data.to_pickle('test_titanic_pickle.pkl')
temp=pd.read_pickle('test_titanic_pickle.pkl')
print(temp)
