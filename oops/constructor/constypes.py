class Constypes:

    def __init__(self, name):
        print(" i am init executed")
        print("haai ", name)

    def test(self, name):
        print(" i am test ")
        print("haai ", name)

    print(" i am outside clas and executed")


c = Constypes("welcome")
c.test("hajara")
