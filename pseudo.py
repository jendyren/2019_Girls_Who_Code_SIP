import random
guesses = []
maxfails = 10
fails = 0
#while fails < maxfails:
    #guess = input("Guess a letter: ")
    #print(guess)
    #fails = fails + 1
    #print("You have " + str(maxfails - fails) + " tries left!")
potential_words = ["bunnypillow", "japan", "mochi", "snapple", "appreciate"]
word = random.choice(potential_words)

list = list(word)

blankList = []
for i in range(len(list)):
    blankList.append("__")
print("current word is ", blankList)
while fails < maxfails:
    guess = input("Guess a letter: ")
    count_1 = list.count(guess)
    if count_1 != 0:
        print("correct!")
        index = list.index(guess)
        blankList.remove("__")
        blankList.insert(index,guess)
        print (blankList)
    else:
        print("You have " + str(maxfails - fails) + " tries left!")
        fails = fails + 1


'''if word == "japan":
    print (word)
    blankList = []
    for i in range(5):
        blankList.append("__")
    print("current word is ", blankList)
    while fails < maxfails:
        guess = input("Guess a letter: ")
        print(guess)
        if input == list(potential_words[1]):
            print("correct!")
        else:
            print("You have " + str(maxfails - fails) + " tries left!")
            fails = fails + 1
if word == "mochi":
    print (word)
    blankList = []
    for i in range(5):
        blankList.append("__")
    print("current word is ", blankList)
    while fails < maxfails:
        guess = input("Guess a letter: ")
        print(guess)
        if input == list(potential_words[2]):
            print("correct!")
        else:
            print("You have " + str(maxfails - fails) + " tries left!")
            fails = fails + 1
if word == "snapple":
    print (word)
    blankList = []
    for i in range(7):
        blankList.append("__")
    print("current word is ", blankList)
    while fails < maxfails:
        guess = input("Guess a letter: ")
        print(guess)
        if input == list(potential_words[3]):
            print("correct!")
        else:
            print("You have " + str(maxfails - fails) + " tries left!")
            fails = fails + 1
if word == "appreciate":
    print (word)
    blankList = []
    for i in range(10):
        blankList.append("__")
    print("current word is ", blankList)
    while fails < maxfails:
        guess = input("Guess a letter: ")
        print(guess)
        if input == "a" or "p" or "r" or "e" or "c" or "i" or "t":

            print("correct!")
        else:
            print("You have " + str(maxfails - fails) + " tries left!")
            fails = fails + 1'''





	# check if the guess is valid: Is it one letter? Have they already guessed it?
	# check if the guess is correct: Is it in the word? If so, reveal the letters!
