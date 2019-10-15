def attack(person1,person2):
    person1['health'] -= damage_reduction(person2['damage'],person1['armor'])    #Дополняем новую функцию которая работает с броней которая поглощает урон, делит его так сказать)


def damage_reduction(damage,armor):
    return damage/armor

player = {'Name':input('Введите имя игрока 1:'),'health':100, 'damage':50 ,'armor':1.2}
enemy = {'Name':input('Введи имя игрока 2:'),'health':100, 'damage':50,'armor':1.2 }



attack(player,enemy)

print(player)
print(enemy)
