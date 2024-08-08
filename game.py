def game(computer_n,player_n):
    
    try:
        if player_n > computer_n:
            return "Your guess is higher than expected"
        elif player_n < computer_n:
            return "Your guess is lower than expected"
        else:
            
            return "Wow you got it!"
    except:
        return "You inputted wrong"




print("-----NUMBER GUESSING GAME-------")
print()
print()
print("You got 10 chances")
print()
print()

import random
fixed = random.randint(1,100)

for i in range(10):
    guess = int(input("Guess the number>> "))
    print(game(fixed,guess))
    if game(fixed,guess) == "Wow you got it!":
        break
print("Your chances are over")
print(fixed,"is the number")



