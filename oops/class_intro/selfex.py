class Ex:
    a=None
    def custom_print(self,x):
        self.x=x*2
        self.b=67
        self._x=77
        self.__y=87
        print(self.b)
        print(x)
        print(self.x)
        print(o1.b)


o1=Ex()
o1.custom_print(10)
# print(o1.x)
#
# o2=Ex()
# o2.x="kjvbkvbv"
# print(o2.x)