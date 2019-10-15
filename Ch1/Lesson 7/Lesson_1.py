
a = ['Яблоко','Груша','Бургер','Пиво','Шаурма']

b = ['Ананас','Пиво','Нектарин','Шаурма','Шаурма']

result = [fruit for fruit in a if fruit in b]
# result = [number for number in set(a) & set(b)] # Можно сделать еще и так)
print(result)
