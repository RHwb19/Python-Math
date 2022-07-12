from matplotlib import pyplot

x_value_list = []
y_value_list = []


def make_graph(x_values, y_values):
    pyplot.plot(y_values, x_values, marker="*")
    pyplot.title("Quadratic Graph")
    return pyplot.show()


def x_values():
    start_value = input("Please enter the x-value to begin at: ")
    for i in range (0, 20):
        x_value_list.append(int(start_value) + 0.5 * i)
    return x_value_list


if __name__ == "__main__":
    x_1 = x_values()
    for x in x_1:
        y_value_list.append(x ** 2 + 2 * x + 1)
    make_graph(y_value_list, x_1)