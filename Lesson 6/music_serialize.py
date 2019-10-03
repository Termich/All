import json
import pickle

my_favourite_group = {
        'name': 'A Victory of Love',
        'artist': 'Alphaville',
        'album': 'Forever Yong',
        'year': '1984',
    }

with open('group.json','w',encoding='utf-8') as f:
    json.dump(my_favourite_group,f)

print('Записано')

with open('group.dat','wb') as f:
    pickle.dump(my_favourite_group, f)

print('Готово')