class Test:
    a=10
    _b=20
    __c=30
    def name(self):
        print("name ")

    def _name1(self):
        print(" name1")

    def __name1(self):
        print(" name2")
a=100
o=Test()
print(dir(o))#to check mangling
print(o._Test__c)# mangling