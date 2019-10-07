import json
import pickle

#Собираем словарь

my_favourite_group = {
    'name': 'A Victory of Love',
    'artist': 'Alphaville',
    'album': 'Forever Yong',
    'year': '1984',
}

# Можно записать в байты следующим образом,
# далеко не сразу до этого дошел после просмотра лекции, там об этом не сказано.

param = pickle.dumps(my_favourite_group)
print(param)
print(type(param))

#Записываем в json

with open('group.jon','w',encoding='utf-8') as f:
    json.dump(my_favourite_group,f)

print('Записано')
#Записываем в picle

with open('group.dat', 'wb') as f:
    # f.write(param)
    pickle.dump(my_favourite_group, f)


print('Готово')
