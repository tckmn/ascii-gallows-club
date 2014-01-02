print 'This game is so fun right'
print 'You won'

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
