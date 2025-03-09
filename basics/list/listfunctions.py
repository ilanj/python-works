ex = ["apple", "banana", "carrot", 1256, 256.34]
print(ex)


def appendlist(e):
    ex.append(e)
    print(ex)
    return ex


def clearlist():
    return ex.clear()


def countlist(e):
    return ex.count(e)


def extendlist(e):
    return ex.extend(e)


def indexlist(e):
    return ex.index(e)


def insertlist(index, e):
    return ex.insert(index, e)


def poplist(index):
    return ex.pop(index)


def removelist(e):
    return ex.remove(e)


def reverselist():
    return list(reversed(ex))


def sortlist():
    return list(sorted(ex))


ex1 = [34, 56, 76]
print(extendlist(ex1))

print(ex.extend(ex1))


def switcher_try(argumet):
    switcher = {"0": appendlist(argumet), "1": countlist(argumet)}
    return print(switcher.get(argument))


if __name__ == "__main__":
    argument = 0
    switcher_try(argument)
