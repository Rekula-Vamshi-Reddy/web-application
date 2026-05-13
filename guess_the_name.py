#guess the number

import random
target = random.randint(1,100)

while True:
    userchoice = input("Guess the target or Quit :")
    if (userchoice == "Quit"):
        break
    
    userchoice = int(userchoice)
    if(userchoice == target):
        print("success : correct guess!!")
        break

    elif(userchoice < target):
        print("your number was too small. take a bigger number")

    else:
        print("your number was too big. take a small number")

print(".....game over......")