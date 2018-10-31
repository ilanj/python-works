import random
nos=[]
rev=[]
for i in range(1,5):
    #nos.append(eval(input("enter any input")))
    nos.append(random.randint(20,99))

len=len(nos)
print(nos)
print(nos[:])
print(len)
for i in range(0,len):
    print(nos[i])
print(nos[1:3])
print(nos)
nos.append(36)
print(nos)
addsum=sum(nos,10)
print(addsum)
print(sum(nos))
#print(nos.sort())
rev=reversed(nos)

for a in reversed(rev):
    print('after reverse',a)
for a in nos:
    print('without reverse',a)
