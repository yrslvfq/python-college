prices_str = '100 50 200 150 75 300'

prices = prices_str.split()

int_list = [int(price) for price in prices]

discount_price = max(int_list) / 2


int_list.append(discount_price)
print('добавлен товар со скидкой:', int_list )

max_price = max(int_list)
int_list.remove(max_price)
print('удалена максимальная цена:', int_list, )


int_list.sort()
print('цены отсортированы по возрастанию:', int_list )
avg_price = sum(int_list) / len(int_list)

print('средняя цена:', avg_price)