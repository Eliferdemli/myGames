import os
print(os.getcwd())
os.chdir("C:\\Users\\xxxx\\xxxx\\xxxx\\HangmanGame")  # change directory
# words.txt must be in the directory

import random
WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


# QUESTION 1
def isWordGuessed(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    """

    secretWordList = list(set(secretWord))
    comparisonList = [i for i in lettersGuessed if i in secretWordList]  # if an item in the lettersGuessed is also in the secretWordList add in comparisonList
    return sorted(secretWordList) == sorted(comparisonList)


# QUESTION 2
def getGuessedWord(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    """

    n = len(secretWord)
    guessWordList = list(n * "_")
    locs = []  # initialize the index list
    secretWordList = list(secretWord)
    # get the common letters in comparisonList
    comparisonList = [i for i in lettersGuessed if i in secretWordList]
    # get the indices of duplicates (after 1st occurrence):
    duplicates = [idx for idx, val in enumerate(secretWordList) if
                  val in (secretWordList[:idx] and comparisonList)]
    for letter in comparisonList:
        if letter in secretWordList:  # this is for the non duplicates (1st occurrence)
            locs.append(secretWordList.index(letter))
    # extend the locs list with the indices of duplicate values:
    locs.extend(duplicates)

    for i in locs:
        guessWordList[i] = secretWordList[i]
    guessWord = "".join(guessWordList)
    return guessWord


# QUESTION 3
def getAvailableLetters(lettersGuessed):
    """
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """

    import string
    availableletters = ""
    guess = "".join(lettersGuessed)
    guessLower = guess.lower()
    for letter in string.ascii_lowercase:
        if letter not in guessLower:
            availableletters = availableletters + letter
    return availableletters


# QUESTION 4
def hangman(secretWord):
    """
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many
      letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    """


    import string
    # initial conditions:
    countguess = 8  # the max number of guesses available for player
    lettersGuessed = []
    playerGuessList = []
    ExitCase = False

    # Game Opens:
    print("Welcome to the game, Hangman!\nI am thinking of a word that is " + str(len(secretWord)) + " long.")
    # Main Gain Loop depends on my Counter:
    while countguess > 0:
        print("------------")
        print("You have " + str(countguess) + " guesses left.")
        availableLetter = getAvailableLetters(lettersGuessed)
        print("Available letters: " + getAvailableLetters(lettersGuessed))
        playerGuess = input('Please guess a letter: ').lower()
        playerGuessList.append(playerGuess)
        lettersGuessed=list(set(playerGuessList))

        ExitCase = isWordGuessed(secretWord, lettersGuessed)
        if ExitCase == True:
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            print("------------")
            print("Congratulations, you won!")
            break
        elif ExitCase == False:
            if playerGuess not in availableLetter:
                print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            elif playerGuess in secretWord:
                print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            else:
                print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
                countguess -= 1
                if countguess == 0:
                    print("------------")
                    print("Sorry, you ran out of guesses. The word was " + secretWord + ".")
                    break


# Example:
secretWord = "ghostlovescore"
hangman(secretWord)















