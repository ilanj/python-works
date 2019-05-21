def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


a, b = map(int, input().split())

n = gcd(a, b)
ans = 0
for i in range(1, int(n ** .5) + 1):
    if n % i == 0:
        ans += 2
if int(n ** .5) ** 2 == n:
    ans -= 1
print(ans)