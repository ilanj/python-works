a="normal variable"
_b="variable with a single under score"
__c="variable with a double underscore"
def factorial(n):
    fact=1;
    for i in range(1,n+1):
        fact=fact*i
    return fact

def fibonacci(n):
    print("this is fibonacci")
    fib=[]
    a,b=0,1
    for i in range(n):
        c=a
        a=b
        b=c+b
        fib.append(b)
    return fib

def _nesting():
    def nest1():
        print("i am nest 1")
    nest1()
    return "i am main nest"

