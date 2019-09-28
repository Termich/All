import os

# определим имя директории, которую удаляем
path = "dir_2"



try:
    os.rmdir(path)
except OSError:
    print ("Удалить директорию %s не удалось" % path)
else:
    print ("Успешно удалена директория %s" % path)
