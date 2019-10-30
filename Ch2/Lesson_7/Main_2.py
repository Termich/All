from Main import Word
from Main import Sentence

class Noun(Word):
    def __init__(self):
        self.__grammar = "сущ"

class Verb(Word):
    def __init__(self):
        self.__grammar = "гл"




words = []
words.append(Noun("собака"))
words.append(Verb("ела"))
words.append(Noun("колбасу"))
words.append(Noun("кот"))


