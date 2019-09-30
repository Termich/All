#тут введя 4 числа мы получим случайное из них

from random import choice


def special(some_list):
    if some_list: return (some_list)

key = [1,2,3,4]


if __name__ == '__main__':
    print(choice(special(key)))
