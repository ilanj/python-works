class C:
    _x=25
    @property
    def getx(self):
        """I'm the 'x' property."""
        return self._x

    @getx.setter
    def setx(self, value):
        self._x = value
        print(self._x)


    # @x.deleter
    # def x(self):
    #     del self._x

c=C()

c.setx="ddvdvdvdcvd"
print(c.getx)