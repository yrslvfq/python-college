attempt_count = 1
password = "admin"
while True:
    attempt_result = input(f'Введите пароль, Попытка №{attempt_count}:')
    if attempt_result == 'admin' :
        print('Пароль верный!!! Вход в систему.')
        break
    elif attempt_count != 4:
        print('Пароль неверный')
        attempt_count += 1
    if attempt_count == 4:
        print('Попытки закончились, вход заблокирован')
        break

