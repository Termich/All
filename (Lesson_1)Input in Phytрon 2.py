# Задание номер 2

while True:
    number = int(input('Угадай число: '))
    if number > 0 and number < 10:
        break
    else:
        print('Не верно, введите 0< число <10')

(print('Вот это число возведенное во 2-ю степень:', number**2 ))