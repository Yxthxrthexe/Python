import random
randNumber = random.randint(1,100)

userguess = None
while (userguess != randNumber):
   userguess = int(input("Enter your guess:"))
   if userguess == randNumber:
    print("You made a right guess")
    
   else:
    print("Your guess is wrong")
    