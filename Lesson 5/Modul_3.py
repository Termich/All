from random import randint,choice

def live(num):
   num = list(map(int, input('Введите 4 числа через запятую, в одной строке.').split(',')))
   return choice(num)


print(live(*num))
