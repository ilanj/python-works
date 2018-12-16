from classex.__.base import Base


class Derived(Base):
    def print_values(self):
        a = "i am a"
        _b = "i am b"
        __c = "i am c"

obj=Derived()
print(" %s  %s  "%(obj.a,obj._b)) # and _b are overrided, but u cannot find
print(obj._Base__c)
print(dir(obj))
print(obj.print_values())
