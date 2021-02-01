seconds = int(input('Введите кол-во секунд: '))

chas = seconds // 3600
minut = seconds % 3600 // 60
sek = seconds % 3600 % 60

string = '%dч:%dм:%dс' % (chas, minut, sek)
print(string)
