print("\n|||||||||ОПРЕДЕЛИТЕЛЬ СЕЗОНА||||||||||")
month = int(input("\nВведите номер месяца от 1 до 12:"))

match month:
    case 12 | 1 | 2:
        season = "❄️зима❄️"
    case 3| 4 | 5:
        season = "🍃весна🍃"
    case 6 | 7 | 8:
        season = "☀️лето☀️"
    case 9 | 10 | 11:
        season = "🍁осень🍁"
    case _:
        error = "\n          ошибка! \n Введите номер месяца от 1 до 12"
if 1 <= month <= 12:
    print("\nваш месяц", month, "время года:", season)
else:
    print(error)

