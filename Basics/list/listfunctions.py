ex=["apple","banana","carrot",1256,256.34]
print(ex)

def appendlist(e):
    ex.append(e)
    return ex
def clearlist():
    return ex.clear()
def countlist(e):
    return ex.count(e)
def extendlist(e):
    return ex.extend(e)
def indexlist(e):
    return ex.index(e)
def insertlist(index,e):
    return ex.insert(index,e)
def poplist(index):
    return ex.pop(index)
def removelist(e):
    return ex.remove(e)
def reverselist():
    return list(reversed(ex))
def sortlist():
    return list(sorted(ex))

print(reverselist())

