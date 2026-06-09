
total = 1
while True:
    num = int(input('Введите число(чтобы получить результат введите отрицательное число):'))
    print('')
    if num > -1:
        total *= num
    else:
        print('Ваше произведение:', total)
        break



