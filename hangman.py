#!/usr/bin/env python3

import random
import os
import textwrap

# grab all the filenames
categories = [f.split('.')[0] for f in os.listdir('wordlists')]

def header():
    "Print the header."
    print('/=======================\\\n'
          '| Welcome to Hangman!!! |\n'
          '\\=======================/\n')

def choose_category():
    "Request the user to input a category."
    for cat in categories:  # print the categories
        print(cat)
    choice = input('Please enter a category name: ')
    while choice not in categories:  # loop until user enters a valid category
        choice = input('Invalid category. Try again: ')
    return choice

def get_word(category):
    "Retrieve a random word from a category."
    with open('wordlists/%s.txt' % category) as f: # use `with` for automatic file closure
        words = f.readlines()
    return random.choice(words).rstrip('\n')

def get_guess(guessed):
    "Get the user to guess a letter."
    guess = input('Guess: ')
    while guess in guessed or len(guess) != 1:  # guess has to be a single letter
        guess = input('You already guessed that. Try again: ')
    return guess

def draw_board(bad_guesses, word):
    "Draw the gallows."

    # ASCII art data
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
        |________________|""").strip('\n'))

def hangman():  # main function
    "Play hangman!"
    header()
    word = get_word(choose_category())
    print('The word is %s (for debugging purposes)' % word)

    # the lines showing the word so far
    guess = ['_' if char != ' ' else ' ' for char in word]

    # already guessed and wrong guesses
    guessed = []
    bad_guesses = []
    while len(bad_guesses) < 6: # main loop
        # print letters so far
        print(' '.join(guess))

        # request input
        letter = get_guess(guessed)
        guessed.append(letter)

        # check if letter is correct or not
        if letter in word:
            # update chars guessed so far
            guess = [letter if char == letter else guess_char for char, guess_char in zip(word, guess)]

            # did they win?
            if ''.join(guess) == word:
                print('Congratulations, you guessed the word: %s!' % word)
                return # TODO add replay functionality?
        else:
            bad_guesses.append(letter)
            print('%s is not in the word.' % letter)

        # separate
        print()
        draw_board(len(bad_guesses), word)

    # if program reaches here, user failed
    print('You couldn\'t guess the word. It was %s.' % word)

if __name__ == '__main__':
    hangman()
