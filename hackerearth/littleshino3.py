"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


a, b = map(int, input().split())

n = gcd(a, b)
ans = 0
for i in range(1, n):
    if n % i == 0:
        ans += 1
    if int(n**0.5) ** 2 == n:
        ans -= 1
print(ans + 1)
