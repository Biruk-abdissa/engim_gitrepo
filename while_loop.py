#while loop exercise
import random

print("welcome to Guess the number!")
print("The rules are simple. I will think of a number and you try to guess it.")
number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10:")
    if int(guess) ==number:
        print("you guesses {}: That is right! you win!".format(guess))
        break
    else:
        print("You guessed {}: sorry! that isn't it. Try aagin".format(guess))
        continue
 