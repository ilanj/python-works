import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Assign the data to predictor and outcome variables
# TODO: Load the data
train_data = pd.read_csv('G:\workspace\pythontutorial\datascience\linear_regression\polydata.txt')
X = train_data['Var_X']
print(X.shape,X)
print(type(X))
X = train_data['Var_X'].values.reshape(-1, 1)
print(X.shape,X)
print(type(X))

y = train_data['Var_Y'].values
print(X.shape)
# Create polynomial features
# TODO: Create a PolynomialFeatures object, then fit and transform the
# predictor feature
poly_feat = PolynomialFeatures(degree = 4)#to understand this line refer ndarraytopoly.py
X_poly = poly_feat.fit_transform(X)
print(X_poly.shape)

# Make and fit the polynomial regression model
# TODO: Create a LinearRegression object and fit it to the polynomial predictor
# features
poly_model = LinearRegression(fit_intercept = False).fit(X_poly, y)
print(type(poly_model))
prediction=poly_model.predict(np.array([[3.45,4,5,6,5]]))
print(prediction)