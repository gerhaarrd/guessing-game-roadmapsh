from random import randint
from time import time

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

print("Please select the difficulty level:")
print("1. Easy (10 attempts)")
print("2. Medium (5 attempts)")
print("3. Hard (3 attempts)")

number = randint(1, 100)

while True:
    choice = input("Enter your choice: ")
    if choice == '1':
        attempts = 10
        break
    elif choice == '2':
        attempts = 5
        break
    elif choice == '3':
        attempts = 3
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

print(f"Great! You have {attempts} attempts.")
print("Let's start the game!")

start_time = time()

guesses = 0

while attempts > 0:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    guesses += 1

    if guess == number:
        end_time = time()
        total_time = round(end_time - start_time, 2)
        print(f"Congratulations! You guessed the correct number in {guesses} attempts and {total_time} seconds.")
        break
    else:
        attempts -= 1
        if number > guess:
            print(f"Incorrect! The number is greater than {guess}.")
        else:
            print(f"Incorrect! The number is less than {guess}.")
        print(f"You have {attempts} attempts left.")

        if attempts == 0:
            print(f"Game Over! The correct number was {number}.")
