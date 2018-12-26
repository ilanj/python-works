nos=(1,2,3,4,5,5,4,5,6)
print(nos)

if 4 in nos:
    print("4 is present")
else:
    print("4 in not present")

print(nos.count(4))
print(sum(nos))
print(tuple(reversed(nos)))
print(tuple(sorted(nos)))
print("size=",len(nos))

sq=tuple(x**2 for x in nos if x%2==0)#for comprehension in tuples use () instead of []
print(sq)