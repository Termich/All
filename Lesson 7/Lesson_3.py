import math


key = [1, -3, 4]
bey = key.copy()

result1 = [number for number in key if number > 0]
result2 = [math.sqrt(number) for number in result1]
print(result2)
result3 = [number for number in key if number < 0]
print(result3)
#def numbers (key):
#    newnumber = int[number for number in key if key**2]

#print(numbers(key))

