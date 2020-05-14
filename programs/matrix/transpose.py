matrixa = [[int(input("enter no")) for i in range(3)] for j in range(3)]
matrixb = [[0 for i in range(3)] for j in range(3)]

print(matrixa)

for i in range(len(matrixa)):
    for j in range(len(matrixa[0])):
        matrixb[j][i]=matrixa[i][j]
print(matrixb)


