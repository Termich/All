from Main import Word
from Main import Sentence

class Noun(Word):
    def __init__(self,grammar):
        self.__grammar = grammar

class Verb(Word,grammar):
    def __init__(self):
        self.__grammar = grammar

        
print(papana.show())
print(papana.show_parts())