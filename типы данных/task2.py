import math

x1,y1 = map(float, input("введите координаты первой точки (x y) через пробел:").split())
x2,y2 = map(float, input("введите координаты второй точки (x y) через пробел:").split())

distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print(f"евклидово расстояние: {distance:.2f}")
