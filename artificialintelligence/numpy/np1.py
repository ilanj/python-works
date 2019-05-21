import numpy as np

x = np.array([1, 2, 3, 4, 5])

print(x)

type(x)

x.dtype

x.shape

y = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(y)
y.shape

y.size

str = np.array(['hi', 'welcome'])
print(str)

str.dtype

nos = np.array([1, 2, 'hi'])
print(nos.dtype)

mixed_nos = np.array([1, 2, 3.4534, 3.3333])
mixed_nos.dtype

mixed_nos1 = np.array([1, 2, 3.4534, 3.3333], dtype=np.int64)
mixed_nos1.dtype

temp = np.array([9, 8, 7, 6])
np.save('newarray', temp)

myarray = np.load('newarray.npy')
print(myarray)
