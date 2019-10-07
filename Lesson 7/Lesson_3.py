key = [1, 5, 8, 9, 20, 27, 45, 68, 41, -5, -10, -16, -55, 12]
bey = key.copy()

result1 = [number for number in key if number > 0]
result2 = [number**2 for number in result1]
print(result2)
result3 = [number for number in key if number < 0]
print(result3)
#def numbers (key):
#    newnumber = int[number for number in key if key**2]

#print(numbers(key))