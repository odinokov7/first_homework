a = int(input('Введите число: '))
b = []
n = 0
i = 0
maxi = 0
while a >= 1:
    b.append(a % 10)
    a //= 10
    n += 1
while i <= n - 1:
    if b[i] > maxi:
        maxi = b[i]
    i += 1
print('Самая большая цифра -', maxi)
