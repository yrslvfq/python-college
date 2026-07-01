n = int(input('Введите число для расчета факториала: '))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"Факториал числа {n} равен {factorial}")
