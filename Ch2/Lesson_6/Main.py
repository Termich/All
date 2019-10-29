class Word:

    def __init__(self, text, part):
        self.text = text
        self.part = part


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


li = [["собака", "сущ"],
      ["ела", "глагол"],
      ["колбасу", "сущ"],
      ["вечером", "наречие"]]

papana = Sentence([0, 1, 2, 3])
banana = Word("собака", "сущ")
apana = Word("ела", "глагол")

words = [Word(word[0], word[1]) for word in li]

print(papana.show())
print(papana.show_parts())




# for word in li:
#     words.append(Word(word[0], word[1]))


# content = [3,0,1,2]
# sentence = ' '.join([words[x].text for x in content])
# # sentence =[]
# # for x in content:
# #     sentence.append(words[x].text)
# # sentence = ' '.join(sentence)
# print(sentence)


# for i in range(len(words1)):
#     words1[i] = Word(words1[i][0], words1[i][1])


# print(papana.show())
# print(words[0].text)
# print(banana.text, apana.text)
# print(banana.part, apana.part)
