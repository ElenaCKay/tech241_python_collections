# Magic number game

import random

user_name = input("What is your name? ")
print(f"Hello {user_name}! This is the magic number game. If you would like to quit at any time just type quit")
level = input("You get three go's to find the magic number! Pick a level: easy, medium, hard, insane ")

biggest_num = 20

if level == "easy":
    biggest_num = 10
if level == "medium":
    biggest_num = 20
if level == "hard":
    biggest_num = 50
if level == "insane":
    biggest_num = 100

magic_number = random.randint(1, int(biggest_num))
guess_count = 0

while guess_count <= 3:
    try:
        user_guess = input(f"Pick a number between 1 and {biggest_num}: ")
        guess_count += 1
        if user_guess == "quit":
            break
        user_number = int(user_guess)
        if user_number == magic_number:
            print(f"You did it! You guessed the magic number {magic_number}!")
            break
        if guess_count == 3:
            print(f"You ran out of guesses! The magic number was {magic_number}. Try again...")
            break
        elif user_number < magic_number:
            print("That number is too small... ")
        else:
            print("That number is too big... ")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

