max_number = 0
while True:
    a = int(input('Введите число из последовательности(чтобы завершить процесс введите 0):'))
    if a == 0:
        break
    if a > max_number:
        max_number = a
print('Максимальное число в последовательности:',max_number)