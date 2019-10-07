key = [1, 5, 8, 9, 20, 27, 45, 68, 41, -5, -10, -16, -55, 12]
bey = key.copy()

result2 = [number**2 for number in key and key > 0]
print(result2)

#def numbers (key):
#    newnumber = int[number for number in key if key**2]

#print(numbers(key))