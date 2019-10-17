import re

with open("text.txt", "r") as file:
    content = file.read()
    # print(content)

patern1 = r'(?<=\w[.!?])'

words = re.compile('\w+')
print(words.findall(content))



#patern2 = re.findall("(\w)" , content)

#print(patern2)

#result = re.split(patern1, content)

#print(result)

