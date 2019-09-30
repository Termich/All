import os

# Данный функция удаляет то что мы создали в Modul_2

def kill (name,range):
    for i in range(1,10):
        path = os.path.join(os.getcwd(), '{}_{}'.format(name, i))
        try:
            os.rmdir(path)
        except OSError:
            print("Удалить директорию %s не удалось" % path)
        else:
            print("Успешно удалена директория %s" % path)

if __name__ == '__main__':
    kill('dir',range)



#try:
#    os.rmdir('dir_[]')
#except OSError:
#    print ("Удалить директорию %s не удалось" % path)
#else:
#    print ("Успешно удалена директория %s" % path)


