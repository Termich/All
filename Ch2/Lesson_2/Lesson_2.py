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
# print(soup.span)
#
# print(soup.title.string)
new_news = []
news = []
print(soup.find_all('div', class_='col'))
for i in range(len(news)):
    if news[i]. find ('div', class_ = 'total-users') is not None:
        new_news.append(news[i].text)

#result = soup.find('div', {'class' :'col'}).find('span'),s
#print(result)






