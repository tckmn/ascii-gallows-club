#!/usr/bin/env python3

import random # for choosing a word
import os # for finding files in wordlists directory
import textwrap # for ASCII art dedentation
import time # for sleeping at the end
import getpass # for 2 player

# grab all the filenames
categories = [f.split('.')[0] for f in os.listdir('wordlists')]

debug_mode = input('Debug mode? (y/n): ').lower() == 'y'
def debug(s):
    if debug_mode: print('[DEBUG] ' + s)

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
    for i, cat in enumerate(categories):  # print the categories & numbers
        print('%i. %s' % (i, cat))
    choice = input('Please enter a category name or number: ').lower()
    if choice.isdigit() and 0 <= int(choice) < len(categories):
        choice = categories[int(choice)]
    for i, cat in enumerate(categories):
        if choice == str(i): choice = cat
    while choice not in categories:  # loop until user enters a valid category
        choice = input('Invalid category. Try again: ')
        if choice.isdigit() and 0 <= int(choice) < len(categories):
            choice = categories[int(choice)]
    return choice

def get_word(category):
    "Retrieve a random word from a category."
    with open('wordlists/%s.txt' % category) as f: # use `with` for automatic file closure
        words = f.readlines()
    return random.choice(words).rstrip('\n').lower().strip()

def get_guess(guessed):
    "Get the user to guess a letter."
    guess = input('Guess: ').lower()
    while guess in guessed or len(guess) != 1: # guess has to be a single letter
        guess = input('You already guessed that. Try again: ' if guess in guessed else 'You must guess a single letter: ').lower()
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
        |________________|""" % ' '.join(map(lambda s: '[%s]' % s, bad_guesses))).strip('\n'))

def hangman(word):  # main function
    """
    Plays hangman!
    Returns True if the user won, False otherwise.
    """

    debug('The word is %s' % word)

    # the lines showing the word so far
    guess = ['_' if char.isalnum() else char for char in word]

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
                print('/nCongratulations, you guessed the word: %s!' % word)
                return True # TODO add replay functionality?
        else:
            bad_guesses.append(letter)
            print('%s is not in the word.' % letter)

        # add a little separation
        draw_board(bad_guesses, word)

    # if program reaches here, user failed
    print('You couldn\'t guess the word. It was %s.' % word)
    return False

if __name__ == '__main__':
    header()
    players = input('How many players? 1 for playing against computer, 2 for playing against another human: ')
    while players not in ['1', '2']:
        players = input('Invalid input. Please try again: ')
    print() # spacing

    if players == '1':
        wins, losses = 0, 0
        if hangman(get_word(choose_category())): wins += 1
        else: losses += 1
        while True:
            print('You have won %i times and lost %i times.' % (wins, losses))
            again = input('Play again? (y/n): ').lower() == 'y'
            print() # separation
            if again:
                if hangman(get_word(choose_category())): wins += 1
                else: losses += 1
            else:
                break
    else:
        while True:
            word = getpass.getpass('Word maker: enter your word (the input will not be shown): ')
            hangman(word)
            again = input('Play again? (y/n): ').lower() == 'y'
            print() # separation
            if not again: break

    print('Goodbye!')
    time.sleep(2)
