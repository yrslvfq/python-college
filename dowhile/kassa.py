basket = 0
while True:
    cost = int(input("Введите цену товара(чтобы посмотреть корзину введите 0):"))
    if cost == 0 :
        break
    if cost < 0 :
        print('Ошибка цены')
        continue
    else:
        basket += cost
print('Сумма покупок', basket)
if basket > 999 :
    print('Для вас полагается скидка 10%')
    discount = basket // 10
    print("Сумма покупок со скидкой -", basket - discount)