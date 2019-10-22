import re

with open ("index.html",encoding='utf-8') as f:
    s = f.read()
# Находим количество человек через .re

li1 = re.findall('<span class="total-users">Нас уже ([\d\s]+) человек</span>', s)
li = re.findall('</a></div><div class="col"><span class="total-users">Нас уже ([\d\s]+) человек</span>',s)

print(li)
print(li1)

# Находим количество человек через .