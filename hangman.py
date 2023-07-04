# modules imported
import random
import re

# create a greeting
print("\n")
print("=" * 41)
print("=  Hello! Welcome to the Hangman Game!  =")
print("=" * 41)

# a word list
wordlist = ["apple", "xylophone", "osmosis", "capybara", "hermes", "computer", "josephine", "theremin", "papaya", "pangolin", "theodore", "oscilloscope"]

# randomly choose a word from the wordlist
secret_word = random.choice(wordlist)
# print(secret_word)
print("\n")

displayed_guesses = [] # displays letters already guessed and blanks left
game_over = 0 # tracks how many guesses used already
guessed_already = [] # tracks letters that have been guessed already

# populates displayed_guesses
for letter in secret_word:
    displayed_guesses += "_"

# ask the user to guess a letter 
print("""A word from a list of words has been randomly chosen. 
Guess a letter in the  word. 
You get as many guesses as there are letters in the secret word. 
Good luck!\n""")

# displays how many guesses you get      
print("The secret word: ")
print(displayed_guesses)
print("You get " + str(len(secret_word)) + " guesses.\n")

# while loop that checks whether there are still blanks and if guesses have been used up
while "_" in displayed_guesses and game_over < len(secret_word):  
    # take input from the user and make it lowercase
    guess = input("Guess a letter in the secret word >> ").lower()
    # print(guess)

    # checks if the letter is not in the secret word
    if guess not in secret_word:
        print("That letter's not in the secret word")

    # checks if a letter has been guessed already
    if guess in guessed_already:
        print("You've guessed that letter already")
    else:
    # checks if the letter is in the word
        for i in range(len(secret_word)):
            letter = secret_word[i]
            if letter == guess:
                displayed_guesses[i] = letter
        # appends guess to guessed_already list
        guessed_already.append(guess)

    # print(guessed_already)
    print(displayed_guesses)

    # adds 1 to how many guesses have been used
    game_over += 1 

    # displays how many guesses you have left
    # guesses_left is turned from an integer into a string
    guesses_left = str(len(secret_word) - game_over)
    # checks for a tiny little grammatical error
    if guesses_left == '1': 
        print(f"You have {guesses_left} guess left.\n")
    else:
        print(f"You have {guesses_left} guesses left.\n")

# detects if guesses have been used up
if game_over >= len(secret_word) and secret_word != ''.join(displayed_guesses):
    print("~" * 53)
    print(f"The secret word was {secret_word}.")
    print("\nYou've run out of guesses. Better luck next time :(")
    print("~" * 53)
    print("\n")
else:
    # victory message
    print("*" * 40)
    print("\nCongratulations! You guessed the word!\n")
    print("*" * 40)
    print("\n")