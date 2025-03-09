n = int(input())
res = []
text = []
for itr in range(n):
    str = input()
    text.append(str)
q = int(input())
l = []
r = []
search = []
for each in range(q):
    line = input()
    words = line.split(" ")
    left = int(words[0])
    l.append(left)
    right = int(words[1])
    r.append(right)
    str = words[2]
    search.append(str)

for itr, each in enumerate(l):
    ans = 0
    for str in range(l[itr], r[itr] + 1):
        if search[itr] == text[str - 1]:
            ans = ans + 1
    res.append(ans)

for each in res:
    print(each)
