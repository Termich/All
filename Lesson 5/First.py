import os

#Данная функция создает папки


def create (name):
    for i in range(1,10):
        path = os.path.join(os.getcwd(), '{}_{}'.format(name, i))
        try:
            os.mkdir(path)
        except OSError:
            print("Создать директорию %s не удалось" % path)
        else:
            print("Успешно создана  директория %s" % path)



def kill (name):
    for i in range(1,10):
        path = os.path.join(os.getcwd(), '{}_{}'.format(name, i))
        try:
            os.rmdir(path)
        except OSError:
            print("Удалить директорию %s не удалось" % path)
        else:
            print("Успешно удалена директория %s" % path)


if __name__ == '__main__':
    create('dir')
    print('Папки созданы, поздраляю!')
    kill('dir')

