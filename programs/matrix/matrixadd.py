matrixa = []
for i in range(0,3):
    matrixa.append([])
    for j in range(0,3):
        temp=int(input("enter a"))
        matrixa[i].append(temp)
print(matrixa)

matrixb = [[int(input("enter no")) for i in range(3)] for j in range(3)]
print(matrixb)

result=[[0 for i in range(3)] for j in range(3)]

for i in range(len(matrixa)):
    for j in range(len(matrixa[0])):
        result[i][j]=matrixa[i][j]+matrixb[i][j]

print(result)
