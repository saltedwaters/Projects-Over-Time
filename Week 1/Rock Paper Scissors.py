import random
options = ("Rock", "Paper", "Scissors")
player = None
computer = random.choice(options).capitalize()

print("-----ROCK, PAPER, SCISSORS-----")
while player not in options:
    player = input("Choose your fighter: ").capitalize()
    print("Choose a valid option.")

print(f"Player: {player}")
print(f"Computer: {computer}")

if player == computer:
    print("Draw!")
elif player == "Rock" and computer == "Scissors":
    print("You win!")
elif player == "Scissors" and computer == "Paper":
    print("You win!")
elif player == "Paper" and computer == "Rock":
    print("You win!")
else:
    print("You lose!")