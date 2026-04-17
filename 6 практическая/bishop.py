before_1, before_2, after_1, after_2 = int(input('введите первое значение слона до хода ')), int(input('введите второе значение  слона до хода ')), int(input('введите первое значение  слона после хода ')), int(input('введите второе значение слона после хода '))
if before_1 + before_2 == after_1 + after_2 or after_1 - before_1 == after_2 - before_2:
    print('\nYES')
else:
    print('\nNO')