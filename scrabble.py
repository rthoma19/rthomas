# I am going to write a program about Scrabble
import os
import random
import string

dict_list = open("scratch.txt", 'r')

contents = dict_list.read()

# print(contents)

# creating a list for letters
letters_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z", "#"]

# creating a list for the point values for each letter
letter_score_list = [1, 3, 3, 2, 1, 4, 2, 4, 1, 1, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]

# joining the two lists together with zip() using a list comprehension
letter_to_points_list = {letters_list: letter_score_list for
                         letters_list, letter_score_list in zip(letters_list, letter_score_list)}

# printing out the two lists together with letters and point values
print(letter_to_points_list)

# creating a list for the number of tiles there are for each letter
letter_tiles_list = [9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1, 2]

# joining the two lists together with zip() using a list comprehension
letter_to_tiles_list = {letters_list: letter_tiles_list for
                         letters_list, letter_tiles_list in zip(letters_list, letter_tiles_list)}

# printing out the two lists togetjer with letters and tile numbers
print(letter_to_tiles_list)

# Asking people how many players you have to play (need at least two but no more than four)
question = int(input("Welcome to Scrabble. How many people are playing today? (2-4 players): "))

# Checking to see if we have a minimum number of two players and a maximum number of four players
if question < 2 or question > 4:
    print("Sorry, the game needs to be at least 2 players but no more than 4 players. ")

# Doing an if/else statement to indicate the number of players so they canb write their names
if question == 2:
    player1 = str(input("Player 1, please enter your name: "))
    print("Welcome " + player1)

    player2 = str(input("Player 2, please enter your name: "))
    print("Welcome " + player2)

if question == 3:
    player1 = str(input("Player 1, please enter your name: "))
    print("Welcome " + player1)

    player2 = str(input("Player 2, please enter your name: "))
    print("Welcome " + player2)

    player3 = str(input("Player 3, please enter your name: "))
    print("Welcome " + player3)

if question == 4:
    player1 = str(input("Player 1, please enter your name: "))
    print("Welcome " + player1)

    player2 = str(input("Player 2, please enter your name: "))
    print("Welcome " + player2)

    player3 = str(input("Player 3, please enter your name: "))
    print("Welcome " + player3)

    player4 = str(input("Player 4, please enter your name: "))
    print("Welcome " + player4)

# converting the alphabet into uppercase letters
letters_alphabet = string.ascii_uppercase

# using an if/else statement to indicate how many players are playing the game so each player can have seven tiles

if question == 2:

    random_letters_for_player_one = random.choices(letters_alphabet, k = 7)

    print(player1, random_letters_for_player_one)

    random_letters_for_player_two = random.choices(letters_alphabet, k = 7)

    print(player2, random_letters_for_player_two)

if question == 3:

    random_letters_for_player_one = random.choices(letters_alphabet, k = 7)

    print(player1, random_letters_for_player_one)

    random_letters_for_player_two = random.choices(letters_alphabet, k = 7)

    print(player2, random_letters_for_player_two)

    random_letters_for_player_three = random.choices(letters_alphabet, k = 7)

    print(player3, random_letters_for_player_three)

if question == 4:

    random_letters_for_player_one = random.choices(letters_alphabet, k = 7)

    print(player1, random_letters_for_player_one)

    random_letters_for_player_two = random.choices(letters_alphabet, k = 7)

    print(player2, random_letters_for_player_two)

    random_letters_for_player_three = random.choices(letters_alphabet, k = 7)

    print(player3, random_letters_for_player_three)

    random_letters_for_player_four = random.choices(letters_alphabet, k = 7)

    print(player4, random_letters_for_player_four)

# Asking the players to enter a word to see if it is in the dictionary or not
# Also asking the players where they would like their words to be on the game board (vertical or horizontal)
# If the user puts in vertical, then the letters will print out vertical
# If the user puts in horizontal, then the letters will print out horizontal

