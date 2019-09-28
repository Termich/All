from random import randint,choice


# Создаем функцию
def live(*args):
   return choice(args)

num = list(map(int, input('Введите 4 числа через запятую, в одной строке.').split(',')))

if num == int:
    print(num)
else:
    print('None')

