price = 0
tickets = int(input('Количество билетов :'))
for i in range(0, tickets):
    ages = int(input('Введите возраст посетителей:'))
    if ages >= 18:
        price = price + (990 if ages in range(18, 25) else 1390)
if tickets > 3:
    print('Сумма со скидкой:', price*0.9,'рублей' )
else:
    print('Сумма: ', price, 'рублей')

