# a instance d created below, can access both class and instance data, where a class can access only class data.
class Dog:
    kind = "canine"  # class variable shared by all instances

    def __init__(self, name):
        self.name = name  # instance variable unique to each instance


d = Dog("Fido")
print(d.kind)
print(d.name)
