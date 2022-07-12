from matplotlib import pyplot

palo_alto_temperature = [63, 63, 62, 61, 61, 60, 60, 60, 62, 64, 67, 70, 73, 75, 77, 79, 79, 79, 78, 75, 71, 67, 65, 64]
pittsburgh_temperature = [77, 77, 76, 76, 76, 75, 74, 74, 75, 75, 76, 78, 80, 82, 83, 85, 86, 86, 85, 83, 81, 79, 77, 75]
local_time = []


def make_graph(x_1, x_2, y_1, y_2):
    pyplot.plot(y_1, x_1, y_2, x_2)
    pyplot.xlabel("Local Time")
    pyplot.ylabel("Temperature on 7/12 (F)")
    pyplot.title("Temperature Throughout 7/12")
    return pyplot.show()


if __name__ == "__main__":
    for i in range(0, 12):
        if i == 0:
            hour = 12
        else:
            hour = i
        local_time.append("{} AM".format(hour))
    for j in range(0, 12):
        if j == 0:
            hour = 12
        else:
            hour = j
        local_time.append("{} PM".format(hour))
    make_graph(palo_alto_temperature, pittsburgh_temperature, local_time, local_time)