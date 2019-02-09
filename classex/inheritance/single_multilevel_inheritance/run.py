from classex.inheritance.single_multilevel_inheritance.calcube import CalCube
from classex.inheritance.single_multilevel_inheritance.calsqr import Calculate


class Run(CalCube):
    name="i am in Run class"
    def __init__(self):
        print(" i am intialised in run class ")
        Calculate.__init__(self) # to initialize in parent classes
        CalCube.__init__(self)

    def powerfour(self,no):
         return no**4

r=Run()
print(r.powerfour(3))
print(r.cube(3))
print(r.square(3))
print(r.name)
