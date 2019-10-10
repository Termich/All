import os
import shutil
import datetime

def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            try:
                f.write(text)
            except Exception:
                print('Ошибка')
            else:
                print('Файл создан')



def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже есть')
    except IndexError:
        print('Папка не создана')
    else:
        print('Папка создана')


def get_list(folder_only=False):
    result = os.listdir()
    if folder_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


def delete_file(name):
    if os.path.isdir(name):
        try:
            os.rmdir(name)
        except Exception:
            print("Удалить директорию  не удалось")
        else:
            print("Успешно удалена директория")


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Таккая папка уже есть')
        else:
            print('Копирование выполнено')
    else:
        shutil.copy(name, new_name)


def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')

def banana(name):
    if os.chdir(name):
        try:
            os.chdir(name)
        except FileNotFoundError:
            print('Ошибка, нет такой директории')
        else:
            print('Вы поменяли директорию')



if __name__ == '__main__':
    create_file('test.dat')
    create_file('test12.dat')
    create_file('test.dat', 'test2')
    create_folder('New_f1')
    create_folder('New_f2')
    get_list(True)
    get_list()
    delete_file('New_f1')
    delete_file('test.dat')
    copy_file('test12.dat', 'test14.dat')
    copy_file('New_f2', 'New_f3')
    save_info('abc')
