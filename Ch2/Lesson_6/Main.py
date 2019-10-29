class Word:

    def __init__(self, text, part):
        self.text = text
        self.part = part


class Sentence:

    def __init__(self, content):
        self.content = content

    def show(self):
        for x in words:
            words.append(Word(x[0], x[1]))





li = [["собака", "сущ"],
          ["ела", "глагол"],
          ["колбасу", "сущ"],
          ["вечером", "наречие"]]

papana = Sentence([0,1,2,3])
banana = Word("собака", "сущ")
apana = Word("ела", "глагол")

words = []
for word in li:
    words.append(Word(word[0], word[1]))

# for i in range(len(words1)):
#     words1[i] = Word(words1[i][0], words1[i][1])




print(papana.content)
print(words[0].text)
print(banana.text, apana.text)
print(banana.part, apana.part)
