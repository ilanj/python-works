# 153 is an Armstrong number since 153 = 1*1*1 + 5*5*5 + 3*3*3.

n = int(input("enter any no"))
length = len(str(n))
check_n = n
armstrong = 0
while n != 0:
    rem = n % 10
    n = n // 10
    armstrong = armstrong + (rem**length)
if check_n is armstrong:
    print("armstrong no")
else:
    print(" not an armstrong no")
