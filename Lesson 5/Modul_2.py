import os

# определим имя директории, которую удаляем
path = "dir_3"

for i in range(1,9)
    path = os.path

try:
    os.rmdir(path)
except OSError:
    print ("Удалить директорию %s не удалось" % path)
else:
    print ("Успешно удалена директория %s" % path)
