import random

choices = ["rock", "paper", "scissors"]

print("Welcome to Rock-Paper-Scissors Game!")
print("Type 'rock', 'paper', or 'scissors' to play.\n")

user = input("Your choice: ").lower()

computer = random.choice(choices)

print("Computer's choice:", computer)

if user == computer:
    print("It's a draw!")
elif user == "rock" and computer == "scissors":
    print("You won the game!")
elif user == "paper" and computer == "rock":
    print("You won the game!")
elif user == "scissors" and computer == "paper":
    print("You won the game!")
elif user in choices:
    print("You lose!")
else:
    print("Invalid input. Please type rock, paper, or scissors.")
