import random
from hangman_art import logo, stages
from hangman_words import word_list
from clear import clear
# note to self - clear doesn't work on pycharm terminal

# Randomly choose a word from the word_list
chosen_word = random.choice(word_list)
print(f"Pssst, the solution is {chosen_word}.")

# Display the game logo at the start
print(f"{logo} \n")

# Initialize the display list with underscores to represent the unguessed letters
display_list = []
for i in range(1, len(chosen_word) + 1):
    display_list.insert(i - 1, "_")

# MAIN GAME LOOP
total_incorrect_guesses = 0
display_list_for_comparison = ""
previous_guesses = []

# Continue looping until the player has made 6 incorrect guesses or guessed the word
while total_incorrect_guesses != 6 and display_list_for_comparison != chosen_word:
    guess = input("Guess a letter: ").lower()

    clear()

    # Check if the letter has already been guessed
    prev_guess = False
    if (guess in previous_guesses and guess in display_list) or (guess not in chosen_word and guess in previous_guesses):
        print(f"You've already guessed {guess}")
        prev_guess = True
    elif guess not in chosen_word and not prev_guess:
        print(
            f"You guessed {guess}, that's not in the word. You lose a life. You now have {5 - total_incorrect_guesses} guesses remaining."
        )

    # Add the guessed letter to the list of previous guesses if it's a new guess
    if guess not in previous_guesses:
        previous_guesses.append(guess)

    # Update the display list with the correctly guessed letter(s)
    for i in range(1, len(chosen_word) + 1):
        if chosen_word[i - 1] == guess and display_list[i - 1] == "_":
            display_list[i - 1] = guess

    # Construct the string to compare the current guess state with the chosen word
    display_list_for_comparison = ""
    for i in range(1, len(chosen_word) + 1):
        display_list_for_comparison += display_list[i - 1]
        print(f"{display_list[i-1]}", end="")

    # Display the appropriate hangman stage and check the game status
    if display_list_for_comparison != chosen_word and guess in chosen_word and total_incorrect_guesses == 6:
        print(f"\n {stages[5]}")
    elif display_list_for_comparison == chosen_word and guess in chosen_word:
        print(f"\n{stages[6 - total_incorrect_guesses]}")
    elif display_list_for_comparison != chosen_word and not prev_guess and guess in chosen_word:
        print(f"\n{stages[6 - total_incorrect_guesses]}")
    elif display_list_for_comparison != chosen_word and prev_guess and guess in chosen_word:
        print(f"\n{stages[6 - total_incorrect_guesses]}")
    elif display_list_for_comparison != chosen_word and not prev_guess and guess not in chosen_word:
        total_incorrect_guesses += 1  # Increment the number of incorrect guesses
        print(f"\n{stages[6 - total_incorrect_guesses]}")
    elif display_list_for_comparison != chosen_word and prev_guess and guess not in chosen_word:
        print(f"\n{stages[6 - total_incorrect_guesses]}")

# End-of-game message
if display_list_for_comparison not in chosen_word:
    print(
        f"Unfortunately, you've been hanged to death for failing to guess the word '{chosen_word}'. Better luck next time!"
    )
else:
    print(
        f"Congratulations! You avoided a deathly hanging by guessing the word '{chosen_word}'. Well done!"
    )
