import json
import pickle

my_favoutite_group = {
    'name': 'A Victory of Love',
    'artist': 'Alphaville',
    'album': 'Forever Yong',
    'year': '1984',
    }

with open('group.json','w',encoding='utf-8') as f:
    json.dump(my_favoutite_group,f)

print('Записано')

my_favoutite_group = {


with open('group.dat','w') as f:
    pickle.dumps(my_favoutite_group,f)

print('Готово')