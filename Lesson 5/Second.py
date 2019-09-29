import os

# Данный функция удаляет то что мы создали в Modul_2

def kill ():
    for i in range(1,10):
        name = 'dir'
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '{}_{}'.format(name, i))
        os.rmdir(path)

kill()

#try:
#    os.rmdir('dir_[]')
#except OSError:
#    print ("Удалить директорию %s не удалось" % path)
#else:
#    print ("Успешно удалена директория %s" % path)


