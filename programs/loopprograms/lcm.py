# lcm
n1 = 45
n2 = 96
max_no = max(n1, n2)
temp = max_no
count = 2

while 1:
    if max_no % n1 is 0 and max_no % n2 is 0:
        lcm = max_no
        print(lcm)
        break
    max_no = temp * count
    count += 1
