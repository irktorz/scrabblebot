from random import choice
from collections import Counter
import itertools
from WordSet import *


class Scrabble:
    def __init__(self):
        self.word_set = WordSet("scrabble_bot/scrabble_words.txt")
        self.available = self.generate_letters()
        self.hand = self.generate_hand(self.available)
        self.points = {1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
                       2: ['D', 'G'],
                       3: ['B', 'C', 'M', 'P'],
                       4: ['F', 'H', 'V', 'W', 'Y'],
                       5: ['K'],
                       8: ['J', 'X'],
                       10: ['Q', 'Z'],
                       0: '%'}

    # generates all letters available in a standard game of Scrabble
    def generate_letters(self):
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
                letters.append("%")

        return letters

    # Generate a new hand and remove the letters drawn from available letters
    def generate_hand(self, available):
        hand = []
        for i in range(7):
            let = choice(available)
            hand.append(let)
            self.available.remove(let)

        self.hand = hand
        return hand

    def possible_words(self, hand):
        words = WordSet("scrabble_bot/scrabble_words.txt")
        combos = []

        # create an array of possible words by comparing all combinations to the word set
        for i in range(len(hand) + 1):
            for subset in itertools.permutations(hand, i):
                # turn the list of characters into a string
                wr = ''.join(subset)
                if wr in words.get_all_word() and wr not in combos:
                    combos.append(wr)

        for wrds in combos:
            word_value = 0
            for ltr in wrds:
                for i in self.points:
                    if ltr in self.points[i]:
                        letter_value = i
                word_value = word_value + letter_value

            print(wrds, word_value)

        return combos

    # returns the hand
    def get_hand(self):
        return self.hand

    # returns the available letters
    def get_available(self):
        return self.available


def main():
    # Generates an inital hand and all the letters available after the hand has been made
    game = Scrabble()

    # Display hand
    print(game.get_hand())

    # Display possible words
    game.possible_words(game.get_hand())


# compare any given hand to the Scrabble words list to find possible words


main()
