
cities = [('Москва',1000),('Лас Вегас',500),('Анттверпен',200),('Мытищи',500)]


print (sorted(cities))

def by_count(city):
    return city[1]


print (sorted(cities,key=by_count))