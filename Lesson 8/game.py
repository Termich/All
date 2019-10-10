import random

def games(start = 1, end = 100):
    print('Давайте сыграем в игру: ты загадаешь число, а я попробую его угадать.')
    print('Для попощи мне, используй знаки "<" ">" Или "=" если я угадал ')
    while True:
        number = random.randint(start, end)
        print(number)
        key = input('Введите символ')
        if key == '=':
            print('Победа, меня не так то просто обхетрить')
            break
        elif key == '<':
            start = number + 1
            print('Неправильно, Маловато')

        elif key == '>':
            end = number - 1
            print('Многовато, попробую еще')
    return (number)



