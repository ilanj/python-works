class Decorators:
    def __init__(self):
        ex=78
        print("decorators cotaining a initializer and 1.instance met 2.class met 3.static met")
    def instance_method(self,a,b):
        self.a=a
        self.b=b

        print(self.a,self.b)

    @classmethod
    def iamclassmethod(cls,x,y):
        cls.x=x
        cls.y=y
        print(cls.x,cls.y)
    @staticmethod#cannot take args like self and cls
    def iamstaticmethod():
        print("inside static",d.a)

        print("in static method, i dont have access to instances or class level")

    def print_instance_class_vars(cls):
        print(cls.x)
        print(d.b)
d=Decorators()
d.instance_method(20,35)
d.iamclassmethod(10,20)
d.iamstaticmethod()
d.print_instance_class_vars()

