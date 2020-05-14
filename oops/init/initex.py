#init is a initializer in python,
#in the following program, clearly InitEx() is the constructor and __init__ is the initializer
#you can only use, one init in a class.. u cannot overload init, eventhough it can take arguments
#if there are 2 init, init with argument will shadow default init
#in the following, first 3 are, shadowed by last init wirh 3 arguments, it means u cannot overload init and call them accordingly, because in this ex u
#are only allowed to call init with 3 args
class InitEx:
    def __init__(self):
        print(" this is a test and i am inside init")
    def __init__(self,a,b):
        print("i am first")
        self.a=a
        self.b=b
        print((self.a,self.b))
    def __init__(self,a,b):
        print("i am sec")
        self.a=a
        self.b=b
        print((self.a,self.b))
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        print((self.a,self.b,c))

InitEx(10,20,30)
#obj=InitEx()
#obj=InitEx()