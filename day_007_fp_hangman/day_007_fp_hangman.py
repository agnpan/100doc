import random
from hangman_art import stages, logo
from hangman_words import word_list

lives = 6  # It takes 6 lives to hang the hangman
display = []
guess = ""
chosen_word = random.choice(word_list)
for letter in chosen_word:
	display.append("_")

print(logo)
print("".join(display))

end_of_game = False
while not end_of_game:

	guess = input("Guess a letter: ").lower()
	if guess in display:
		print(f"\nYou have already guessed the letter {guess}.")

	index_word = 0
	for letter in chosen_word:
		if guess == letter:
			display[index_word] = letter
			index_word += 1
		else:
			index_word += 1

	display_joint = "".join(display)
	if guess not in chosen_word:
		print(f"Incorrect letter: {guess}. You lose a life.")
		print(stages[lives])
		print(display_joint)
		lives -= 1
	else:
		print(display_joint)
		
	if "_" not in display:
		print(f"\nCongratulations! You won! The word is '{chosen_word}'.")
		end_of_game = True
	elif lives == -1:
		print(f"\nSorry! You lost. The word is '{chosen_word}'.")
		end_of_game = True
