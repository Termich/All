numbers = [1, 5, 8, 9, 20, 27, 45, 68, 41, -5, -10, -16, -55, 12]

# result = [number for number in numbers if number % 3 == 0]
# result1 = [number for number in numbers if number > 0]
# result2 = [number for number in numbers if number % 4 != 0]
# print(f'number %3==0: {result}')
# print(f'number > 0: {result1}')
# print(f'number %4!=0: {result2}')

bigresult = [number for number in numbers if number > 0 and number % 4 != 0 and number % 3 == 0]
print('All')
print(bigresult)
