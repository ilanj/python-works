# Use Broadcasting to create a 4 x 4 ndarray that has its first
# column full of 1s, its second column full of 2s, its third
# column full of 3s, etc..
import numpy as np

x=np.ones((4,4))
y=np.array([1,2,3,4])
y1=np.array([[1],[2],[3],[4]])
print(x*y)
print(x*y1)

print(np.ones((4,4)) * np.arange(1,5))
