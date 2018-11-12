from collections import deque

nos=deque([1,2,3,4])
print(nos)


nos.append(5)
nos.append(6)
print(nos)

nos.popleft()
print(nos)

