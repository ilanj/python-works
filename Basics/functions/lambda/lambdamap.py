nos=range(1,15)
even=list(map(lambda x:x%2==1,nos))

for i in even:
    print(i)

even=list(map(lambda x:x*2,nos))

for i in even:
    print(i)
