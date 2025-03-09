try:
    print(25 / 0)
except OSError as e:
    print("one", e)
except EnvironmentError as e:
    print("two", e)
except ZeroDivisionError as e:
    print("three", e)
except Exception as e:
    print("four", e)
finally:
    print(" this is finally")
