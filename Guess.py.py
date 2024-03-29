#Jendy
#Guess the Number Game

#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)

i = 0
while i < 3:
	guess = input("Guess a number between 1 and 20 (inclusive): ")
	if not guess.isnumeric(): # checks if a string is only digits 0 to 9
		print("That's not a positive whole number, try again!")
	else:
		guess = int(guess) # converts a string to an integer
	if (guess == aRandomNumber):
		print("Correct!")
		break
	else:
		print("Wrong, try again.")
		i += 1
		if (guess < aRandomNumber):
			print("Guess a higher number.")
		else:
			print("Guess a lower number.")

print ("Game Over. The number chosen was:")
print (aRandomNumber)
