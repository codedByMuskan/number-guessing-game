
import random

secret_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

guess_count = 0

while True:
    guess = int(input("Take a guess: "))
    guess_count += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Correct! You guessed it in {guess_count} tries.")
        break
while True:
    # (put the entire guessing logic here)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing! Goodbye.")
        break

 