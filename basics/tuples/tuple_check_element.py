nos=(1,2,3,4,5,5,4,5,6)
print(nos)
print(nos[0])

if 4 in nos:
    print("4 is present")
else:
    print("4 in not present")

print("count of 4 = ",nos.count(4))
print("sum = ",sum(nos))
<<<<<<< HEAD
print("descending order ",tuple(reversed(nos))) #returned as list, so typecasting as tuple
print("ascending order ",sorted(nos))
print("ascending order ",(sorted(nos, reverse=True)))
=======
print("descending order ",tuple(reversed(nos)))
print("ascending order ",list(sorted(nos)))
>>>>>>> 7aea316fb7211c19240808b49e999c9f2e0561f2
print("size=",len(nos))

sq=tuple(x**2 for x in nos if x%2==0)#for comprehension in tuples use () instead of []
print(sq)