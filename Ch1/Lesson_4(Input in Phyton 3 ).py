def attack(person1,person2):
    person1['health'] -= person2['damage']  #Собственно как по условием задания функция работает с параметрами словаря

player = {'Name':input('Введите имя игрока 1:'),'health':100, 'damage':50}
enemy = {'Name':input('Введи имя игрока 2:'),'health':100, 'damage':50}
print(attack(player,enemy))           # Наблюдаем работу функции с переменными
print(player)


