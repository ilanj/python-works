# without parameter

def struper(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner

@struper
def printstr():
    return "hi welcome! "

print(printstr())