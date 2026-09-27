 # CMSC 140, Spring 2026, Final Project, hangman.py
#
# Name: Fidel F. Ovalle
#
# Honor Code: IHRTLUHC
#
# Hangman Game
# -----------------------------------
# Helper code
# You do not need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
        # inFile: file
    inFile = open("words.txt", 'r')
        # line: string
    line = inFile.readline()
        # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # check if every letter in the secret word has been guessed
    for letter in secret_word:

        found = False

        for guess in letters_guessed:
            if letter == guess:
                found = True

        if found == False:
            return False

    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessWord = " "

    # check each letter in secret
    for letter in secret_word:

        if letter in letters_guessed:
            guessWord = guessWord + letter

        else:
            missing = "_ "
            guessWord = guessWord + missing

    return guessWord

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    lettersLeft = ""

    # builds a string of letters that has not been guessed
    for letter in string.ascii_lowercase:
        
        if letter not in letters_guessed:
                lettersLeft = lettersLeft + letter
                   
    return lettersLeft

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses remain.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      remain and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the project write-up.
    '''
    # keep track of guesses, warnings, and guessed letters
    guessesLeft = 6
    warningsLeft = 3
    letters_guessed = []

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have", warningsLeft, "warnings left.")
    print("-------------")

    # Loop checking win or lose
    while guessesLeft > 0 and not is_word_guessed(secret_word, letters_guessed):
        print("You have", guessesLeft, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))

        # gets user input as guess and puts it lowercase
        userGuess = input("Please type in a letter: ")
        userGuess = userGuess.lower()

        # check if input is nonletter
        if not userGuess.isalpha():

            # takes away 1 warning for invalid input
            if warningsLeft > 0:
                warningsLeft = warningsLeft - 1
                print("Oops! That is not a valid letter.")
                print("You have", warningsLeft, "warnings left:", get_guessed_word(secret_word, letters_guessed))

            # when no warnings left remove a guess
            else:
                guessesLeft = guessesLeft - 1
                print("Oops! That is not a valid letter.")
                print("You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))

        # checks if letter was already guessed    
        elif userGuess in letters_guessed:

            # check if warnings is more than 0, and then remove a warning for same guess
            if warningsLeft > 0:
                warningsLeft = warningsLeft - 1
                print("Oops! You've already guessed that letter.")
                print("You have", warningsLeft, "warnings left:", get_guessed_word(secret_word, letters_guessed))

            # remove guess if warnings are not above 0
            else:
                guessesLeft = guessesLeft - 1
                print("Oops! You've already guessed that letter.")
                print("You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))

        # adds a correct guess to list of guessed letters
        elif userGuess in secret_word:
            letters_guessed.append(userGuess)
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))

        # remove guess for letter not in word
        else:
            letters_guessed.append(userGuess)

            # check if user guess is a vowel and remove 2 guesses, if not just remove 1
            if userGuess in "aeiou":
                guessesLeft = guessesLeft - 2
            else:
                guessesLeft = guessesLeft - 1
                
            print("Oops! That letter is not in my word:")
            print("Please guess a letter:", get_guessed_word(secret_word, letters_guessed))

        print("-------------")

    # Check if player won or lost
    if is_word_guessed(secret_word, letters_guessed):

        # Calculates final score
        differentLetters = len(set(secret_word))
        score = guessesLeft * differentLetters

        # print winning message
        print("Congratulations, you won!")
        print("Your total score for this game is:", score)
    # print losing message    
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word)
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

# -----------------------------------
if __name__ == "__main__":

    restart = "y"

    while restart == "y":
               
        secret_word = choose_word(wordlist)
        hangman(secret_word)

        restart = input("Would you like to play again? y or n: ")
        restart = restart.lower()

    print("Thanks for playing!")

