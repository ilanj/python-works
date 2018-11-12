matrix=[(1,2,3),(4,5,6),(7,8,9)]
r2c=[[r[x] for r in matrix] for x in range(3)]
print(r2c)

for x in matrix:
    for each in x:
        print(each)

each_item=[[x for each in x]for x in matrix]
print(each_item)

each_item1=[[x for x in matrix]for each in x]
print(each_item1)