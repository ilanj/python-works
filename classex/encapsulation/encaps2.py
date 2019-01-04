class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        print(self._x)


    @x.deleter
    def x(self):
        del self._x

c=C()
c.x="ddvdvdvdcvd"
print(c.x)