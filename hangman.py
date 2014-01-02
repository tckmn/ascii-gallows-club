#!/usr/bin/env python3

import random
import os
import textwrap

categories = [f.split('.')[0] for f in os.listdir('wordlists')]  # avoid having to put everything in memory?

def header():
    "Print the header."
    print('/=======================\\\n'
          '| Welcome to Hangman!!! |\n'
          '\\=======================/\n')

def choose_category():
    for cat in categories:  # print the categories
        print(cat)
    choice = input('Please enter a category name: ')
    while choice not in categories:  # loop until user enters a valid category
        choice = input('Invalid category. Try again: ')
    return choice

def get_word(category):
    "Retrieve a random word from a category."
    with open('wordlists/%s.txt' % category) as f:  # use `with` for automatic file closure
        words = f.readlines()
    return random.choice(words).rstrip('\n')  # does returning inside a `with` still close the file?

def get_guess(guessed):
    "Get the user to guess a letter."
    guess = input('Guess: ')
    while guess in guessed or len(guess) != 1:  # guess has to be a single letter
        guess = input('You already guessed that. Try again: ')
    return guess

def draw_board(bad_guesses, word):
    "Draw the gallows."

    hangs = list(map(lambda x: textwrap.dedent(x).strip('\n'), ["""
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
    print(textwrap.dedent("""
        ______________
        | /          |
        |/           |"""))

    # different level of hang-ness
    print(hangs[bad_guesses])

    # this is also always drawn
    print(textwrap.dedent("""
        |
        |
        |
        |________________|
    """))

    spaces = ' '.join(['__'] * len(word))

    # draw spaces - need to put a function here to insert correct guesses in right location
    print(spaces)

def hangman():  # main function
    "Play hangman!"
    header()
    word = get_word(choose_category())
    print('The word is', word)  # for debugging purposes
    guess = ['_' if char != ' ' else ' ' for char in word]
    guessed = []
    bad_guesses = []
    for _ in range(6):  # main loop
        print(' '.join(guess))
        letter = get_guess(guessed)
        guessed.append(letter)
        if letter in word:
            guess = [letter if char == letter else guess_char for char, guess_char in zip(word, guess)]
            if ''.join(guess) == word:
                print('Congratulations, you guessed the word: {}!'.format(word))
                return  # add replay functionality?
        else:
            bad_guesses.append(letter)
            print(letter, 'is not in the word.')
        print()
        draw_board(len(bad_guesses))
    print('You couldn\'t guess the word. It was', word)

if __name__ == '__main__':
    hangman()
