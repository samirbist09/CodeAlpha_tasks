import random

words = ["python", "coding", "intern", "alpha", "program"]

secret_word = random.choice(words)

guessed_letters = []

attempts = 6

print(" Welcome to Hangman Game!")
print("Guess the word, one letter at a time.")
print("_ " * len(secret_word))

# Game loop
while attempts > 0:
    guess = input("\nEnter a letter: ").lower()

    # Check for valid input
    if len(guess) != 1 or not guess.isalpha():
        print(" Please enter a single valid letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print(" You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if guess is in word
    if guess in secret_word:
        print(" Good guess!")
    else:
        attempts -= 1
        print(f" Wrong guess! Attempts left: {attempts}")

    # Display current progress
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(display_word)

    # Check if user won
    if "_" not in display_word:
        print("\n Congratulations! You guessed the word!")
        break

# If attempts are finished
if attempts == 0:
    print("\n Game Over! The word was:", secret_word)
