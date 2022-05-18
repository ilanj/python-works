import numpy as np

nos=np.arange(1,21).reshape(4,5)
print(nos)

nos1=nos[1:4,1:3]
print(nos1)

nos1[1][1]=111
print(nos)

n=np.arange(1,21).reshape(4,5)
n1=n[1:4,1:3].copy()
n1[1][1]=23432
print(n1)
print(n)#now change in n1 will not refflect n

indices=np.array([1,3])
print(indices)
y=n[indices,:]
print(y)

x=n[:,indices]
print(x)

print(np.diag(n,k=2))#k arg is optional
print(np.unique(n))
