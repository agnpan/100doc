# ROCK PAPER SCISSORS

import random

rock = '''
	_______
---'   ____)
	  (_____)
	  (_____)
	  (____)
---.__(___)
'''

paper = '''
	_______
---'   ____)____
		  ______)
		  _______)
		 _______)
---.__________)
'''

scissors = '''
	_______
---'   ____)____
		  ______)
	   __________)
	  (____)
---.__(___)
'''

print("Welcome to Rock Paper Scissors!")

options = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)
if (player_choice > 2) or (player_choice < 0):
	print("You chose an invalid number! You lose")
else:
	print(f"You chose:\n{options[player_choice]}")
	print(f"Computer chose:\n{options[computer_choice]}")

if player_choice == computer_choice:
	print("Draw")
elif (player_choice == 0 and computer_choice == 1) or \
		(player_choice == 1 and computer_choice == 2) or \
		(player_choice == 2 and computer_choice == 0):
	print("You lose")
elif (computer_choice == 0 and player_choice == 1) or \
		(computer_choice == 1 and player_choice == 2) or \
		(computer_choice == 2 and player_choice == 0):
	print("You win")
