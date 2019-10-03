import json
import pickle

def favorit_j():
    my_favourite_group = {
        'name': 'A Victory of Love',
        'artist': 'Alphaville',
        'album': 'Forever Yong',
        'year': '1984',
    }

with open('group.json','w',encoding='utf-8') as f:
    json.dump(my_favourite_group,f)

print('Записано')

def favorit_p():
    my_favourite_group = {
    'name': 'A Victory of Love',
    'artist': 'Alphaville',
    'album': 'Forever Yong',
    'year': [1984,1985]
    }

with open('group.dat','wb') as f:
    pickle.dump(my_favourite_group, f)

print('Готово')