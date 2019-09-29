from random import choice

def special():
    return (choice(list(map(int, input('Введите 3 числа через запятую, в одной строке.').split(',')))))
print(special())


