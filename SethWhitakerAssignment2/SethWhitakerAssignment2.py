# INF360 - Programming in Python
# Seth Whitaker
# Assignment 2
# Rock Paper Scissors
#
# Key: 
#      rock = 0
#      paper = 1
#      scissors = 2

import random

# Output Intro
print("Let's play Rock, Paper, Scissors!")
print("This will be best 3 out of 5.\n")

score = 0 # keep track of score

# Start Game
for i in range(5):
   
    computerChoice = random.randint(0, 2) # computer choice
    playerChoice = 0                      # player choice

    # validate input
    while True:
        choice = input("Choose rock, paper, or scissors: ")

        choice = choice.lower()

        # check if input is valid
        if choice == "rock":
            playerChoice = 0
        elif choice == "paper":
            playerChoice = 1
        elif choice == "scissors":
            playerChoice = 2            
        else:
            print("Invalid choice") # if invalid, repeat
            continue

        # output choice to user
        print("\nYou chose " + choice + ".")
        break

    # determine winner and output computer choice
    winner = 0
    if computerChoice == 0:
        print("I chose rock.")
        if playerChoice == 1:
            winner = 1
        elif playerChoice == 2:
            winner = 2
    elif computerChoice == 1:
        print("I chose paper.")
        if playerChoice == 2:
            winner = 1
        elif playerChoice == 0:
            winner = 2
    else:
        print("I chose scissors.")
        if playerChoice == 0:
            winner = 1
        elif playerChoice == 1:
            winner = 2

    # output round results
    if winner == 0:
        print("It's a tie.\n")
    elif winner == 1:
        score+=1
        print("Nice one!\n")
    elif winner == 2:
        score-=1
        print("Too bad.\n")

# output final results
print("After 5 rounds...")

if score > 0:
    print("You came out on top!")
elif score < 0:
    print("It didn't go very well for you.")
else:
    print("It ended in a draw.")

print("\n")

