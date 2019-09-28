from random import randint,choice

def live(*args):
   return choice(args)

num = list(map(int, input('Введите 4 числа через запятую, в одной строке.').split(',')))
print(live(*num))
