class Student:
    def __init__(self):
        self.name = "ila"
        self.id = 36
        self.location = "chennai"
        # print(self.__module__)


std = Student()
print(std.name)
print(std.__dict__)
# print(obj.__module__)
