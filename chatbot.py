def intro():
    print(" (\___/)")
    print(" (^ - ^)")
    print(".(_____)")
    print("\nHello! My name is Botto!")

def hello_name(name):
    print("Hi " + name)

name = input()

yealist = ["yes", "Yes", "yea", "Yea", "ok", "Okay", "okay", "Ok"]
nolist = ["no", "nah", "No", "nope"]

def is_valid_input_yea(answer):
    if answer in yealist:
        return True
    else:
        return False
def is_valid_input_no(answer):
    if answer in nolist:
        return True
    else:
        return False


def game():
    answer = input("\nDo you want to play rock papers scissors? Type 'yes' or 'no'  ")
    if is_valid_input_yea(answer):
        print("Here we go!")
        from random import randint

        #create a list of play options
        t = ["rock", "raper", "scissors"]

        #assign a random play to the computer
        computer = t[randint(0,2)]

        #set player to False
        player = False

        while player == False:
        #set player to True
            player = input("rock, paper, scissors?   ")
            if player == computer:
                print("Tie!")
            elif player == "rock":
                if computer == "paper":
                    print("You lose!", computer, "covers", player)
                else:
                    print("You win!", player, "smashes", computer)
            elif player == "paper":
                if computer == "scissors":
                    print("You lose!", computer, "cut", player)
                else:
                    print("You win!", player, "covers", computer)
            elif player == "scissors":
                if computer == "rock":
                    print("You lose...", computer, "smashes", player)
                else:
                    print("You win!", player, "cut", computer)
            else:
                print("That's not a valid play. Check your spelling!")
            #player was set to True, but we want it to be False so the loop continues
            player = False
            computer = t[randint(0,2)]
            break

    else:
        is_valid_input_no(answer)
        print("\nOh darn! :<")

def main():
    intro()
    answer = input("\nWhat's your name? ")
    hello_name(answer)
    answer = input("\nWhat do you like to do?   ")
    print("\nThat's cool!")
    print("I like to mess around behind the scenes and maybe steal a few cookies here and there.")
    game()
    answer = input("\nWould you like to hear some jokes?")
    if is_valid_input_yea(answer):
        print('What do you get when you cross a snowman with a vampire?')
        input()
        print('Frostbite!')
        print()
        print('What do dentists call an astronaut\'s cavity?')
        input()
        print('A black hole!')
        print()
        print('Knock knock.')
        input()
        print("Who's there?")
        input()
        print('Interrupting cow.')
        input()
        print('Interrupting cow wh', end='')
        print('-MOO!')
    else:
        print("\nwow...ok be like that then.")
    print("\nThat's all for now! Make you come back and visit!")





# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
