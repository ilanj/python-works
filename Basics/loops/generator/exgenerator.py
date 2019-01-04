def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]#replace with rerurn and check
rev=''
ch=reverse("haai")
print("list=",(ch))

for each in list(ch):
    print(each)
    rev=rev+each
print("rev=",rev)
"""

h-0
a-1
a-2
i-3
"""