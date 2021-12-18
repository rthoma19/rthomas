# I am doing to write a program about a list of my favorite fruits

favorite_fruits = ["bananas", "apples", "avocado", "watermelon", "grapes", "blueberries", "strawberries"]

# ['bananas', 'apples', 'avocado', 'watermelon', 'grapes', 'blueberries', 'strawberries']
print(favorite_fruits)

# will print out bananas, apples (does not include avocado) (slicing)
print(favorite_fruits[0:2])

# using the append method to add more elements to my favorite fruits list
favorite_fruits.append("peppers")

favorite_fruits.append("cantaloupe")

favorite_fruits.append("raspberries")

# bananas, apples, avocado, watermelon, grapes, blueberries, strawberries, peppers, cantaloupe, raspberries
print(favorite_fruits)

# using the insert method to add a new element at a certain place

favorite_fruits.insert(3, "honeydew")

favorite_fruits.insert(5, "pineapple")

# bananas, apples, avocado, honeydew, watermelon, pineapple, grapes, blueberries, strawberries, peppers, cantaloupe,
# raspberries
print(favorite_fruits)

# using the remove method to remove elements to my favorite fruits list
favorite_fruits.remove("apples")

favorite_fruits.remove("watermelon")

# bananas, avocado, honeydew, pineapple, grapes, blueberries, strawberries, peppers, cantaloupe, raspberries
print(favorite_fruits)

# printing out a single index to my favorite fruits list
print(favorite_fruits[0])

print(favorite_fruits[-1])

# modifying my favorite fruits list with a different element

favorite_fruits[3] = "peaches"

favorite_fruits[-1] = "pears"

# bananas, avocado, honeydew, peaches, grapes, blueberries, strawberries, peppers, cantaloupe, pears
print(favorite_fruits)

# using the insert method with lists
favorite_fruits.insert(0, "blackberries")

# blackberries, bananas, avocado, honeydew, peaches, grapes, blueberries, strawberries, peppers, cantaloupe, pears
print(favorite_fruits)

# Doing a 2D list of other peoples favorite fruits
fruits = [["Michelle", "bananas"], ["Bob", "blueberries"], ["Justin", "strawberries"], ["Ryan", "grapes"]]

# [['Michelle', 'bananas'], ['Bob', 'blueberries'], ['Justin', 'strawberries'], ['Ryan', 'grapes']]
print(fruits)

# using the append method to add more elements to the 2D list
fruits.append(["Nancy", "avocado"])

fruits.append(["Daniel", "oranges"])

# [['Michelle', 'bananas'], ['Bob', 'blueberries'], ['Justin', 'strawberries'], ['Ryan', 'grapes'],
# ['Nancy', 'avocado'], ['Daniel', 'oranges']]
print(fruits)

# using the remove method to remove the elements in the 2D list
fruits.remove(["Bob", "blueberries"])

fruits.remove(["Michelle", "bananas"])

# [['Justin', 'strawberries'], ['Ryan', 'grapes'], ['Nancy', 'avocado'], ['Daniel', 'oranges']]
print(fruits)

# modifying the 2D list with different elements
fruits[-1][-1] = "blackberries"

fruits[-1][-2] = "Rachel"

fruits[0][0] = "Shannon"

fruits[0][1] = "prunes"

# [['Shannon', 'prunes'], ['Ryan', 'grapes'], ['Nancy', 'avocado'], ['Rachel', 'blackberries']]
print(fruits)

# printing out a single index to my favorite fruits list
print(fruits[1][1])

print(fruits[1][0])

# using the insert method with 2d lists
fruits.insert(0, ["Marilyn", "bell peppers"])

# [['Marilyn', 'bell peppers'], ['Shannon', 'prunes'], ['Ryan', 'grapes'], ['Nancy', 'avocado'],
# ['Rachel', 'blackberries']]
print(fruits)

# use the count method to print out the number of elements in the list
fruits_count = favorite_fruits.count("cantaloupe")

print(fruits_count)

# use the sort method to sort the list in alphabetical order (in ascending order)
favorite_fruits.sort()

print(favorite_fruits)

# use the sort method to sort the list in alphabetical order (in descending order)
favorite_fruits.sort(reverse = True)

print(favorite_fruits)

# another property we can use with lists is using the negative slicing method
# will print out the last two elements
last_two_elements = favorite_fruits[-2:]

print(last_two_elements)

# will slice the last six elements of the list and print out the rest
slice_off_last_six_elements = favorite_fruits[:-6]

print(slice_off_last_six_elements)
