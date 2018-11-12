import random

nos=[]
n=random.randint(5,10)
for i in range(n):
    nos.append(random.randint(10,20))
print(nos)

for n in nos:
    if n==15:
        continue
    print(n)
