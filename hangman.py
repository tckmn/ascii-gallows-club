#!/usr/bin/env python3

import random
import os

categories = [f.split('.')[0] for f in os.listdir('wordlists')]  # avoid having to put everything in memory?

def header():
    "Print the header."
    print('/=======================\\\n'
          '| Welcome to Hangman!!! |\n'
          '\\=======================/\n')

def choose_category():
    "Get the user to choose a category."
    print('Choose a category:')
    for cat in categories:  # print the categories
        print(cat)
    while True:  # loop until user enters a valid category
        choice = input('Please enter a category name: ')
        if choice in categories:
            return choice
        else:
            print('Invalid category. Please try again.')

def getword(category):
    "Retrieve a random word from a category."
    with open(category + '.txt') as f:  # use `with` for automatic file closure
        words = f.readlines()
    return random.choice(words).rstrip('\n')
    
def draw_board(bad_guesses):
    "Draw the gallows."
    # This is always drawn
    print("______________")
    print("| /          |")
    print("|/           |")

    # different level of hang-ness
    if bad_guesses == 0:
        print("|")
        print("|")
        print("|")
        
    elif bad_guesses == 1:
        print("|            O")
        print("|")
        print("|")
        print("|")

    elif bad_guesses == 2:
        print("|            O")
        print("|            |")
        print("|            |")
        print("|")

    elif bad_guesses == 3:
        print("|          __O")
        print("|            |")
        print("|            |")
        print("|")

    elif bad_guesses == 4:
        print("|          __O__")
        print("|            |")
        print("|            |")

    elif bad_guesses == 5:
        print("|          __O__")
        print("|            |")
        print("|            |")
        print("|           /")

    else:
        print("|          __O__")
        print("|            |")
        print("|            |")
        print("|           / \\")

    # this is also always drawn
    print("|")
    print("|")
    print("|")
    print("|________________|")

    spaces = "__"
    for i in range(1, len(word)):
        spaces = spaces + " __"

    # draw spaces - need to put a function here to insert correct guesses in right location
    print(spaces)

    # Fill print word on spaces using variation of afore-said function 
    if bad_guesses >= 6:
        print("You could not guess the word. It was {}".format(word))

def hangman():  # main function
    "Play hangman!"
    header()
    word = getword(choose_category())
    print('The word is', word)  # for debugging purposes
    guess = ['_' if char != ' ' else ' ' for char in word]
    guessed = []
    # insert main loop here

if __name__ == '__main__':
    hangman()