if question == 2:
    player1_word = str(input(player1 + " please enter a word: "))

    play_word_1 = str(input(player1 + " would you like the word to be vertical (v) or horizontal (h): "))

    play_game_1 = str(input(player1 + " where would you like the word to be? Please include x axis and y axis (x, y): "))

    player2_word = str(input(player2 + " please enter a word: "))

    play_word_2 = str(input(player2 + " would you like the word to be vertical (v) or horizontal (h): "))

    play_game_2 = str(input(player2 + " where would you like the word to be? Please include x axis and y axis (x, y): "))

    if play_word_1 == 'v':
        player1_word_1 = ""
        for i in player1_word:
            player1_word_1 = player1_word_1 + i + "\n"
        print(player1_word_1)

    if play_word_1 == 'h':
        print(player1_word)

    if play_word_2 == 'v':
        player2_word_1 = ""
        for i in player2_word:
            player2_word_1 = player2_word_1 + i + "\n"
        print(player2_word_1)

    if play_word_2 == 'h':
        print(player2_word)

if question == 3:
    player1_word = str(input(player1 + " please enter a word: "))

    play_word_1 = str(input(player1 + " would you like the word to be vertical (v) or horizontal (h): "))

    play_game_1 = str(input(player1 + " where would you like the word to be? Please include x axis and y axis (x, y): "))

    player2_word = str(input(player2 + " please enter a word: "))

    play_word_2 = str(input(player2 + " would you like the word to be vertical (v) or horizontal (h): "))

    play_game_2 = str(input(player2 + " where would you like the word to be? Please include x axis and y axis (x, y): "))

    player3_word = str(input(player3 + " please enter a word: "))

    play_word_3 = str(input(player3 + " would you like the word to be vertical (v) or horizontal (h): "))

    play_game_3 = str(input(player3 + " where would you like the word to be? Please include x axis and y axis (x, y): "))

    if play_word_1 == 'v':
        player1_word_1 = ""
        for i in player1_word:
            player1_word_1 = player1_word_1 + i + "\n"
        print(player1_word_1)

    if play_word_1 == 'h':
        print(player1_word)

    if play_word_2 == 'v':
        player2_word_1 = ""
        for i in player2_word:
            player2_word_1 = player2_word_1 + i + "\n"
        print(player2_word_1)

    if play_word_2 == 'h':
        print(player2_word)

    if play_word_3 == 'v':
        player3_word_1 = ""
        for i in player3_word:
            player3_word_1 = player3_word_1 + i + "\n"
        print(player3_word_1)

    if play_word_3 == 'h':
        print(player3_word)

if question == 4:
    player1_word = str(input(player1 + " please enter a word: "))

    play_word_1 = str(input(player1 + " would you like the word to be vertical (v) or horizontal (h): "))

    play_game_1 = str(input(player1 + " where would you like the word to be? Please include x axis and y axis (x, y): "))

    player2_word = str(input(player2 + " please enter a word: "))

    play_word_2 = str(input(player2 + " would you like the word to be vertical (v) or horizontal (h): "))

    play_game_2 = str(input(player2 + " where would you like the word to be? Please include x axis and y axis (x, y): "))

    player3_word = str(input(player3 + " please enter a word: "))

    play_word_3 = str(input(player3 + " would you like the word to be vertical (v) or horizontal (h): "))

    play_game_3 = str(input(player3 + " where would you like the word to be? Please include x axis and y axis (x, y): "))

    player4_word = str(input(player4 + " please enter a word: "))

    play_word_4 = str(input(player4 + " would you like the word to be vertical (v) or horizontal (h): "))

    play_game_4 = str(input(player4 + " where would you like the word to be? Please include x axis and y axis (x, y): "))

    if play_word_1 == 'v':
        player1_word_1 = ""
        for i in player1_word:
            player1_word_1 = player1_word_1 + i + "\n"
        print(player1_word_1)

    if play_word_1 == 'h':
        print(player1_word)

    if play_word_2 == 'v':
        player2_word_1 = ""
        for i in player2_word:
            player1_word_1 = player2_word_1 + i + "\n"
        print(player2_word_1)

    if play_word_2 == 'h':
        print(player2_word)

    if play_word_3 == 'v':
        player3_word_1 = ""
        for i in player1_word:
            player3_word_1 = player3_word_1 + i + "\n"
        print(player3_word_1)

    if play_word_3 == 'h':
        print(player3_word)

    if play_word_4 == 'v':
        player4_word_1 = ""
        for i in player1_word:
            player4_word_1 = player4_word_1 + i + "\n"
        print(player4_word_1)

    if play_word_4 == 'h':
        print(player4_word)

