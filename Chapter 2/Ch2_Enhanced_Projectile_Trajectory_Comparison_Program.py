from matplotlib import pyplot
import math

input_list = []
speeds = []
angles = []
maximum_flight_data = []


def ask_for_inputs(trajectory_number):
    try:
        speed = float(input("Enter the initial velocity for trajectory (m/s) {}: ".format(trajectory_number)))
        angle = float(input("Enter the angle of projection for trajectory (degrees) {}: ".format(trajectory_number)))
    except ValueError:
        print("Input Invalid: Please restart program")
    else:
        return speed, angle


def make_graph(x_list, y_list):
    pyplot.plot(x_list, y_list)
    pyplot.xlabel("Distance (m)")
    pyplot.ylabel("Height (m)")
    pyplot.title("Projectile Trajectory Comparison")


def frange(start, finish, interval):
    numbers = []
    while start < finish:
        numbers.append(start)
        start += interval
    return numbers


def calculate_path(trajectory_speed, trajectory_angle):
    trajectory_angle = math.radians(trajectory_angle)
    g = 9.8
    x = []
    y = []

    total_flight_time = 2*trajectory_speed*math.sin(trajectory_angle)/g
    time_intervals = frange(0, total_flight_time, 0.001)

    for t in time_intervals:
        x.append(trajectory_speed*math.cos(trajectory_angle)*t)
        y.append(trajectory_speed*math.sin(trajectory_angle)*t - 0.5*g*t*t)

    make_graph(x, y)


if __name__ == "__main__":
    try:
        number_of_trajectories = int(input("Enter number of trajectories: "))
    except ValueError:
        print("Input Invalid: Please restart program")
    else:
        for i in range(1, number_of_trajectories + 1):
            traj_speed, traj_angle = ask_for_inputs(i)
            calculate_path(traj_speed, traj_angle)
            maximum_flight_data.append(2*traj_speed*math.sin(math.radians(traj_angle))/9.8)
            maximum_flight_data.append((traj_speed**2)*((math.sin(math.radians(traj_angle)))**2)/(2*9.8))
            maximum_flight_data.append((traj_speed ** 2) * ((math.sin(2 * math.radians(traj_angle)))) / 9.8)
        i = 0
        j = 1
        while i <= len(maximum_flight_data)//3 + 1:
            print("Trajectory {} Flight Time: {} s".format(j, maximum_flight_data[i]))
            print("Trajectory {} Maximum Vertical Distance: {} m".format(j, maximum_flight_data[i+1]))
            print("Trajectory {} Maximum Horizontal Distance: {} m".format(j, maximum_flight_data[i+2]))
            i += 3
            j += 1
        pyplot.show()
