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
    input()

if __name__ == '__main__':
    hangman()


#input guess
def get_guess():
    guess = input('Guess: ')
    while guess in guesses:
        guess = input('You already guessed that. Try again: ')
    return guess

def draw_board(bad_guesses, word):
    # OH NO this method has an error
    # MUST FIX LATER BLAH OH NO AHHHHHH
    # the """ ... """ strings are causing indentation problems.
    
    hangs = list(map(lambda x: x.strip('\n'), [
"""
|
|
|
|
""","""
|            O
|
|
|
""","""
|            O
|            |
|            |
|
""","""
|          __O
|            |
|            |
|
""","""
|          __O__
|            |
|            |
|
""","""
|          __O__
|            |
|            |
|           /
""","""
|          __O__
|            |
|            |
|           / \\
"""
    ]))

    # This is always drawn
    print("""______________
| /          |
|/           |""")

    # different level of hang-ness
    print(hangs[bad_guesses])

    # this is also always drawn
    print("""|
|
|
|________________|
""")

    spaces = ' '.join(['__'] * len(word))

    # draw spaces - need to put a function here to insert correct guesses in right location
    print(spaces)

    # Fill print word on spaces using variation of afore-said function
    if bad_guesses >= 6:
        print("You could not guess the number. It was {0}".format(word))
