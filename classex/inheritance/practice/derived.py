from classex.inheritance.practice.a import *
from classex.inheritance.practice.b import BBase


class CDerived(BBase,ABase):
    def __init__(self):
        print(self.balance())
        print(self.interest)


obj=CDerived()
print(obj.balance())
print(obj._test)