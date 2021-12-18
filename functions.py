# Using different functions to write code and then call out the function when you run the code

train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1
c = 3*10**8

# Write your code below:
# Turn up the temperature


def f_to_c(f_temp):
    c_temp = (f_temp - 32) * (5/9)
    return c_temp


f100_in_celsius = f_to_c(100)

print(f100_in_celsius)


def c_to_f(c_temp):
    f_temp = c_temp * (9/5) + 32
    return f_temp


c0_in_fahrenheit = c_to_f(37.7)

print(c0_in_fahrenheit)

# Use the Force


def get_force(mass, acceleration):
    return mass * acceleration


train_force = get_force(train_mass, train_acceleration)

print("The GE train supplies " + str(train_force) + " Newtons of force.")


def get_energy(mass, c=3*10**8):
    return mass * c ** 2


bomb_energy = get_energy(bomb_mass, c)

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

# Do the Work


def get_work(mass, acceleration, distance):
    return mass * acceleration * distance


train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")

# I am going to write a program about my family vacation trip


def family_trip_planner(destination_1, destination_2, destination_3, destination_4):
    print("My family vacation starts at " + destination_1)
    print("Our next destination with my family vacation is " + destination_2)
    print("After " + destination_2 + " will be " + destination_3)
    print("Our final destination will be " + destination_4)


family_trip_planner("Yellowstone", "Badlands", "Grand Teton", "The Rocky Mountains")
