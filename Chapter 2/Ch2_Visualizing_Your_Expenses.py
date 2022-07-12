from matplotlib import pyplot
import math

categories = []
expenditures = []


def ask_for_inputs(category_number):
    try:
        category = input("Enter the name of Category {}: ".format(category_number))
        expenditure = float(input("Enter the amount spent: "))
    except ValueError:
        print("Input Invalid: Please restart program")
    else:
        return category, expenditure


def make_graph(data_list, category_list):
    positions = range(1, len(data_list) + 1)
    pyplot.barh(positions, data_list, align="center")
    pyplot.yticks(positions, category_list)
    pyplot.xlabel("Expenditure ($)")
    pyplot.ylabel("Expenditure Category")
    pyplot.title("Weekly Expenditure")
    pyplot.grid()


if __name__ == "__main__":
    try:
        number_of_categories = int(input("Enter number of categories: "))
    except ValueError:
        print("Input Invalid: Please restart program")
    else:
        for i in range(1, number_of_categories + 1):
            category_name, expenditure_amount = ask_for_inputs(i)
            categories.append(category_name)
            expenditures.append(expenditure_amount)
        make_graph(expenditures, categories)
        pyplot.show()
