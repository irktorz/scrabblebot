# Reads the text file full of acceptable words in Scrabble and makes an array out of it
# text file taken from https://github.com/redbo/scrabble/blob/master/dictionary.txt
class WordSet:
    def __init__(self, filename):
        self.words = self._load_words(filename)

    def _load_words(self, filename):
        with open(filename, "r") as f:
            return set(word.strip() for word in f)

    def contains_word(self, word):
        return word in self.words

    def get_all_word(self):
        return self.words
