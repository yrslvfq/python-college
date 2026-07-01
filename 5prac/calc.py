PI = 3.14


def calculate_rectangle_area(width, height):
    """
    Функция принимает ширину и высоту прямоугольника,
    перемножает их и возвращает площадь.
    """
    rect_area = width * height
    return rect_area



def calculate_circle_area(radius):
    """
    Функция принимает радиус круга,
    считает площадь по формуле (Пи * радиус в квадрате) и возвращает её.
    """
    circle_area = PI * (radius ** 2)
    return circle_area



print("--- Расчет площади прямоугольника ---")
rect_width = float(input("Введите ширину прямоугольника: "))
rect_height = float(input("Введите высоту прямоугольника: "))


result_rect = calculate_rectangle_area(rect_width, rect_height)
print(f"Площадь прямоугольника: {result_rect:.2f}")

print() 

print("--- Расчет площади круга ---")
user_radius = float(input("Введите радиус круга: "))

result_circle = calculate_circle_area(user_radius)
print(f"Площадь круга: {result_circle:.2f}")