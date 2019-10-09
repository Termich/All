import os


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже есть')


def get_list(folder_only=False):
    result = os.listdir()
    if folder_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copyfree(name, new_name)
        except FileExistsError:
            print('Таккая папка уже есть')
    else:
        shutil.copy(name, new_name)




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
    copy_file('test12.dat','test14.dat')
    copy_file('New_f2','New_f3')