from classex.inheritance.practice.a import *
from classex.inheritance.practice.b import BBase


class CDerived(BBase,ABase):
    def __init__(self):
        pass
        # print(self.balance())
        # print(self.interest)


obj=CDerived()
print(obj.balance())
print(obj.test)