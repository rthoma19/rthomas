# Writing a program that answers any "Yes" or "No" question with a different fortune each time it executes.

# Setting up
import random

name = "Ryan"

question = "Do you know if I will get a career job in the future?"

answer = ""

# Generating a random number
random_number = random.randint(1, 10)

# printing a random number from 1 to 9
# print(random_number)

# control flow
if random_number == 1:
    answer = "Yes - definitely."

elif random_number == 2:
    answer = "It is decidedly so."

elif random_number == 3:
    answer = "Without a doubt."

elif random_number == 4:
    answer = "Reply hazy, try again."

elif random_number == 5:
    answer = "Ask again later."

elif random_number == 6:
    answer = "Better not tell you now."

elif random_number == 7:
    answer = "My sources say no."

elif random_number == 8:
    answer = "Outlook not so good."

elif random_number == 9:
    answer = "Very doubtful."

elif random_number == 10:
    answer = "My sources say yes."

else:
    answer = "Error"

# Seeing the result

# Checking to see if the name is not equal to an empty string

if name == "":
    print("Question: " + question)

else:
    print(name + " asks: " + question)

# Checking to see if the question is not equal to an empty string

if question == "":
    print("The Magic 8-Ball cannot provide a fortune unless you ask it something.")

else:
    print("Magic 8-Ball's answer: " + answer)
