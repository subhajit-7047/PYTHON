import random

jackpot= random.randint(1,100)

Guess=int(input("Let's Guess any integer:"))
counter=1

while Guess!=jackpot:
    if Guess<jackpot:
        print("Guess Higher.")
    else:
        print("Guess lower.")
    
    Guess=int(input("Let's Guess onece's more: "))
    counter+=1
print("correct Guess.") 
print("you took",counter ,"attempts.")   