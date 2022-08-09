def create_classes(numbers, n):
    low = min(numbers)
    high = max(numbers)

    width = (high - low)/n
    a = low
    b = low + width
    classes = []
    while a < (high - width):
        classes.append((a, b))
        a = b
        b = a + width

    classes.append((a, high + 1))
    return classes


def read_file(filename):
    data_list = []
    with open(filename) as f:
        for line in f:
            data_list.append(float(line))
    return data_list


if __name__ == "__main__":
    file_name = input("Enter file name: ")
    class_name = input("Enter name of classes: ")
    number_of_classes = input("Enter number of classes: ")
    data = read_file(file_name)

    #class_name = "test"
    #number_of_classes = 5
    #data = [18, 12, 18, 11, 14, 19, 15, 19, 19, 19, 19, 16, 15, 18, 18, 12, 6, 10, 3, 2]

    data.sort()
    class_list = create_classes(data, number_of_classes)

    class_frequency_list = []

    for lower, higher in class_list:
        frequency = 0
        for element in data:
            if higher > element >= lower:
                frequency += 1
        class_frequency_list.append((lower, higher, frequency))

    print("{}\tFrequency".format(class_name))
    for lower_bound, upper_bound, freq in class_frequency_list:
        print("{:.2f}-{:.2f}\t{}".format(lower_bound, upper_bound, freq))