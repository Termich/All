number = int(input('Введите число: '))

def banana(number):
    if number == 13:
        raise ValueError
    else:
        number * 2

print(banana(number))
