#name=str(input("enter string"))
name='python'
rev=''
for ch in range(len(name)):
    print(name[ch],name[len(name)-(ch+1)])
    rev=rev+name[len(name)-(ch+1)]
<<<<<<< HEAD
print('after reverse',rev)

for ch in range(len(name), 0, -1):
    print(name[ch-1])
=======
print('after reverse',rev)
>>>>>>> 7aea316fb7211c19240808b49e999c9f2e0561f2
