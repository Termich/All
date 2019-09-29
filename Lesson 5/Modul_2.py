import os

# определим имя директории, которую удаляем

def kill ():
    for i in range(1,10):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '{}_{}')
        os.rmdir(path)

kill()

#try:
#    os.rmdir('dir_[]')
#except OSError:
#    print ("Удалить директорию %s не удалось" % path)
#else:
#    print ("Успешно удалена директория %s" % path)


