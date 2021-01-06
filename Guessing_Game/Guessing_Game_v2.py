# Write a program that picks a random integer from 1 to 100, and has players guess the number. 

# The rules are:
# If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
# On a player's first turn, if their guess is within 10 of the number, return "WARM!"
# further than 10 away from the number, return "COLD!"
# On all subsequent turns, if a guess is
# closer to the number than the previous guess return "WARMER!"
# farther from the number than the previous guess, return "COLDER!"
# When the player's guess equals the number, tell them they've guessed correctly and 
# how many guesses it took!

import random

goal = random.randint(1, 101)
stored_answers = [0]
guess = 0

print("WELCOME TO GUESS THE NUMBER!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

while True:
    valid = False
    while valid == False:
        try:
            guess = int(input('Make a guess between 1 - 100: '))
        except ValueError:
            print('Found string input - Make a numerical guess between 1 - 100')
        else:
            if guess <= 0 or guess > 100:
                print('OUT OF BOUNDS - Make a numerical guess between 1 - 100')
            else:
                valid = True

    if guess == goal:
        stored_answers.append(guess)
        stored_answers.pop(0)
        print('You win! It took you {} tries.'.format(str(len(stored_answers))))
        print(stored_answers)
        break

    stored_answers.append(guess)

    if stored_answers[-2]:
        if abs(goal-guess) < abs(goal - stored_answers[-2]):
            print('WARMER!')
        else:
            print('COLDER!')
    else:
        if abs(guess - goal) < 10:
            print('WARM!')
        else:
            print('COLD!')