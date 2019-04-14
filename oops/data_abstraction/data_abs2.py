class Employee:
    __count = 0;

    def __init__(self):
        Employee.__count = Employee.__count + 1

    def display(self):
        print("The number of employees", Employee.__count)


emp = Employee()
emp2 = Employee()
try:
    print(emp.__count)

except Exception as e:
    print(e)
finally:
    emp.display()