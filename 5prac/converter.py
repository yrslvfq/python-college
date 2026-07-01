USD_TO_RUB = 95.50
def convert_usd_to_rub(amount_usd):
    """
    Функция принимает сумму в долларах,
    умножает её на курс и возвращает сумму в рублях.
    """
    total_rub = amount_usd * USD_TO_RUB
    return total_rub

user_usd = float(input("Введите сумму в долларах: "))

result_rub = convert_usd_to_rub(user_usd)

print(f"Сумма в рублях: {result_rub:,.2f} руб.")