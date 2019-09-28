import os

# определим имя директории, которую удаляем


try:
    os.rmdir(path)
except OSError:
    print ("Удалить директорию %s не удалось" % path)
else:
    print ("Успешно удалена директория %s" % path)


