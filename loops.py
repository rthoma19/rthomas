# Writing a program that prints out numbers from 0 to 100 (using a while loop)

i = 0
while i <= 100:
    print(i)
    i += 1

# Writing a while loops that counts backwards from ten for a movie to start

countdown = 10

while countdown >= 0:
    print(countdown)
    countdown -= 1

print("It's showtime!")

# Project with while loops for a number guessing game

# defining a variable
secret_number = 9

# number of guesses
guess_count = 0

# number of chances we have
guess_limit = 3

while guess_count < guess_limit:
    # converting the input into an inout
    guess = int(input('Guess the number: '))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        # terminate our loop
        break

# else goes outside of the while loop
else:
    print('Sorry, you failed!')

# Project with while loops for a word guessing game

# defining a variable
secret_word = "fancy"

# number of guesses
guess_count = 0

# number of chances we have
guess_limit = 3

# using a while loop to guess the secret word
while guess_count < guess_limit:
    # converting the input into a string
    guess = str(input('Guess the word: '))
    guess_count += 1
    if guess == secret_word:
        print("You won!")
        # terminate our loop
        break

    # else goes outside of the while loop
else:
    print('Sorry, you failed!')

# Writing a program that prints out the values on a list (using a for loop)

list_fruit = ['bananas', 'apples', 'avocado', 'watermelon', 'grapes', 'blueberries', 'strawberries', 'peppers']

for item in list_fruit:
    print(item)

# Writing a program that uses the range function (using a for loop)

for item in range(0, 101, 10):
    print(item)

for item in range(0, 101):
    print(item)

# exercise with using for loops

prices = [10, 20, 30, 40, 50]

# setting up a variable and set it equal to 0
total = 0

# summing up all of the numbers in the prices list
for price in prices:
    total += price

# formatted string
print(f"Total: {total}")
