#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")
text = f.read().strip().split()

print("\nCan your password survive a dictionary attack? You have three tries.")
for i in range(3):
    x = input("Type in a trial password: ")
    if x in text:
        print("The password: " + "'"+ (x) + "'" + " is too weak.")
        print("I hacked you! HAHA")
        print("Try again!\n")
    else:
        print("Darn! You made an actual good password.")
        print("Good job I guess...")
        break




'''
print("Can your password survive a dictionary attack?")

#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
test_password = input("Type in a trial password: ")

#Write logic to see if the password is in the dictionary file below here:
for line in f:
    if test_password == ("dictionary.txt", "r")
        print("The password " + input + "is too weak.")'''
