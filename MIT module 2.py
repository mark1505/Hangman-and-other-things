# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "wordslong.txt"


def load_words():
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


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''

    test = []
    for letter in secret_word:
        if letter in letters_guessed:
            test.append(1)
        else:
            test.append(0)
    if sum(test) == len(secret_word):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''

    letters = ["_ "]*len(secret_word)
    for i in range(len(secret_word)):
        for let in letters_guessed:
            if secret_word[i] == let:
                letters[i] = let
    return ''.join(letters)

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    import string
    al = string.ascii_lowercase
    al = list(al)
    for i in range(len(al)):
        for let in letters_guessed:
            if al[i] == let:
                al[i] = ""
    al = "".join(al)
    return al


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_remaining = 8
    warnings_remaining = 2
    letters_guessed = []
    compliment = ["Well done!", "Correct!", "That's one!"]
    vowels = list("aeiou")
    consonants = list("bcdfghjklmnpqrstvwxyz")
    print("You have initiated a game of hangman!")
    print("I am thinking of a word that's", len(secret_word), "letters long.")
    print("You have", warnings_remaining, "warnings remaining")
    print("-------------")
    print("You have", guesses_remaining, "guesses remaining")
    print("Available letters: abcdefghijklmnopqrstuvwxyz")
    # entered_letter = str.lower(input("Please guess a letter: "))

    while True:
        entered_letter = str.lower(input("Please guess a letter: "))
        if len(entered_letter) > 1:
            print("Enter a real letter fool!")
            continue

        # This is if the same letter has been entered twice and warnings are remaining
        if entered_letter in letters_guessed and warnings_remaining >= 1:
            letters_guessed.append(entered_letter)
            warnings_remaining = warnings_remaining - 1
            print("You've already guessed that letter, dumbass!. You have", warnings_remaining, "warnings remaining.", get_guessed_word(secret_word, letters_guessed))
            print("-------------")
            print("You have", guesses_remaining, "guesses remaining.")
            print("Available letters:", get_available_letters(letters_guessed))

        # This is if symbols or numbers are entered instead of letters and warnings are remaining
        elif not str.isalpha(entered_letter) and warnings_remaining >= 1:
            letters_guessed.append(entered_letter)
            warnings_remaining = warnings_remaining - 1
            print("Enter a real letter, you fool. You have", warnings_remaining, "warnings left.", get_guessed_word(secret_word, letters_guessed))
            print("-------------")
            print("You have", guesses_remaining, "guesses remaining.")
            print("Available letters:", get_available_letters(letters_guessed))

        # This is if out of warnings
        elif not str.isalpha(entered_letter) and warnings_remaining == 0:
            letters_guessed.append(entered_letter)
            guesses_remaining = guesses_remaining - 1
            print("That is not a valid letter:", get_guessed_word(secret_word, letters_guessed))
            print("-------------")
            print("You have", guesses_remaining, "guesses left.")
            print('Available letters:', get_available_letters(letters_guessed))
            if guesses_remaining == 0:
                print("-------------")
                print("You ran out of guesses. The word was", secret_word)
                break
        elif (entered_letter in letters_guessed) and warnings_remaining == 0:
            letters_guessed.append(entered_letter)
            guesses_remaining = guesses_remaining - 1
            print("You have already guessed that letter:", get_guessed_word(secret_word, letters_guessed))
            print("-------------")
            print("You have", guesses_remaining, "guesses left.")
            print("Available letters:", get_available_letters(letters_guessed))
            if guesses_remaining == 0:
                print("-------------")
                print('You ran out of guesses. The word was', secret_word)
                break

        #Enter the correct letter
        elif (entered_letter in secret_word) and not (entered_letter in letters_guessed):
            letters_guessed.append(entered_letter)
            print(random.choice(compliment), get_guessed_word(secret_word, letters_guessed))
            print("-------------")
            print("You have", guesses_remaining, "guesses left.")
            print("Available letter:", get_available_letters(letters_guessed))

        #Enter the wrong letter
        elif (entered_letter not in secret_word) and str.isalpha(entered_letter) and (
                    entered_letter not in letters_guessed):
            guesses_remaining = guesses_remaining - 1 if entered_letter in consonants else guesses_remaining - 2

            letters_guessed.append(entered_letter)
            print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))

            if guesses_remaining > 0:
                print('-------------')
                print('You have', guesses_remaining, 'guesses left.')
                print('Available letters:', get_available_letters(letters_guessed))
            else:
                print('-------------')
                print('Sorry, you ran out of guesses. The word was', secret_word)
                break

        # ALL WORDS HAVE BEEN GUESSED
        if is_word_guessed(secret_word, letters_guessed):
            print('-------------')
            print('Congratulations, you won!')
            print('Your total score for this game is:', guesses_remaining * len(secret_word))
            break


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

# secret_word = choose_word(wordlist)
# hangman_with_hints(secret_word)