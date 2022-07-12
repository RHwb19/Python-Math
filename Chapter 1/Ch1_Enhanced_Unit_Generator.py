# Pounds to Kilograms and Celsius to Fahrenheit
def pounds_to_kilos(p_amount):
    k_amount = p_amount * 0.455
    return k_amount


def kilos_to_pounds(k_amount):
    p_amount = k_amount / 0.455
    return p_amount


def c_to_f(c_amount):
    f_amount = c_amount * 1.8 + 32
    return f_amount


def f_to_c(f_amount):
    c_amount = 5 * (f_amount - 32) / 9
    return f_amount


def print_options():

    print("Options")
    print("1. Pounds to Kilos")
    print("2. Kilos to Pounds")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    output = input("Please choose an option: ")
    return int(output)


if __name__ == "__main__":
    status = "try again"
    while status == "try again":
        option_number = print_options()
        if option_number == 1:
            kilos = pounds_to_kilos(int(input("Pounds: ")))
            print("Kilograms: {:.2f}".format(kilos))
            status = ""
        elif option_number == 2:
            pounds = kilos_to_pounds(int(input("Kilos: ")))
            print("Pounds: {:.2f}".format(pounds))
            status = ""
        elif option_number == 3:
            fahrenheit = c_to_f(int(input("Celsius: ")))
            print("Fahrenheit: {:.2f}".format(fahrenheit))
            status = ""
        elif option_number == 4:
            celsius = f_to_c(int(input("Fahrenheit: ")))
            print("Celsius: {:.2f}".format(celsius))
            status = ""
        else:
            print("Error: Option not available")

