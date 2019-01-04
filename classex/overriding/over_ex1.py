class Animal:
    def speak(self):
        print("speaking")


class Dog(Animal):
    def speak(self):
        print("Barking")


d = Dog()
d.speak()  