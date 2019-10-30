
class Word:
    def __init__(self, text):
        self.text = text

class Sentence:

    def __init__(self, content):
        self.content = content


    def show(self):
        sentence = ' '.join([words[x].text for x in self.content])
        return sentence


    def show_parts(self):
        parts = [words[x].part for x in self.content]
        parts = list(set(parts))
        return parts

class Noun(Word):
    __grammar = "сущ"
    # def __init__(self):


class Verb(Word):
    __grammar = "гл"
    # def __init__(self):


words = []
words.append(Noun("собака"))
words.append(Verb("ела"))
words.append(Noun("колбасу"))
words.append(Noun("кот"))


