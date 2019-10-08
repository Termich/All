def banana(number):
    if number == 13:
        raise ValueError
    else:
      return number ** 2

while True:
    number = int(input('Введите число от 0 до 100: '))
    if number > 0 and number < 101:
        break
    else:
        print('Не верно, введите 0< число <100')

try:
    print(banana(number))
except ValueError:
    print('Обработал исключительную ситуацию, которая поднялась внутри Вункции')


# print(banana())
#
# def banan(number):
#     num = -1    if number == 13 else number ** 2
#     if num ==-1 : raise ValueError
#     return number
