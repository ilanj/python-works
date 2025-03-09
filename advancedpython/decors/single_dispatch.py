""" demo for single instance which can also be called as
polymorphism/ method overloading-
5 May 2020 ilanchezhian619@gmail.com"""

from functools import singledispatch


class Circle:

    def __init__(self, r):
        self.r = r


class Rect:

    def __init__(self, l, b):
        self.l = l
        self.b = b


@singledispatch
def calc_area(params_req):
    raise TypeError("Don't know how to draw ")


@calc_area.register(Circle)
def _(params_req):
    print(3.14 * params_req.r * params_req.r)


@calc_area.register(Rect)
def _(params_req):
    print(params_req.l * params_req.b)


def main():
    params = [Circle(5.6), Rect(24, 32)]

    for param in params:
        calc_area(param)


if __name__ == "__main__":
    main()
