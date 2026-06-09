balance = 1000

while True:
    print('1. Узнать баланс')
    print('2. Снять 100 руб')
    print('3. Положить 100 руб')
    print('4. Выход')
    a = int(input())
    if a == 1:
        print('Баланс:', balance)
    elif a == 2:
        balance -= 100
    elif a == 3:
        balance += 100
    elif a == 4:
        print('До свидания!')
        break
    else:
        print("Неверная команда")