# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчете на одного сотрудника.

profit = int(input('Введите выручку: '))
costs = int(input('Введите затраты: '))
if profit > costs:
    print(f'Фирма работает с прибылью. Рентаьельность составила {profit / costs:}')
    workers = int(input('Введите колличество сотрудников'))
    print(f'Прибыль в расчете на одного сотрудник фирмы составила {profit / workers:}')
elif profit == costs:
    print('Фирма работает в ноль')
else:
    print('фирма работает в убыток')