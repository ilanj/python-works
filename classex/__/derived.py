from classex.__.base import Base


class Derived(Base):
    a = "i am a"
    _b = "i am b"
    __c = "i am c"
    def print_values(self):
      print()

obj=Derived()
print(" %s  %s  "%(obj.a,obj._b)) # and _b are overrided, but u cannot find
print(obj._Base__c)
print(obj._Derived__c)# this is the usage of double undercore
print(dir(obj))
print(obj.print_values())

obj.x=15
