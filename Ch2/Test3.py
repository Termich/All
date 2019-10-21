import re

with open ("index.html",encoding='utf-8') as f:
    s = f.read()

#li1 = re.findall("([0-9\-\+]+) °C", s)
li = re.findall("<a class=\"home-link home-link_black_yes\" aria-label=\"([^\"]+)\" href=", s)
li1 = re.findall("<a class=\"home-link home-link_black_yes\" weather__grade\" aria-label=\"([^\"]+)\" href=", s)

print(li1)