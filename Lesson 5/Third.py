#тут введя 4 числа мы получим случайное из них

from random import choice

def special():
    return(choice(list(map(int, input('Введите 4 числа через запятую, в одной строке.').split(',')))))



print(special())

