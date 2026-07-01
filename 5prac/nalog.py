TAX = (0.13)
doxod = int(input("Введите свой доход до вычета налогов:"))
tax_sum = doxod * TAX
aftertax = doxod - tax_sum

print(f"Доход: {doxod:,.2f}")
print(f"Сумма налога: {tax_sum:,.2f}")
print(f"Доход после вычета налогов: {aftertax:,.2f}")