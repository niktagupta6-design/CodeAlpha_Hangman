import random

# List of predefined words
words = ["python", "apple", "banana", "school", "computer"]

# Randomly select a word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of wrong guesses
wrong_guesses = 0
max_wrong_guesses = 6

print("=================================")
print("      WELCOME TO HANGMAN GAME")
print("=================================")

# Game loop
while wrong_guesses < max_wrong_guesses:

    # Display the guessed word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the player has guessed the word
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    # Take input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Store guessed letter
    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        print("✅ Correct Guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong Guess!")
        print("Remaining Chances:", max_wrong_guesses - wrong_guesses)

# Game Over
if wrong_guesses == max_wrong_guesses:
    print("\n💀 Game Over!")
    print("The correct word was:", word)
