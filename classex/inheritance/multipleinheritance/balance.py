from classex.inheritance.multipleinheritance.banka import BankA
from classex.inheritance.multipleinheritance.bankb import BankB


class Balance(BankA,BankB): #in both parents interest is present as instance variable, so class name mentioned first will shadow other classes. here interest from classb is taken
    def __init__(self):
        print(" i am from Derived")
        BankB.__init__(self)#this is initialized last
        BankA.__init__(self)




    def calculate_balance(self):
        print(self.balancea+self.balanceb)
        return self.balance_a()+self.balance_b()

b=Balance()
print(b.interest)#based on value initialized last, interest will be displayed
print("test=",b.test)
print(b.calculate_balance())
print(b.balancea+b.balanceb)
