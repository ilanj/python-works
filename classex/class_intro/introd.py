class DemoClass:
    n=50

    def add(self):#substitutes the object here
        self.n=40
        print("inside add n= ",DemoClass.n)
n=100
o1=DemoClass()
o2=DemoClass()
o3=DemoClass()
o3.add()
o1.add()
# o1.n=60
# o2.n=70
# o3.n=80
print(o3.n)
print(o1.n)
print(DemoClass.n)
