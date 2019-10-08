import math

key = [1, 5, 8, 9, 20, 27, 45, 68, 41, -5, -10, -16, -55, 12]

def banana(key):
    result = [math.sqrt(number) if number > 0 else number for number in key]
    return result
print(banana(key))
print(key)
