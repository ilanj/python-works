# implemented without decorator, with decor is available at with_decorator.py

def struper(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner


def printstr():
    return "hi welcome! "

obj = struper(printstr)
print(obj())