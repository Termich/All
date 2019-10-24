import requests
import json


link1 = "https://www.travelpayouts.com/widgets_suggest_params?q=Из%20Москвы%20в%20Лондон"
test1 = requests.get(link1)
print(link1)

# Вариант 1
# Почему то препод сдел это задание и выгрузил его =))

def get_iata_code(city):
    link = "https://www.travelpayouts.com/widgets_suggest_params?q=Из%20" + city + "%20в%20Лондон"
    text = requests.get(link).text
    data = json.loads(text)
    iata = data["origin"]["iata"]
    return iata

# Вариант 2
# Я Порпобовал сделать функцию которая возвращает код IATA столицы, надо внести только страну
def iata_code(cim):
    link = "https://www.travelpayouts.com/widgets_suggest_params?q=" + cim
    text = requests.get(link).text
    data = json.loads(text)
    iata = data["capital"]["iata"]
    return iata

# Вариант 3
# Альтернативное решение основного задания, очень долгий вывод т.к. он выкачивают всю библиотеку.

def iata(pim):
    link = "http://api.travelpayouts.com/data/ru/cities.json"
    text = requests.get(link).text
    data = json.loads(text)
    for dict in data:
        if dict['name'] == pim:
            return dict['code']


print(get_iata_code(input('Введите интересующий вас город, я сообщу вам IATA')))
#
print(iata_code(input('Введите страну, а я скажу IATA код столицы ')))
#
print(iata(input('Введите интересующий вас город, я сообщу вам IATA')))

# origin = get_iata_code(input("Введите интересующий вас город, я сообщу вам IATA"))
# dest = get_iata_code(input("Введите город прибытия:"))
# link = "http://min-prices.aviasales.ru/calendar_preload?one_way=true&origin="+origin+"&destination="+dest
# data = json.loads(requests.get(link).text)
# print(data["best_prices"][0])
# print(get_iata_code(input('Введите интересующий вас город ')))
