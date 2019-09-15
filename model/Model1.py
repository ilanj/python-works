import random
import string

list_model= []
class Employee():
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def is_old(self):
        for i in range(10):
            self.name= ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
            self.age= ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
            self.major= ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
            obj=Employee(self.name, self.age, self.age)
            list_model.append(obj)
            print(self.__dict__)

run= Employee("ila",28,'python')
run.is_old()