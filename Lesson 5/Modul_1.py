import sys, os



#for i in range(1,9) :
#    path = os.path.join(os.getcwd(), '{}_{}'.format(name,i))
#    os.mkdir(path)


def create (name,range):
    for i in range(1,10):
        path = os.path.join(os.getcwd(), '{}_{}'.format(name, i))
        os.mkdir(path)

create('dir',range)

print('Папки созданы, поздраляю!')
