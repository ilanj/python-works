class Dog:
    tricks = []             # mistaken use of a class variable
    def __init__(self, name):
        self.name = name

    def add_trick(self, *trick):
        self.tricks.append(trick)
d=Dog("haai")
d.add_trick("hajaj","dded","feff")
print(d.tricks)