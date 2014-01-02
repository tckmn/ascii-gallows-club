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