letter_to_points = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 1, 'K': 5, 'L': 1,
                    'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
                    'Y': 4, 'Z': 10, '#': 0}

# creating a board to print out the first word on the game board after it is being played

game_board = [[' '] * 15 for i in range(15)]

def first_word_on_game_board(game_board, player1_word):
    columns_on_board = '012345678901234'

    rows_on_board = '_' * 15

    print(' ' + columns_on_board)
    print(' ' + rows_on_board)

    for i in range(15):
        if i != 7:
            star = ''.join(game_board[i])
            print('|' + star + '|' + str(i))

        else:
            length_for_word = int((15 - len(player1_word)) / 2)

            if len(player1_word) % 2 == 0:
                print('|' + length_for_word * " " + player1_word + length_for_word * " " + '|7')

            else:
                print('|' + length_for_word * " " + player1_word + length_for_word * " " + '|7')

    print(' ' + rows_on_board)
    print(' ' + columns_on_board)

first_word_on_game_board(game_board, player1_word)

# indicating the total score for each player

# Score for two players

if question == 2:
    grand_total_1 = 0
    for letter in player1_word.upper():
        grand_total_1 += letter_to_points[letter]
    print(grand_total_1)

    grand_total_2 = 0
    for letter in player2_word.upper():
        grand_total_2 += letter_to_points[letter]
    print(grand_total_2)

# Score for three players

if question == 3:
    grand_total_1 = 0
    for letter in player1_word.upper():
        grand_total_1 += letter_to_points[letter]
    print(grand_total_1)

    grand_total_2 = 0
    for letter in player2_word.upper():
        grand_total_2 += letter_to_points[letter]
    print(grand_total_2)

    grand_total_3 = 0
    for letter in player3_word.upper():
        grand_total_3 += letter_to_points[letter]
    print(grand_total_3)

# Score for four players

if question == 4:
    grand_total_1 = 0
    for letter in player1_word.upper():
        grand_total_1 += letter_to_points[letter]
    print(grand_total_1)

    grand_total_2 = 0
    for letter in player2_word.upper():
        grand_total_2 += letter_to_points[letter]
    print(grand_total_2)

    grand_total_3 = 0
    for letter in player3_word.upper():
        grand_total_3 += letter_to_points[letter]
    print(grand_total_3)

    grand_total_4 = 0
    for letter in player4_word.upper():
        grand_total_4 += letter_to_points[letter]
    print(grand_total_4)

if question == 2:
    print("The total score for " + str(player1) + " is " + str(grand_total_1))

    print("The total score for " + str(player2) + " is " + str(grand_total_2))

if question == 3:
    print("The total score for " + str(player1) + " is " + str(grand_total_1))

    print("The total score for " + str(player2) + " is " + str(grand_total_2))

    print("The total score for " + str(player3) + " is " + str(grand_total_3))

if question == 4:
    print("The total score for " + str(player1) + " is " + str(grand_total_1))

    print("The total score for " + str(player2) + " is " + str(grand_total_2))

    print("The total score for " + str(player3) + " is " + str(grand_total_3))

    print("The total score for " + str(player4) + " is " + str(grand_total_4))
