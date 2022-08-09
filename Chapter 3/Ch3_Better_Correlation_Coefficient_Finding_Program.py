

def find_corr_x_y(x,y):

    if len(x) == len(y):
        n = len(x)

        prod = []
        x_square = []
        y_square = []

        for xi, yi in zip(x,y):
            prod.append(xi*yi)
            x_square.append(xi ** 2)
            y_square.append(yi ** 2)
        x_square_sum = sum(x_square)
        y_square_sum = sum(y_square)

        sum_prod_x_y = sum(prod)
        sum_x = sum(x)
        sum_y = sum(y)
        squared_sum_x = sum_x**2
        squared_sum_y = sum_y**2

        numerator = n*sum_prod_x_y - sum_x*sum_y
        denominator_term1 = n*x_square_sum - squared_sum_x
        denominator_term2 = n*y_square_sum - squared_sum_y
        denominator = (denominator_term1*denominator_term2)**0.5
        correlation = numerator / denominator
    else:
        correlation = False

    return correlation

if __name__ == "__main__":
    x = []
    y = []
    result = find_corr_x_y(x,y)
    if result:
        print result
    else:
        print("List length is not equal, correlation cannot be calculated")
