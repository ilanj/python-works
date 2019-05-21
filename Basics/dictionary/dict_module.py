class Student:
    def __init__(self):
        self.name="ila"
        self.id=36
        self.location="chennai"
        print(self.__module__)

obj=Student()
print(obj.__dict__)
print(obj.__module__)