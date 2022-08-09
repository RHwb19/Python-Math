from collections import Counter


def read_file(filename):
    data_list = []
    with open(filename) as f:
        for line in f:
            data_list.append(float(line))
    return data_list


if __name__ == "__main__":
    file_name = input("Enter File Name: ")
    data = read_file(file_name)
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