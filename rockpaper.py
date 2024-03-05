import random

choices = ["rock","paper","scissors"]
player = None
while True:
    computer = random.choice(choices)
    player = input("Rock, Paper, Scissors? = ").lower()
    if player not in choices:
        continue
    print("computer:",computer)
    if player == computer:
        print("Its tie!")
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"): 

        print("player wins")
    else:
        print("computer wins")
    play=input("play again y/n:").lower()
    if play not in ['yes','y']:
        break
print("Bye!")