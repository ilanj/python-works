class Scope:
    name=""
    def __init__(self):#only inside a class
        print("inside init")
    def check(self,n1):
        obj.x="i am jkjk"
        print(self.x)
        n=20
        name=n1
        print(n1)

        def print_nest():
            print("i am nest")
        print_nest()
    print("i am just inside class")


obj=Scope()
obj.check("hgf")
print(obj.name)

