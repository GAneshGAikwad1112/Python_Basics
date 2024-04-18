#Guess the number

import random

target = random.randint(1, 100)

while True:

    user = input("Guess the value or Quit(Q) : ")

    if (user =="Q" or "q"):
        break

    user = int(user)
    
    if ( user == target):
        print("\nSuccess : correct Guess!\n")
        break

    elif ( user < target):
        print("Your number was too small. Take a bigger guess.....")

    else:
        print("Your number was too big. Take a smaller guess.....")

print("\n---------------GAME_OVER----------------------\n")