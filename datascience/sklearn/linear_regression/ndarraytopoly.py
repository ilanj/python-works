import numpy as np
from sklearn.preprocessing import PolynomialFeatures


nos=np.arange(20).reshape(20,1)
print(nos)

to_poly=PolynomialFeatures(degree=4)
nos_poly=to_poly.fit_transform(nos)
print()