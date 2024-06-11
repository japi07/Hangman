import random

# List of words
words = ["apple", "banana", "cherry", "date", "elderberry"]

# Randomly select a secret word
secret_word = random.choice(words)

while True:
    # Step 2: Ask the user to guess a letter
    guess = input("Guess a letter: ")
    
    # Step 3: Check that the guess is a single alphabetical character
    if len(guess) == 1 and guess.isalpha():
        # Step 1: Create an if statement that checks if the guess is in the word
        if guess in secret_word:
            # Step 2: Print a message if the guess is in the word
            print(f"Good guess! {guess} is in the word.")
            break  # If you want to end the loop after a correct guess, you can keep this line
        else:
            # Step 3: Print a message if the guess is not in the word
            print(f"Sorry, {guess} is not in the word. Try again.")
    else:
        # Step 5: Print an error message if the input is not valid
        print("Invalid letter. Please, enter a single alphabetical character.")
