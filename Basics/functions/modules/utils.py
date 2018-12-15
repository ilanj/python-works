def factorial(n):
    fact=1;
    for i in range(1,n+1):
        fact=fact*i
    return fact

def fibonacci(n):
    fib=[]
    a,b=0,1
    for i in range(n):
        c=a
        a=b
        b=c+b
        fib.append(b)
    return fib
