# 1. Создайте класс Word. (Вспомните, какое зарезервированное слово используется для создания класса).
class Word:
    # 2. Добавьте свойства text (класс будет хранить слово)
    # и part (часть речи, которой является слово. Например, существительное, прилагательное и т.п.). Для добавления свойств воспользуйтесь методом __init__.
    def __init__(self, text, part):
        self.text = text
        self.part = part


# 4. Создайте класс Sentence. (по аналогии с п. 1).
class Sentence:
    # 5. Добавьте свойство content. (по аналогии с п. 2).
    def __init__(self, content):
        self.content = content

    # 7. Добавьте в класс Sentence метод show, составляющий предложение.
    # Метод должен перебирать числа из свойства content и подставлять соответствующие слова,
    # которые хранятся в свойстве text экземпляров класса Word.
    # Данные извлекаем из списка words, который получили на прошлом шаге.
    # При соединении слов в предложение не забудьте добавить пробел между словами.
    def show(self):
        sentence = ' '.join([words[x].text for x in self.content])
        return sentence

    # 8. Добавьте в класс Sentence метод show_parts, отображающий, какие части речи входят в предложение.
    # По аналогии с п. 7 перебирайте в цикле числа из свойства content и сохраняйте результат в отдельный список.
    # Учтите, что части речи могут повторяться, но список не должен содержать дубликаты.

    def show_parts(self):
        parts = [words[x].part for x in self.content]
        parts = list(set(parts))
        return parts


li = [["собака", "сущ"],
      ["ела", "глагол"],
      ["колбасу", "сущ"],
      ["вечером", "наречие"]]

papana = Sentence([0, 1, 2, 3])
# 3. Создайте экземпляр класса Word, передав в качестве параметров любое слово и указав его часть речи.

banana = Word("собака", "сущ")
apana = Word("ела", "глагол")
# print(banana.text, apana.text)
# print(banana.part, apana.part)

# . Создайте из массива (можете взять приведённый выше или придумать свой)
# список, каждый элемент которого является экземпляром класса Word.
# Примечание: список list (назовём его words) — отдельная переменная, не относящаяся к классам Word и Sentence.

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
