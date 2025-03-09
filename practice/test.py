nos = [1, -1, 3, 4, 8, 7, 2]
possitive_nos = list()
for itr, n in enumerate(nos):
    if n > 0:
        possitive_nos.append(n)

possitive_nos = sorted(possitive_nos)
for itr, n in enumerate(possitive_nos, start=1):
    if itr not in possitive_nos:
        print(itr)
        break
