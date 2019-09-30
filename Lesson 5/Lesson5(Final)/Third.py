#тут введя 4 числа мы получим случайное из них

from random import choice

#Функция для проверки целостности списка), None, с начала было желание провернуть это через Print

def special(some_list):
    if some_list: return choice(some_list)

if __name__ == '__main__':
    key = [1, 2, 3, 4]
    print(special(key))
