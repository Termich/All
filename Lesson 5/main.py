import First
from Third import special

print(f'введите номер желаемой функции:\n'
      f'1 создать директории в рабочей директории  \n'
      f'2 удалить директории из рабочей директории \n'
      f'3 ввести лист и получить случайное значение из листа \n'
      f'Либо любая другая клавиша, что бы покинуть программу')

rom = input('Введите номер желаемой функции')
name = 'dir'
#key = [1, 2, 3, 4]
key=[]


if rom == '1':
    First.create(name)
elif rom == '2':
    First.kill(name)
elif rom == '3':
    print(special(key))



