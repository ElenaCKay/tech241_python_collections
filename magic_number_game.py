# Magic number game

import random

magic_number = random.randint(1, 20)
guess_count = 0

user_name = input("What is your name? ")
print(f"Hello {user_name}! This is the magic number game. If you would like to quit at any time just type quit")

while guess_count <= 3:
    try:
        user_guess = input("Pick a number between 1 and 20: ")
        guess_count += 1
        if user_guess == "quit":
            break
        user_number = int(user_guess)
        if user_number == magic_number:
            print(f"You did it! You guessed the magic number {magic_number}!")
            break
        if guess_count == 3:
            try_again = input(f"You ran out of guesses! The magic number was {magic_number}. Try again...")
            break
        elif user_number < magic_number:
            print("That number is too small... ")
        else:
            print("That number is too big... ")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

