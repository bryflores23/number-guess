import random
# import random: this tells python we want to use the standard library module named random.
# that module contains functions for gathering random numbers, which we need so the game choses a different number each run.
secret_number = random.randint(1,100)
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
        break
    # break is how you escape that infinate loop when the user finally gives valid input. 
    # if you forget break or place it outside the try block, the loop will either run forever or stop unexpectedly. 
    except ValueError:
        print("Please enter a whole number like 42.")
# int() tries to convert its argument to an integer value. int("42) -> 42
# after this line, the varible raw no longer holds a string - it holds an integer.

print(f"You guessed {guess}.")
# f-strings automatically converts the value to a string when inserting {guess} and are easier to read. 