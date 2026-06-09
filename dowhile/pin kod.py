pin_kod = "4590"
while True:
    attempt_result = input(f'Введите пин - код:')
    if attempt_result == pin_kod :
        print('Доступ разрешен.')
        break
    else:
        print('Ошибка. Попробуйте еще раз')


