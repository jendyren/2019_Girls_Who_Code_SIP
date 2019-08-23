while 1:
    print("Made by Olivia + Jendy!")
    #Jendy
    #Olivia
    # Update this text to match your story.
    start = '''
    \n\n\nYou wake up one morning and find that you aren't in your bed; you aren't even in your room.
    You're in the middle of a giant maze.
    A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
    There is a hallway to your right and to your left.
    '''

    print(start)

    print("Type 'left' to go left or 'right' to go right.") # Update to match your story.
    user_input = input()
    if user_input == "left":
        print("\nYou decide to go left and found a skeleton in leather armor. The skeleton holds a sign saying, if you turn right you die, if you turn left again you'll find a way out." ) # Update to match your story.
        print("Type 'left' to go left or 'right' to go right.")
        user_input = input()
        if (user_input == "left"):
            print("\nYou listen to the skeleton and find a door on your left.")
            print("When you go through the door, you find a glittering ring on the floor. When you pick it up a beam of light shines to the right.")
            print("Type 'left' to go left or 'right' to go right.")
            user_input = input()
            if (user_input == "left"):
                print ('\nYou chose not to follow the light and stumble into a dark cave and get eaten by a giant mutant bat.')
            else:
                print ('\nYou chose to follow the ring and find yourself in a bright cave lit by clusters of glittering ores.')
                print ('There in the room lies a mountain of treasure. However, at the foot of the treaure pile is a warning that the treasure is cursed.')
                print("Type 'take' to take the treasure or 'leave' to keep going.")
                user_input = input()
                if (user_input == "take"):
                    print ('\nYou take a glittering crown and place it on your head. You instantly get possesed by a ghost.')
                else:
                    print ('\nYou leave the treasure and continue walking, eventually finding a strange portal. When you jump in, you are back in your bedroom.')


        else:
            print("\nYou refused to listen to the skeleton and decided to go right. Let's hope you chose the right path! As you continue walking, you see three strange wooden doors. The 1st door is labelled with Fiery Hell, the 2nd door holds a dangerous serial killer, and the 3rd door holds a hungry lion who hasn't been fed for 100 years. ")
            print("Type '1' to go to the first door, '2' to go the the second door, or '3' to go to the third door.")
            user_input = input()
            if (user_input == "1"):
                print("\nYou decided to open the first door and ultimately fell to a fiery doom.")
            if (user_input == "2"):
                print("\nWhen you open the door to the serial killer, you find yourself being cut down the middle with a saw.")
            if (user_input == "3"):
                print("\nCongratulations! You used your brain and chose this door. You find yourself in the room with a pile of bones. If the lion was not fed for 100 years, it would have died!")
                print ("You notice a particularly sharp bone in the pile. Do you want to take it with you? Answer \"yes\" or \"no\".")
                user_input = input()
                if (user_input == "yes"):
                    print ('\nYou find an ogre and slay it with the sharp bone. Inside the ogre\'s pocket is a red button. Do you want to press the button?')
                    print ('Answer "yes" or "no".')
                    user_input = input()
                    if (user_input == "yes"):
                        print ('\nWhen you press the button the entire world immedietly explodes and you die.')
                    else:
                        print ("\nYou wisely decide not to press the red button and continue to the next room.")
                        print("\nThe next room only contain a table with a bottle saying 'Drink Me.' Do you want to drink it?")
                        print("Answer 'yes' or 'no'.")
                        user_input = input()
                        if (user_input == "yes"):
                            print ('\nYou decide to the drink the liquid in the strange bottle and end up fainting. When you wake up, you find yourself in your bedroom.')
                        else:
                            print('\nYou decide not to drink the liquid and spend the rest of your life in the room, eventually dying of starvation.')

                else:
                    print ('When you walk into the next room you are immedietly attacked by an ogre and die.')

    elif user_input == "right":
        print("\nYou choose to go right and found a pile of silver with strange engravings. When looking carefully, you find that each of the engravings have a letter R.  ") # Update to match your story.
        print("Type 'left' to go left or 'right' to go right.")
        user_input = input()
        if (user_input == "right"):
            print("\nCongratualations! You paid close attention to details and chose the correct path.")
            print ("You find yourself in a magical fairy kingdom. Do you want to stay here or try to find a way out?")
            print("Type 'stay' to stay in the kingdom or 'leave' to find your way home.")
            user_input = input()
            if (user_input == "leave"):
                print("\nYou find a traveling fairy and pay him a silver coin to take you home. You end up back in your bedroom.")
            else:
                print ('\nWhile staying in the fairy kingdom, you catch the wrath of the Fairy Mafia and get turned into a frog.')

        else:
            print("\nYou didn't pay close attention to clues and as a result fell into a pit of lava.")
        # Continue code to finish story.
