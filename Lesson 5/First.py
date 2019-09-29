import sys, os

#Данная функция создает папки

def create (name,range):
    for i in range(1,10):
        path = os.path.join(os.getcwd(), '{}_{}'.format(name, i))
        try:
            os.mkdir(path)
        except OSError:
            print("Создать директорию %s не удалось" % path)
        else:
            print("Успешно создана  директория %s" % path)


create('dir',range)

print('Папки созданы, поздраляю!')
