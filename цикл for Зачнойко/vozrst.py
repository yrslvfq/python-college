m = int(input('введите число m:'))
n = int(input('введите число n:'))
for i in range(m, n + 1, 1):
    print(i)
if m > n:
    for i in range(m, n -1, -1):
        print(i)
elif m == n:
    print(m)


