# Number Guessing Game
# Computer picks a random number between 1 and 100.
# User guesses until they get it right, with hints if too high/low.
import random
# import random: this tells python we want to use the standard library module named random.
# that module contains functions for gathering random numbers, which we need so the game choses a different number each run.
secret_number = random.randint(1,100)
attempts = 0 # initialize attempts counter
# Store the number once so it doesn't change every guess. 
# random.radint(1,100): returns an integer including both endpoints 1 and 100. 
# we store the returned value in the variable secret_number so the program can compare the players guesses to this value later. 
# we use a variable because we need that same number avalible accross multiple steps in the program (not re-generating it each time).
print("I'm thinking of a number between 1 and 100.")
# this gives feedback to the user so they know the program is running and what to guess in.
# print() writes text to the console.
while True:
    # A While True: loop keeps running forever.
    raw = input("Make a guess: ")
# input(prompt) prints the prompt to the console and pauses the program until the user types something and presses enter. 
# Whatever the user types is returned as a string(text) If they type 42, input() returns "42". 
    try:
# converts guess to integer 
        guess = int(raw)
        attempts += 1 # increment here after valid input

    except ValueError:
        print("Please enter a whole number like 42.")
        continue
    # continue jumps back to the start of the loop. 
# int() tries to convert its argument to an integer value. int("42) -> 42
# after this line, the varible raw no longer holds a string - it holds an integer.
# if the user types something that can't be converted to an integer (like "hello" or "3.14"), int() will raise a ValueError exception.
    print(f"You guessed {guess}.")
# f-strings automatically converts the value to a string when inserting {guess} and are easier to read. 

    if guess < secret_number:
        print("Sorry too low.")
# if states if the guess is less than the secret number, it'll print "Sorry too low."
    elif guess > secret_number:
        print("Sorry too high.")
# elif states if the guess is greater than the secret number, it'll print "Sorry too high."
    else:
        print(f"CONGRATS! You guessed it right in {attempts} attempts!")
# for else, since both "if" and "elif" are false, the only possible outcome would be guess == secret_number.
# keep in mind that you don't need to write "else guess == secret_number" as this would cause an error. 
        break 
# break exits the loop.
