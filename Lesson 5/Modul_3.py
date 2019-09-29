from random import randint,choice

def live(*vum):
   vum = list(map(int, input('Введите 4 числа через запятую, в одной строке.').split(',')))
   return choice(vum)


print(*vum)
