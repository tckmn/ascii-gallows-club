#!/usr/bin/env python3

import random
import os

words = {}
for f in os.listdir('wordlists'): words[f.split('.')[0]] = open('wordlists/' + f).readlines()

def header():
    print('/=======================\\\n'
          '| Welcome to Hangman!!! |\n'
          '\\=======================/\n')

def choose_category():
    print('Choose a category:')
    print('\n'.join(words.keys()))
    while True:
        choice = input('Please enter a category name: ')
        if choice in words.keys(): return choice

def getword(category):
    return random.choice(words[category]).rstrip('\n')

def hangman():
    header()
    word = getword(choose_category())
    print('The word is %s' % word)

if __name__ == '__main__':
    hangman()
    

#input guess
def get_guess():
    guess = input('Guess: ')
    while guess in guesses:
        guess = input('You already guessed that. Try again: ')
    return guess

def draw_board(bad_guesses):

    # This is always drawn
    print("______________")
    print("| /          |")
    print("|/           |")

    # different level of hang-ness
    if bad_guesses is 0:
        print("|")
        print("|")
        print("|")

    elif bad_guesses is 1:
        print("|            O")
        print("|")
        print("|")
        print("|")

    elif bad_guesses is 2:
        print("|            O")
        print("|            |")
        print("|            |")
        print("|")

    elif bad_guesses is 3:
        print("|          __O")
        print("|            |")
        print("|            |")
        print("|")

    elif bad_guesses is 4:
        print("|          __O__")
        print("|            |")
        print("|            |")

    elif bad_guesses is 5:
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
        print("You could not guess the number. It was {0}".format(word))
