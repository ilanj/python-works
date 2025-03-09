import numpy as np

nos = np.arange(25).reshape(5, 5)
print(nos)

print(nos | nos > 20)

print(nos[nos > 20])
print(nos[(nos > 20) | (nos < 15)])

x = np.array([1, 2, 3, 4, 5])
y = np.array([6, 7, 8, 2, 4])

print(np.intersect1d(x, y))
print(np.setdiff1d(x, y))
print(np.union1d(x, y))

x = np.random.randint(1, 11, size=(10))
print(x)
print(np.sort(x))
print(x)

print(x)
x.sort()
print(x)

print(np.unique(x))

x1 = np.random.randint(2, 22, size=(5, 5))
print(x1)

print(np.sort(x1, axis=0))
print(np.sort(x1, axis=1))
