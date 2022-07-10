from fractions import Fraction

def add(Fraction_1, Fraction_2):
    return "Result of addition: {}".format(Fraction_1 + Fraction_2)


def subtract(Fraction_1, Fraction_2):
    return "Result of subtraction: {}".format(Fraction_1 - Fraction_2)


def multiply(Fraction_1, Fraction_2):
    return "Result of multiplication: {}".format(Fraction_1 * Fraction_2)


def divide(Fraction_1, Fraction_2):
    return "Result of division: {}".format(Fraction_1 / Fraction_2)


def options_menu():
    print("Fraction Calculator")
    fraction_1 = Fraction(input("Enter first fraction: "))
    fraction_2 = Fraction(input("Enter second fraction: "))
    operation = input("Choose operation -- Add, Subtract, Multiply, Divide: ")
    return fraction_1, fraction_2, operation


if __name__ == "__main__":
    status = "try again"
    while status == "try again":
        fract_1, fract_2, op = options_menu()
        if op == "Add":
            print(add(fract_1, fract_2))
            status = ""
        elif op == "Subtract":
            print(subtract(fract_1, fract_2))
            status = ""
        elif op == "Multiply":
            print(multiply(fract_1, fract_2))
            status = ""
        elif op == "Divide":
            print(divide(fract_1, fract_2))
            status = ""
        else:
            status = "try again"
            print("Error: Please choose another operation")
