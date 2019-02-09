try:
    print(25/3)
except OSError as e:
    print(e)

except Exception as e:
    print(e)
finally:
    print("this is finally")

print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")