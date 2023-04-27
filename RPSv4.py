import random

player_wins = 0
computer_wins = 0
winning_score = 2

while player_wins < winning_score and computer_wins < winning_score:
	print()
	print("First to 3 WINS!")
	print(f"Player: {player_wins} vs Computer: {computer_wins}")
	print("rock...")
	print("paper...")
	print("scissors...")
	print()

	player = input("Shoot!: ").lower()
	if player == "quit" or player == "q":
		break
	rand_num = random.randint(0,2)
	if rand_num == 0:
		computer = "rock"
	elif rand_num == 1:
		computer = "paper"
	else:
		computer = "scissors"

	print()
	print(f"computer plays, {computer}")	

	if player == computer:
		print("It's a tie!")
	elif player == "rock":
		if computer == "scissors":
			print("You Win!")
			player_wins += 1
		elif computer == "paper":
			print("Computer Wins!")
			computer_wins += 1
	elif player == "paper":
		if computer == "rock":
			print("You Win!")
			player_wins += 1
		elif computer == "scissors":
			print("Computer Wins!")
			computer_wins += 1
	elif player == "scissors":
		if computer == "rock":
			print("Computer Wins!")
			computer_wins += 1
		elif computer == "paper":
			print("You Win!")
			player_wins += 1
	else: 
		print("your repsonse was invalid, computer wins by default...stoopid human")
		computer_wins += 1
print()
if player_wins == winning_score:
	print("*****You Won!*****")
else: 	
	print("You lost, sucka!")
print(f"Final Score...P: {player_wins} v C: {computer_wins}")
print()

# #this is ChatGPT's Version
# import random

# print("Let's play Rock, Paper, Scissors!")
# print("You will be playing against the computer.")

# # Define the options
# options = ["rock", "paper", "scissors"]

# # Get user's choice
# user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

# # Generate computer's choice
# computer_choice = random.choice(options)

# # Determine the winner
# if user_choice == computer_choice:
#     print("It's a tie!")
# elif user_choice == "rock":
#     if computer_choice == "paper":
#         print("Sorry, you lose. Paper covers rock.")
#     else:
#         print("Congratulations, you win! Rock smashes scissors.")
# elif user_choice == "paper":
#     if computer_choice == "scissors":
#         print("Sorry, you lose. Scissors cut paper.")
#     else:
#         print("Congratulations, you win! Paper covers rock.")
# elif user_choice == "scissors":
#     if computer_choice == "rock":
#         print("Sorry, you lose. Rock smashes scissors.")
#     else:
#         print("Congratulations, you win! Scissors cut paper.")
# else:
#     print("Invalid input. You must enter either 'rock', 'paper', or 'scissors'.")

