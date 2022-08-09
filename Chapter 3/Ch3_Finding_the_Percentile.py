def read_file(filename):
    data_list = []
    with open(filename) as f:
        for line in f:
            data_list.append(float(line))
    return data_list


if __name__ == "__main__":
    file_name = input("Enter File Name: ")
    data = read_file(file_name)
    data.sort()
    desired_percentage = int(input("Enter Desired Percentile: "))
    raw_value = len(data)*desired_percentage/100 + 0.5
    if raw_value.is_integer():
        percentile_value = data[raw_value]
    else:
        k = int(raw_value)
        f = raw_value - int(raw_value)
        percentile_value = (1-f)*data[k] + f*data[k+1]
    print("The Corresponding Value is: {}".format(percentile_value))
