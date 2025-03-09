"""
Abstraction is an important aspect of object-oriented programming. In python, we can also perform data hiding by adding the double underscore (___)
as a prefix to the attribute which is to be hidden. After this, the attribute will not be visible outside of the class through the object.
"""


class One:
    __a = "a"
    b = "b"


obj = One()
print(obj._One__a)
