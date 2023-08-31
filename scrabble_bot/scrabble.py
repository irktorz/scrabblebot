from random import choice
from collections import Counter
import itertools
#from pyglet import app, shapes
#from pyglet.window import Window
#import pyglet

# Reads the text file full of acceptable words in Scrabble and makes an array out of it
# text file taken from https://github.com/redbo/scrabble/blob/master/dictionary.txt
def create_word_set():
    f = open("scrabble_bot/scrabble_words.txt", "r")
    words = set()
    for x in f:
        x = x.replace("\n", '')
        words.add(x)

    return words

# Creates an array of all letters and blanks in a standard Scrabble game according to the Scrabble manual
def generate_letters():
    letters = []
    for i in range(100):
        if i < 9:
            letters.append('A')
        elif i < 11:
            letters.append('B')
        elif i < 13:
            letters.append('C')
        elif i < 17:
            letters.append('D')
        elif i < 29:
            letters.append('E')
        elif i < 31:
            letters.append('F')
        elif i < 34:
            letters.append('G')
        elif i < 36:
            letters.append('H')
        elif i < 45:
            letters.append('I')
        elif i < 46:
            letters.append('J')
        elif i < 47:
            letters.append('K')
        elif i < 51:
            letters.append('L')
        elif i < 53:
            letters.append('M')
        elif i < 59:
            letters.append('N')
        elif i < 67:
            letters.append('O')
        elif i < 69:
            letters.append('P')
        elif i < 70:
            letters.append('Q')
        elif i < 76:
            letters.append('R')
        elif i < 80:
            letters.append('S')
        elif i < 86:
            letters.append('T')
        elif i < 90:
            letters.append('U')
        elif i < 92:
            letters.append('V')
        elif i < 94:
            letters.append('W')
        elif i < 95:
            letters.append('X')
        elif i < 97:
            letters.append('Y')
        elif i < 98:
            letters.append('Z')
        elif i < 100:
            letters.append("BLANK")

    return letters


# compare any given hand to the Scrabble words list to find possible words
def possible_words(hand):
    words = create_word_set()
    combos = []

    # create an array of possible words by comparing all combinations to the word set
    for i in range(len(hand) + 1):
        for subset in itertools.permutations(hand, i):
            wr = ''.join(subset)   # turn the list of characters into a string
            if wr in words and wr not in combos:
                combos.append(wr)

    print(combos)
    return combos


def main():
    available = generate_letters()
    words = create_word_set()

    hand = []
    for i in range(7):
        let = choice(available)
        hand.append(let)
        available.remove(let)
    
    print(hand)
    possible_words(hand)
    

main()
