#!/usr/bin/env python3

import random
import ast

categories = ['food']
num_categories = len(categories)

def header():
    print('/=======================\\\n'
          '| Welcome to Hangman!!! |\n'
          '\\=======================/\n')

def choose_category():
    print('Choose a category:')
    for idx, cat in enumerate(categories):
        print('{}. {}'.format(idx + 1, cat))
    while True:
        try:
            n = ast.literal_eval(input())
            if n < 1 or n > num_categories:
                raise ValueError
            break
        except ValueError:
            print('Invalid number, try again.')
    return categories[n - 1]

def getword(category):
    with open(category + '.txt') as f:
        words = f.readlines()
    return random.choice(words).rstrip('\n')

def hangman():
    header()
    word = getword(choose_category())
    print('Congratulations, you chose a category!')
    print('You won!')

if __name__ == '__main__':
    hangman()
    
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
