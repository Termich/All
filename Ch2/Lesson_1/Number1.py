import re

with open("text.txt", "r") as file:
    content = file.read()
    # print(content)

patern1 = r'(?<=\w[.!?])'
patern2 = re.findall("\w+\.{3}" , content)

print(patern2)

result = re.split(patern1, content)

#print(result)

