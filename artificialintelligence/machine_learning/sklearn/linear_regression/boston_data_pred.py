from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
import numpy as np

boston_data=load_boston()

x=boston_data['data']
y=boston_data['target']
print(x.shape)
print(y.shape)
model=LinearRegression()
model.fit(x,y)
sample_house = [[2.29690000e-01, 0.00000000e+00, 1.05900000e+01, 0.00000000e+00, 4.89000000e-01,
                6.32600000e+00, 5.25000000e+01, 4.35490000e+00, 4.00000000e+00, 2.77000000e+02,
                1.86000000e+01, 3.94870000e+02, 1.09700000e+01]]
prediction=model.predict(sample_house)
print(prediction)

print(type(x))
print(type(y))
print(type(boston_data))
print(y)