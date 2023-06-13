# Magic number game

import random

magic_number = random.randint(1, 20)
guess_count = 0

print("Hello! This is the magic number game.")

while guess_count <= 3:
    try:
        user_guess = int(input("Pick a number between 1 and 20: "))
        guess_count += 1

        if user_guess == magic_number:
            print(f"You did it! You guessed the magic number {magic_number}!")
            break
        if guess_count == 3:
            print(f"You ran out of guesses! The magic number was {magic_number}. Try again...")
            break
        elif user_guess < magic_number:
            print("That number is too small... ")
        else:
            print("That number is too big... ")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

