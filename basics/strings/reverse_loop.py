# name=str(input("enter string"))
name = "python"
rev = ""
for ch in range(len(name)):
    print(name[ch], name[len(name) - (ch + 1)])
    rev = rev + name[len(name) - (ch + 1)]
print("after reverse", rev)

for ch in range(len(name), 0, -1):
    print(name[ch - 1])
print("after reverse", rev)
