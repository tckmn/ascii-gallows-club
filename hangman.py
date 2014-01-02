#!/usr/bin/env python3

import random # for choosing a word
import os # for finding files in wordlists directory
import textwrap # for ASCII art dedentation
import time # for sleeping at the end

# grab all the filenames
categories = [f.split('.')[0] for f in os.listdir('wordlists')]

def print_ASCII(ascii_str):
    "Print ASCII art."
    print(textwrap.dedent(ascii_str))

def header():
    "Print the header."
    print_ASCII("""
        /=======================\\
        | Welcome to Hangman!!! |
        \\=======================/
    """)

def choose_category():
    "Request the user to input a category."
    for cat in categories:  # print the categories
        print(cat)
    choice = input('Please enter a category name: ').lower()
    while choice not in categories:  # loop until user enters a valid category
        choice = input('Invalid category. Try again: ')
    return choice

def get_word(category):
    "Retrieve a random word from a category."
    with open('wordlists/%s.txt' % category) as f: # use `with` for automatic file closure
        words = f.readlines()
    return random.choice(words).rstrip('\n').lower().strip()

def get_guess(guessed):
    "Get the user to guess a letter."
    guess = input('Guess: ')
    while guess in guessed or len(guess) != 1: # guess has to be a single letter
        guess = input('You already guessed that. Try again: ' if guess in guessed else 'You must guess a single letter: ')
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
    print_ASCII("""
        ______________
        | /          |
        |/           |""")

    # different level of hang-ness
    print(hangs[len(bad_guesses)])

    # this is also always drawn
    print_ASCII(("""
        |
        |
        | %s
        |________________|""" % ' '.join(bad_guesses)).strip('\n'))

def hangman():  # main function
    """
    Plays hangman!
    Returns True if the user won, False otherwise.
    """

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
                return True # TODO add replay functionality?
        else:
            bad_guesses.append(letter)
            print('%s is not in the word.' % letter)

        # add a little separation
        print()
        draw_board(bad_guesses, word)

    # if program reaches here, user failed
    print('You couldn\'t guess the word. It was %s.' % word)
    return False

if __name__ == '__main__':
    header()
    wins, losses = 0, 0
    if hangman(): wins += 1
    else: losses += 1
    while True:
        print('You have won %i times and lost %i times.' % (wins, losses))
        again = input('Play again? (y/n): ').lower() == 'y'
        if again:
            if hangman(): wins += 1
            else: losses += 1
        else:
            break
    print('Goodbye!')
    time.sleep(2)
