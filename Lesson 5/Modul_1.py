import sys, os

name = 'dir'

for i in range(1,9) :
    path = os.path.join(os.getcwd(), '{}_{}'.format(name,i))
    os.mkdir(path)