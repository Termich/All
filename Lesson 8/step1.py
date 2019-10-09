import os


def create_file(name, text = None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)

def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже есть')



if __name__=='__main__':
    create_file('test.dat')
    create_file('test.dat', 'test2')
    create_folder('Folder test')


