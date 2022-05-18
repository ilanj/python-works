try:
<<<<<<< HEAD
    print(25/0)
except OSError as e:
    print("one", e)

except EnvironmentError as e:
    print("two", e)
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print("three", e)

finally:
    print("this is finally")
=======
    print(25/3)
except OSError as e:
    print(e)

except EnvironmentError as e:
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
>>>>>>> 7aea316fb7211c19240808b49e999c9f2e0561f2
