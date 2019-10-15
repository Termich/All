import json
import pickle

#Читаем Json
with open('group.jon','r') as f:
    js = json.load(f)
#Читаем Picle
with open('group.dat', 'rb') as f:
    pi = pickle.load(f)

print(js)
print(type(js))

print(pi)
print(type(pi))