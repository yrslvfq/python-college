temp = int(input ("Введите температуру в градусах Цельсия:"))
pressure = int(input("Введите давление:"))
pulse = int(input("Введите пульс в уд/мин:"))

if (temp<35 or temp>38) or (pressure<105 or pressure>140) or (pulse<55 or pulse>110):
    print("\nТребуется врач")
elif 36 <= temp <= 37 and 110 <= pressure <= 130 and 60 <= pulse <= 100:
    print("\nНормальное состояние")
elif  (35 <= temp <= 36 or 37 <= temp <= 38) or (105 <= pressure <= 100 or 130 <= pressure <= 140) or (55 <= pulse <= 60 or 100 <= pulse <= 110):
    print("\nЛегкое недомогание")

