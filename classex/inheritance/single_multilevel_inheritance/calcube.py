from classex.inheritance.single_multilevel_inheritance.calsqr import Calculate


class CalCube(Calculate):
    name="ila"
    def __init__(self):
        print("i am initialized in CalCube and calculating cube")

    def cube(self,n):
        return n**3;

c=CalCube()
print(c.cube(3))
print(c.square(3))
