import re

with open("text.txt", "r", encoding='utf-8') as file:
    content = file.read()
 #   print(content)
print(content)

patern1 = re.compile('[\.\?!]\s+')
result = re.split(patern1, content)
#print(result)


words = re.compile('\w{4,}')
# print(words.findall(content))





#patern2 = re.findall("(\w)" , content)

#print(patern2)

links = re.compile('[\w]+\.[\w]+')
print(links.findall(content))
#print(links)



