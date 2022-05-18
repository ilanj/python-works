import random

<<<<<<< HEAD
nos1 = [1,4,2,67,9]

print(max(nos1))
print(min(nos1))
print(sum(nos1))

=======
>>>>>>> 7aea316fb7211c19240808b49e999c9f2e0561f2
nos=[]
rev=[]
sort=[]
for i in range(1,5):
    #nos.append(eval(input("enter any input")))
    nos.append(random.randint(10,99))
print(nos)
<<<<<<< HEAD
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
=======

rev=list(reversed(nos))
print(rev)
sort=list(sorted(nos))
print(sort)
>>>>>>> 7aea316fb7211c19240808b49e999c9f2e0561f2
