def vending_machine(input_number):
    if input_number > 0 and input_number.is_integer():
        numb_list = []
        if input_number % 2 == 1:
            for factor in range(1, 10):
                numb_list.append(str(int(input_number) + factor * 2))
            return print(", ".join(numb_list))
        if input_number % 2 == 0:
            for factor in range(1, 10):
                numb_list.append(str(int(input_number) + factor * 2))
            return print(", ".join(numb_list))
    return "try again"


if __name__ == "__main__":
    status = "try again"
    while status == "try again":
        user_number = input("Please enter a positive integer: ")
        status = vending_machine(float(user_number))