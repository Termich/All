class Word:

    def __init__(self, text, part):
        self.text = text
        self.part = part


class Sentence:

    # words = [["собака", "сущ"],
    #          ["ела", "глагол"],
    #          ["колбасу", "сущ"],
    #          ["вечером", "наречие"]]

    def __init__(self, words):
        self.content = words[["собака", "сущ"],
             ["ела", "глагол"],
             ["колбасу", "сущ"],
             ["вечером", "наречие"]]


banana = Word("собака", "сущ")
apana = Word("ела", "глагол")
papana = Sentence(0,2)


print(papana.content)
print(banana.text, apana.text)
print(banana.part, apana.part)
