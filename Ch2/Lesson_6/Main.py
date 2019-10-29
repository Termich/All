class Word:

    def __init__(self, text, part):
        self.text = text
        self.part = part


class Sentence:

    def __init__(self, text, part):
        self.content = []
        self.words = [["собака", "сущ"],
                      ["ела", "глагол"],
                      ["колбасу", "сущ"],
                      ["вечером", "наречие"]]



banana = Word("собака","сущ")
apana = Word("ела","глагол")

print(banana.text,apana.text)
print(banana.part,apana.part)
