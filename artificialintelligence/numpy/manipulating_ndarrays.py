import numpy as np
x=np.arange(1,26).reshape(5,5)
print(x)
print(x[x%2 == 1])