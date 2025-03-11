def recur_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n - 1)


# take input from the user
num = int(input("Enter a number: "))
print(recur_factorial(num))