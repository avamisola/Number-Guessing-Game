"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
"""

import random

def start_game():

    """
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    """

    #1
    print("-------------------------------------------")
    print("Welcome to the Number Guessing Game!")
    print("-------------------------------------------")

    #2
    random_num = random.randint(1, 10)

    #3
    game_active = True
    try_count = 0
    while game_active:
        try_count += 1
        try:
            guess_num = int(input("Please guess a whole number between (and including) 1 and 10: "))
        except ValueError:
            print("Please input an integer...")
            continue
        if guess_num == random_num:
            game_active = False
        elif guess_num > random_num:
            print("It's lower...")
        elif guess_num < random_num:
            print("It's higher...")
    #4
    else:
        print("-------------------------------------------")
        print(f"Got it! You guessed the correct number: {random_num}!")
        print(f"It took you {try_count} attempts to guess the correct number!")
    #5
        print("-------------------------------------------")
        print(f"The game has ended. Thank you for playing!")
        print("-------------------------------------------")

# Kick off the program by calling the start_game function.
start_game()
