from collections import Counter
import csv

def read_csv(filename):
    diff_population = []
    with open(filename) as f:
        r_csv = csv.reader(f)
        next(r_csv)
        for row in r_csv:
            diff_population.append(int(row[1]) - int(row[0]))
    return diff_population


if __name__ == "__main__":
    file_name = input("Enter File Name: ")
    data = read_csv(file_name)
    sum_data = sum(data)

    #Mean
    mean_data = sum_data/len(data)

    #Median
    n = len(data)
    if n % 2 == 0:
        data.sort()
        median_data = (data[int(n/2 - 1)] + data[int(n/2)])/2
    else:
        median_data = data[int(n / 2)]

    #Mode
    mode = []
    counted_data = Counter(data)
    c = counted_data.most_common()
    for element, count in c:
        if count >= c[0][1]:
            mode.append(str(element))
        else:
            break
    mode_data = ", ".join(mode)

    #Variance
    mean_difference_squares = []
    for data_point in data:
        mean_difference_squares.append((data_point - mean_data)**2)
    variance_data = sum(mean_difference_squares)/n

    #Standard Deviation
    standard_deviation_data = variance_data**0.5

    #Printing
    information = [("mean_data", mean_data), ("median_data", median_data), ("mode_data", mode_data), ("variance_data", variance_data), ("standard_deviation_data", standard_deviation_data)]
    print("Measure\tValue")
    for name, value in information:
        print("{}\t{}".format(name, value))