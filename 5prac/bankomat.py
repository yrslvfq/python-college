
amount = int(input("Введите сумму для снятия (кратную 100): "))

print("\nОтчет о выдаче купюр:")

count_5000 = amount // 5000  
amount = amount % 5000      

count_2000 = amount // 2000
amount = amount % 2000

count_1000 = amount // 1000
amount = amount % 1000

count_500 = amount // 500
amount = amount % 500

count_200 = amount // 200
amount = amount % 200

count_100 = amount // 100
amount = amount % 100

print(f"Купюры 5000 руб.: {count_5000} шт.")
print(f"Купюры 2000 руб.: {count_2000} шт.")
print(f"Купюры 1000 руб.: {count_1000} шт.")
print(f"Купюры 500 руб.:  {count_500} шт.")
print(f"Купюры 200 руб.:  {count_200} шт.")
print(f"Купюры 100 руб.:  {count_100} шт.")
