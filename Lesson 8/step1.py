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
        result = [f for f in result if os.patch.isdir(f)]
    print(result)


if __name__ == '__main__':
    create_file('test.dat')
    create_file('test.dat', 'test2')
    create_folder('Folder test')
    get_list(True)
