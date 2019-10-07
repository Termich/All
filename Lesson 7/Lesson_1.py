
a = ['Яблоко','Груша','Бургер','Пиво','Шаурма']

b = ['Ананас','Пиво','Нектарин','Шаурма','Шаурма']

#for result in a + b:
#    print(result)

#banana = [result for result in a + b]
#print(banana)

result = [fruit for fruit in a if fruit in b]
# result = [number for number in set(a) & set(b)]
print(result)
