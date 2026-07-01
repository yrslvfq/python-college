weight, height = map(float, input("Введите вес (кг) и рост (м) через пробел: ").split())

imt = weight / (height * height)
print(f"Индекс Массы Тела (ИМТ): {imt:.1f}")