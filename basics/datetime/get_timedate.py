import time

start = time.strftime("%X")
print(time.strftime("%x %X"))
print(time.strftime("%X"))
time.sleep(1)
end = time.strftime("%X")

# print(start - end) this wont work as both are str
