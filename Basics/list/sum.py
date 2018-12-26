import random

nos=[]
rev=[]
sort=[]
for i in range(1,5):
    #nos.append(eval(input("enter any input")))
    nos.append(random.randint(10,99))
print(nos)

rev=list(reversed(nos))
print(rev)
sort=list(sorted(nos))
print(sort)