class Word:
    def text(self):
        text = self.text
        print(text)

    def Sentence(self):
        Sentence = self.Sentence
        print(Sentence)

    def __init__(self, word, part, content):
        self.word = word
        self.part = part
        self.content = []
        self.words = [["собака", "сущ"],
                      ["ела", "глагол"],
                      ["колбасу", "сущ"],
                      ["вечером", "наречие"]]
