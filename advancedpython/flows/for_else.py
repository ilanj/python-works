items = [25,36,9]
divisor = 13

for item in items:
    if item % divisor == 0:
        found = item
        break
else:
    items.append(divisor)
    found = divisor

print(f"{items} contain {found} which is a multiple of {divisor}")
