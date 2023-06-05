# This is a program that asks for your name.
#Then it invites you to guess the correct secret number.

import random

print('Hello. What is your name.')
name = input()

print('Well, ' + name + ' ,I am thinking of a number between 1 and 20. Take a guess.')
secretNumber = random.randint(1, 20)

for guessesTaken in (1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break #this condition is for the correct guess.


if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my secret number in ' + str(guessesTaken) + ' guesses.')
else:
    print('Nope. the number I was thinking of was ' + str(secretNumber) + '.')

