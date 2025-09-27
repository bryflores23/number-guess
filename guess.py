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
