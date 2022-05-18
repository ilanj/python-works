import random

nos1 = [1,4,2,67,9]

print(max(nos1))
print(min(nos1))
print(sum(nos1))

nos=[]
rev=[]
sort=[]
for i in range(1,5):
    #nos.append(eval(input("enter any input")))
    nos.append(random.randint(10,99))
print(nos)
nos.sort()
print(nos)

nos.sort(reverse= True)
print(nos)

# list-append-insertion order maintained
# set-add- insertion order not maintained
n = set()
n.add("one")
n.add("two")
n.add("three")
print(n)
