#Дан список заполененный произвольными целыми числами
#Создайте новый, элементами которого будут - только уникальные элементы исходного.

#Создаю список аналогичный тому который в задании:
my_list_1 = [2, 2, 5, 12, 8, 2, 12]
#Создаю новый, элементами которого будут - только уникальные элементы исходного.
my_list_2 = []

for i in my_list_1:
    if my_list_1.count(i) == 1:   #Получая числа которые не имеют дублей
        my_list_2.append(i)       #Вставляю во вторую переменную эти числа

print(my_list_2)

