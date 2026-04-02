num = int(input())
thousands = num // 1000
hundreds = num % 1000 // 100
tens = num % 100 // 10
numbers = num % 10

print('Цифра в позиции тысяч равна', thousands)
print('Цифра в позиции сотен равна', hundreds)
print('Цифра в позиции десятков равна', tens)
print('Цифра в позиции единиц равна', numbers)