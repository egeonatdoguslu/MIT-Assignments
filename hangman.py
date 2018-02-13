from time import sleep as sp
import random
file = open("words.txt", mode="r")
lets_read = file.read()
words_list = lets_read.split()
print("Loading 55,900 words...")
print(" ... \n ... \n ... \n")
sp(2)
print("Loading completed. We can play now!")
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
letters_guessed = []


def hangman():
    word = random.choice(words_list)
    lives = int(len(word)+3)
    print("Available letters for now are = {}".format(lowercase_letters))
    print("I am thinking of a word of", len(word), "letters.\n", ("_ " * len(word)))
    print("You have got {} guesses".format(lives))
    print(word)

    while not is_word_guessed(letters_guessed, word):
        ask = input("Which letter would you like to try?")
        letters_guessed.append(ask)
        if lives == 0:
            print("You ran out of lives. Sorry!")
            break
        if ask in word:
            print(get_guessed_word(word, letters_guessed))
            print(get_available_letters(letters_guessed))
            if is_word_guessed(letters_guessed, word):
                print("YAY! You guessed the word correctly!")
                other_round()
            else:
                pass
        else:
            print(get_guessed_word(word, letters_guessed))
            print("The letter you introduced could not be found in the secret word!")
            lives -= 1
            print("You have got {} guesses left!".format(lives))
            print(get_available_letters(letters_guessed))
    other_round()


def get_guessed_word(x, y):
    hint = ""
    for i in x:
        if i in y:
            hint += i
        else:
            hint += "_ "
    return hint


def is_word_guessed(x, y):
    check = ""
    for i in y:
        if i in x:
            check += i
    if len(y) == len(check):
        return True
    else:
        return False


def get_available_letters(x):
    x.sort()
    lowercase_list = [i for i in lowercase_letters]
    for i in x:
        for j in lowercase_list:
            if i == j:
                lowercase_list.remove(i)
    return "Available letters are {}".format(lowercase_list)


def other_round():
    wanna_play = input("The game ended. Would you like to play another round? If so,"
                       " please type 'yes'. Else, type 'quit'")
    if wanna_play == 'yes':
        hangman()
    elif wanna_play == 'quit':
        raise SystemExit
    else:
        print("Please give a proper answer.")
        return other_round()


hangman()
