import numpy as np

x=np.random.randint(1,11,size=(10,))
print(x)

print(np.sort(x))
print(x)#this sorting did not affect original x

x.sort()
print(x)#now x is also affected

twod=np.random.randint(1,99,size=(3,3))
print(twod)
print(np.sort(twod,axis=1))
print(np.sort(twod,axis=0))

