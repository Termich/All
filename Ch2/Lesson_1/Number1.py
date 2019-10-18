import re
from collections import Counter

# Получил текст из файла
with open("text.txt", "r", encoding='utf-8') as file:
    content = file.read()

# Разбил полученный текст на предложения.
patern1 = re.compile('[\.\?!]\s+')
result = re.split(patern1, content)

# Нашел слова состоящие из 4 букв
words = re.compile('\w{4,}')

cnt = Counter(x for x in re.findall('[\w]+\.[\w]+', content))

# Отобрал все ссылки
links = re.compile('[\w\.]+\.[\w/]+')

#Возврат ссылок которые встречаються чаще всего


# Замените все ссылки на текст:
Registration = re.sub(links, "'Ссылка отобразится после регистрации'", content)


print("Получил текст из файла")
print(content)
print("Разбил текс на предложения")
print(result)
print("Нашел слова состоящие из 4-х букв")
print(words.findall(content))
print('10 самых часто используемых слов')
print(cnt.most_common(10))
print("Нашел все ссылки")
print(links.findall(content))
print("Самая часто употребляемая ссылка")
print(cnt.most_common(1))
print("Ссылка отобразиться после регистрации")
print(Registration)