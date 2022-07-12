def enhanced_table_generator(factor, multiple_count):
    if factor.is_integer() and multiple_count.is_integer():
        for multiple in range(1, int(multiple_count) + 1):
            print("{} x {} = {}".format(int(factor), int(multiple), int(multiple * factor)))
    else:
        return "try again"


if __name__ == "__main__":
    status = "try again"
    while status == "try again":
        factor = float(input("Please enter the desired number: "))
        multiple_count = float(input("Please enter the number of multiples desired: "))
        status = enhanced_table_generator(factor, multiple_count)
