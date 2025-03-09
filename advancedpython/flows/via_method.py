# better approach than for_else.py
def ensure_has_divisible(items, divisor):
    for item in items:
        if item % divisor == 0:
            # found = item
            # break
            # alternative to break
            return item
        items.append(divisor)
        return divisor


items = [2, 25, 9]
divisor = 12
dividend = ensure_has_divisible(items, divisor)
print(f"{items} contain {dividend} which is a multiple of {divisor}")
