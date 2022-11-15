import random

options = ("rock" , "paper", "scissors")

Variable = True
while Variable:
	player = None
	computer = random.choice(options)

	while player not in options:
		player = input("Enter a choice (rock, paper, scissors) : ")

	print(f"player : {player}")
	print(f"computer : {computer}")

	if player == computer:
		print("It's a tie.")
	elif player == "rock" and computer == "scissors":
		print("You won.")
	elif player == "paper" and computer == "rock":
		print("You won.")
	elif player == "scissors" and computer == "paper":
		print("You won.")
	else:
		print("You lost.")
	if not input("Play again ! (y/n) : ").lower() == 'y':
		Variable = False
print("\nThank you for playing.")
