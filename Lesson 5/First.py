import sys, os

#Данная функция создает папки

def create (name,range):
    for i in range(1,10):
        path = os.path.join(os.getcwd(), '{}_{}'.format(name, i))
        os.mkdir(path)
    return

create('dir',range)

print('Папки созданы, поздраляю!')
