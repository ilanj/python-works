class DemoClass:
    n=50

    def add(self):#substitutes the object here
        self.n=40
<<<<<<< HEAD
        print("inside add n= ",o1.n)
=======
        print("inside add n= ",DemoClass.n)
>>>>>>> 7aea316fb7211c19240808b49e999c9f2e0561f2
n=100
o1=DemoClass()
o2=DemoClass()
o3=DemoClass()
<<<<<<< HEAD
o1.add()
o3.add()
=======
o3.add()
o1.add()
>>>>>>> 7aea316fb7211c19240808b49e999c9f2e0561f2
# o1.n=60
# o2.n=70
# o3.n=80
print(o3.n)
print(o1.n)
print(DemoClass.n)
