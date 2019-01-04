from abc import ABC,abstractmethod
class BaseEx(ABC):
    @abstractmethod
    def print_message(self):
        pass

class DerivedEx(BaseEx):
    def print_message(self):
        print(" i am in derived class")

obj=DerivedEx()
obj.print_message()