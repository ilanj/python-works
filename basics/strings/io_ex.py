name="      haai welcome      "
print("entered name=",name)

length=len(name)
print("length of name=",length)
print(name.upper())
print(name.lower())
eachword=name.split(" ")
print(eachword)
name=name.replace(" ","")
print(name)
print(name.index("w"))
print(name.strip())
print(name.capitalize())
print(name.join("ABC"))

txtfile=open("G:\workspace\pythontutorial\print2console.txt")
txtfile=txtfile.read()
print(txtfile)
print(txtfile.splitlines())

print(txtfile.casefold())


