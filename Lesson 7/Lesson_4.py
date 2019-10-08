#Написали функцию
def banana(number):
    if number == 13:
        raise ValueError
    else:
      return number ** 2
#Сделали проверку от 1 до 100
while True:
    number = int(input('Введите число от 0 до 100: '))
    if number > 0 and number < 101:
        break
    else:
        print('Не верно, введите 0< число <100')
#Обработали исключительные ситуации и выдали результат
try:
    print(banana(number))
except ValueError:
    print('Обработал исключительную ситуацию, которая поднялась внутри Вункции')

