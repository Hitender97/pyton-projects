import random

choices = ["rock","paper","scissors"]
player = None
computer = random.choice(choices)
while True:
    player = input("Rock, Paper, Scissors? = ").lower()
    if player not in choices:
        continue
    print("computer picks:",computer)
    if player == computer:
        print("Its tie!")
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"): 

        print("player wins")
    else:
        print("computer wins")
    play=input("play again:").lower()
    if play != "yes":
        break
print("Bye!")