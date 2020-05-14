from advancedpython.switch.calc.arithematic_operations import divison, difference
from basics.functions.calculator import add, product

def calc(choice):
    # while choice:
        calculator = {
            "add": add(5, 6),
            "sub": difference(25, 5),
            "product":  product(5, 6),
            "division":  divison(55, 4)
        }
        try:
            result = calculator[choice]
            print(result)
        except KeyError:
            product(KeyError)

if __name__ == "__main__":
    choice = input("enter operation sum difference product division")
    calc(choice)

