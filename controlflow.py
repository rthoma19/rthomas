# Going to write a program about which roller coaster people should ride at Six Flags Magic Mountain

import random

random_number = random.randint(1, 16)

# print(random_number)

question = "Which roller coaster at Six Flags Magic Mountain should I ride?"

answer = ""

if random_number == 1:
    answer = "Full throttle"

elif random_number == 2:
    answer = "Goliath"

elif random_number == 3:
    answer = "X2"

elif random_number == 4:
    answer = "Viper"

elif random_number == 5:
    answer = "Tatsu"

elif random_number == 6:
    answer = "West Coast Racers"

elif random_number == 7:
    answer = "Apocalypse"

elif random_number == 8:
    answer = "Batman"

elif random_number == 9:
    answer = "Scream"

elif random_number == 10:
    answer = "Superman"

elif random_number == 11:
    answer = "Riddler's Revenge"

elif random_number == 12:
    answer = "Gold Rusher"

elif random_number == 13:
    answer = "Lex Luthor"

elif random_number == 14:
    answer = "Ninja"

elif random_number == 15:
    answer = "The Revolution"

elif random_number == 16:
    answer = "Twisted Colossus"

else:
    answer = "Error"

print(question + " The roller coaster that you should ride at Six Flags Magic Mountain is: " + answer)
