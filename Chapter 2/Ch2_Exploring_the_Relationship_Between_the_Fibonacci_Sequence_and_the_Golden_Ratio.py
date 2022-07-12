from matplotlib import pyplot
import math

x = []
y = []


def make_graph(x_list, y_list):
    pyplot.plot(x_list, y_list)
    pyplot.xlabel("No.")
    pyplot.ylabel("Ratio")
    pyplot.title("Ratio Between Consecutive Fibonacci Numbers")


def fibo(n):
    if n == 1:
        fibonacci_sequence = [1]
    elif n == 2:
        fibonacci_sequence = [1, 1]
    else:
        a = 1
        b = 1
        fibonacci_sequence = [a, b]
        for i in range(3, n):
            c = a + b
            fibonacci_sequence.append(c)
            a = b
            b = c
    return fibonacci_sequence[-1]


if __name__ == "__main__":
    try:
        number_of_iterations = int(input("Enter number of iterations: "))
    except ValueError:
        print("Input Invalid: Please restart program")
    else:
        for i in range(1, number_of_iterations):
            y.append(fibo(i + 1)/fibo(i))
            x.append(i)
        make_graph(x, y)
        pyplot.show()
