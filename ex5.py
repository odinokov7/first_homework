viruchka = float(input('Введите значение выручки:'))
izderzhka = float(input('Введите значение издержки:'))

if viruchka > izderzhka:
    print('Прибыль!')
    pribyl = viruchka - izderzhka
    rent = pribyl / viruchka
    print('Рентабельность составляет:', rent * 100, '%')
    sotrud = int(input('Введите кол-во сотрудников фирмы: '))
    print('Прибыль на одного сотрудника составляет:', pribyl / sotrud)
else:
    print('Убыток..')
