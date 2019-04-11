import numpy as np
import pandas as pd
from sklearn.linear_model import Lasso

# Assign the data to predictor and outcome variables
# TODO: Load the data
train_data = pd.read_csv('G:\workspace\pythontutorial\datascience\linear_regression\input.txt',header = None)
X = train_data.iloc[:,:-1]
print(X.shape)
y = train_data.iloc[:,-1]

# TODO: Create the linear regression model with lasso regularization.
lasso_reg = Lasso()

# TODO: Fit the model.
lasso_reg.fit(X, y)

# TODO: Retrieve and print out the coefficients from the regression model.
reg_coef = lasso_reg.coef_
print(reg_coef)

print(X.shape)
print(type(reg_coef))
# reg_coef.reshape(-1,1)
print(reg_coef.shape)
prediction=lasso_reg.predict(np.array([[1.2,2,-6.2,4.7,-4,0.2,]]))
print()