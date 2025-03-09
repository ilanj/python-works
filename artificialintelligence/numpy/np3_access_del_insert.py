import numpy as np

x = np.array([1, 2, 3, 4, 5])
print(x)

print(x[0], x[1], x[2], x[3], x[4])
print(x[-1], x[-2], x[-3], x[-4], x[-5])

x[3] = 65
print(x)

x = np.arange(1, 10).reshape(3, 3)
x[0][0] = 11
x[1][1] = 22
x[2][2] = 33
print(x)

oned = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
oned = np.delete(oned, [0, 9])
print(oned)

y = np.arange(1, 10).reshape(3, 3)
print(y)
y1 = np.delete(y, 0, axis=1)  # y axis, column 0 is removed
print(y1)

y2 = np.delete(y, 0, axis=0)  # x axis
print(y2)

y3 = np.delete(y, [0, 1], axis=0)  # x axis
print(y3)

print(oned)
oned = np.append(oned, [34, 32])
print(oned)
oned = np.insert(oned, 2, [34, 32])
print(oned)


twod = np.arange(1, 10).reshape(3, 3)
print(twod)
twod = np.append(twod, [[23, 45, 65]], axis=0)
print(twod)
twod = np.insert(twod, 1, [[12, 32, 45]], axis=0)
print(twod)

twod = np.append(twod, [[45], [34], [23], [12], [23]], axis=1)
print(twod)
twod = np.insert(twod, 2, 87, axis=1)
print(twod)

a = np.array([1, 2, 3])
b = np.array([[4, 3, 5], [5, 3, 5]])
c = np.vstack((a, b))
print(c)


# x=np.delete(x,[(1,1),{1,2}])
