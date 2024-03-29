import sys, random
import os

from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, banana
from game import games

save_info('Старт')

try:
    command = sys.argv[1]
except Exception:
    print('Введите команду')
else:
    if command == 'list':
        get_list()

    elif command == 'game':
        games()


    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла')
        else:
            create_file(name)
            print('Файл создан')

    elif command == 'change':
        try:
            name = sys.argv[2]
        except Exception:
            print('Ошибка')
        else:
            banana(name)
            print('Вы находитесь в директории:', os.getcwd())

    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except Exception:
            print('Ошибка')
        else:
            create_folder(name)

    elif command == 'delete':
        try:
            name = sys.argv[2]
        except Exception:
            print('Ошибка')
        else:
            delete_file(name)


    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except Exception:
            print('Ошибка')
        else:
            copy_file(name, new_name)

    elif command == 'help':
        print('list - список файлов и папок')
        print('create_file - создание файла')
        print('create_folder - создание папки')
        print('delete - удаление файла или папки')
        print('copy - копирование файла или папки')
        print('change - смена директории')
        print('game - Игра угадай число')

save_info('Конец')
