import random


def game(comp, p1):
    if comp == 'S' and p1 == 'W':
        print("You Win")
    elif comp == 'S' and p1 == 'G':
        print("You Lose")
    elif comp == 'W' and p1 == 'S':
        print("You Lose")
    elif comp == 'W' and p1 == 'G':
        print("You Win")
    elif comp == 'G' and p1 == 'S':
        print("You Win")
    elif comp == 'G' and p1 == 'W':
        print("You Lose")
    elif comp == 'S' and p1 == 'S':
        print("Tie")
    elif comp == 'G' and p1 == 'G':
        print("Tie")
    else:
        print("Tie")


print(" -----------------------------------------------------------")
print(" |||||||||||||||||| STONE PAPER SCISSOR ||||||||||||||||||||")
print(" -----------------------------------------------------------")
randNo = random.randint(1, 3)
b = input("Your Turn: Stone(S) Paper(W) or Scissor(G) ")

if randNo == 1:
    comp = 'S'
elif randNo == 2:
    comp = 'W'
elif randNo == 3:
    comp = 'G'
print("Computer's Turn: ", comp)

game(comp, b)
