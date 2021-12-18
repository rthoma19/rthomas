# I am going to write a program about classes

# types
# it will indicate the different types from the classes
# here are a few examples (checking the Python variable)

# <class 'int'>
print(type(5))

# <class 'float'>
print(type(6.3))

# <class 'str'>
print(type("Hello"))

my_list = []

my_dict = {}

# <class 'list'>
print(type(my_list))

# <class 'dict'>
print(type(my_dict))


# defining a class (use camelcase) (with class variables)
class MyClass:
    class_1 = "Mathematics"
    class_2 = "Computer Science"
    class_3 = "Science"
    class_4 = "Writing"
    class_5 = "Reading"
    class_6 = "Social Studies"

# Method with no arguments

    def favorite_class(self):
        return "My favorite class is mathematics."


# calling out the function outside of the class


fav_class = MyClass()
print(fav_class.favorite_class())


first_class = MyClass()
print(first_class.class_1)
print(first_class.class_2)
print(first_class.class_3)
print(first_class.class_4)
print(first_class.class_5)
print(first_class.class_6)

# Instantiation (must create an instance of a class, in order to breathe life into the schematic.)
# calling out the function

my_class_1 = MyClass()

# Object-Oriented Programming (OOP)
# Instantiation takes a class and turns it into an object
# main means "this current file that we're running"

print(type(my_class_1))

# constructors (method that is used to prepare an object being instantiated)


class Name:
    def __init__(self):
        print("Hello. My name is Ryan.")


name1 = Name()

# Instance Variables (data that can be held by an object)


class RollerCoaster:
    pass


gold_striker = RollerCoaster()

timber_twister = RollerCoaster()

giant_dipper = RollerCoaster()

gold_striker.coaster_name = "Gold Striker"

timber_twister.coaster_name = "Timber Twister"

giant_dipper.coaster_name = "Giant Dipper"

# joining the three strings together
working_list = "{} {} {}".format(gold_striker.coaster_name, timber_twister.coaster_name, giant_dipper.coaster_name)

print(working_list)
