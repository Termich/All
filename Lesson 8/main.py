import sys

from core import create_file, create_folder, get_list, delete_file, copy_file, save_info

save_info('Старт')

command = sys.argv[1]

if command == 'list':
    get_list()

elif command == 'create_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название файла')
    else:
        create_file(name)

elif command == 'create_folder':
    name = sys.argv[2]
    new_name = sys.argv[3]
    create_folder(name, new_name)