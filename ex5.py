income = int(input('Значение вычуки фирмы:'))
outcome = int(input('Значение издержек фирмы:'))
if income > outcome:
    p = ((income - outcome) / income) * 100
    print('Ваша фирма евляется прибыльной! Рентабельность выручки: ' + str(p) + "%")
    num = int(input('Сколько сотрудников в вашей фирме?'))
    n = (income - outcome) / num
    print(f'Прибыль в расчете на одного сотрудника равняется: {n}')
else:
    print('Ваша компания страдает от издержек')
