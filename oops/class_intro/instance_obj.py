class TestEx:
    def TestEx(self):
        print("just an ex")
        print(self.name)


obj = TestEx()
obj.name = "ila"
print(obj.name)


def checkname():
    print(obj.name)


checkname()
obj.TestEx()
