num_a = float(input("введите число a:"))
operator = input("введите оператор +, -, * или /:")
num_b = float(input("введите число b:"))



match operator:
    case "+":
        result = num_a + num_b
match operator:
    case "-":
        result = num_b - num_a
match operator:
    case "*":
        result = num_a * num_b
match operator:
    case "/":
        if num_b != 0:
            result = num_a / num_b
        else:
                result = "\n       !!ОШИБКА!!\n\n НА НОЛЬ ДЕЛИТЬ НЕЛЬЗЯ!!"


print(result)
