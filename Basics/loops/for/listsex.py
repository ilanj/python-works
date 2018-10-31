words=['apple','banana','carrot','diary']
for x in words:
    print(x,len(x))
for x in words[:]:
    if x.__eq__("banana"):
        words.remove(x)
print('after remove',words)

for x in words:
    if x.__eq__("banana"):
        words.remove(x)
print('after remove',words)

for i in range (len(words)):
    print(i,words[i])
