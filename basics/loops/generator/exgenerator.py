def reverse(data):
<<<<<<< HEAD
    for index in range(len(data)-1,-1,-1): # to iterate till 0th char in reverse, we use -1 as its exclusive
=======
    for index in range(len(data)-1,-1,-1): # to iterate eill 0th char in reverse, we use -1 as its exclusive
>>>>>>> 7aea316fb7211c19240808b49e999c9f2e0561f2
        yield data[index]#replace with rerurn and check
rev=''
ch=reverse("haai")
print("list=",list(ch))

for each in reverse("haai"):
    print(each)
    rev=rev+each
print("rev=",rev)
"""

h-0
a-1
a-2
i-3
"""
