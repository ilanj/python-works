from oops.__.base import Base


class Derived(Base):
    a = "i am derived a"
    _b = "i am derived b"
    __c = "i am derived c"
    def print_values(self):
      print()

obj=Derived()
print(" %s  %s  "%(obj.a,obj._b)) # and _b are overrided, but u cannot find

print(dir(obj))
print(obj._Derived__c)
print(obj._Base__c)