import random

# List of possible words
word_list = ['python', 'hangman', 'challenge', 'programming', 'developer']

# Choose a random word from the list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
max_attempts = 6  # Maximum number of incorrect guesses allowed

# To keep track of guessed letters and attempts
guessed_letters = []
wrong_guesses = 0

# Create display with underscores
display = ['_' for _ in chosen_word]

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have", max_attempts, "incorrect guesses allowed.\n")

# Game loop
while wrong_guesses < max_attempts and '_' in display:
    print("Word:", ' '.join(display))
    guess = input("Guess a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You've already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess
        print("✅ Good guess!\n")
    else:
        wrong_guesses += 1
        print(f"❌ Wrong guess! You have {max_attempts - wrong_guesses} attempts left.\n")

# Game result
if '_' not in display:
    print("🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("💀 You've run out of guesses. The word was:", chosen_word)
