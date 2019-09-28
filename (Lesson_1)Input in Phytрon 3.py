print('Добро пожаловать в больницу SimSity, введите пожалуйста следующие данные:')
name = input('Введте ваше имя:')
surname = input('Введите вашу фамилию')
weight = int(input('Введите ваш вес:'))
age = int(input('Уточните ваш возраст'))

print('Пациент' ,name,'' ,surname, 'Возраст:' ,age,'Вес: ' ,weight)

if age <= 30 and (weight >= 50 and weight <= 120) :
    print('Хорошее состояние')
elif (age > 30 and age <= 40) and (weight < 50 or weight > 120):
    print('Требуется заняться собой')
#Скобки эта важная ЖОПА, ели догадался
elif age > 40 and (weight < 50 or weight > 120) :
    print('требуется врачебный осмотр')
else:
    print('Ты не подходишь не под один из фильтров, эта больница не для тебя')




