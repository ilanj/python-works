from collections import namedtuple


class Student:

    def __init__(self, name, dob, location):
        self.name = name
        self.dob = dob
        self.location = location

    def checkdata(self):
        Student.__init__(self, 54, 88888, 87)
        print(self.name, self.dob, self.location)


obj = Student(3, 32, 23)
obj.checkdata()
