class Intro:

    no = 100

    def a(self):
        no = 150
        print(no)

    def b(self):
        no = 200
        self.no = 250
        print(Intro.no)
        print(self.no)
        print(no)


obj = Intro()
obj.b()
print(obj.no)
print(obj.getname())
