def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]#replace with rerurn and check

for ch in reverse("haai"):
    print(ch)