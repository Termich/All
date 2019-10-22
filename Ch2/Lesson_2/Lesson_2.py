import re
from bs4 import BeautifulSoup as BS


with open ("index.html",encoding='utf-8') as f:
    s = f.read()
# Находим количество человек через .re

li1 = re.findall('<span class="total-users">Нас уже ([\d\s]+) человек</span>', s)
li = re.findall('</a></div><div class="col"><span class="total-users">Нас уже ([\d\s]+) человек</span>',s)

print(li)
print(li1)

# Находим количество человек через BeautifulSoup.

# Сделаем как у препода)

soup = BS(s, "html.parser")
print(soup.find_all('<span class="total-users"'))


print("HTML: {0}, name: {1}, text: {2}".format(soup.h2,
        soup.h2.name, soup.h2.text))