from sys import argv

task, sap_h, cost_h, prize = argv

# salary_c =
sap_h = int(sap_h)
cost_h = int(cost_h)
prize = int(prize)
salary = sap_h * cost_h + prize

print(f'SLA {salary}')


# тут у меня ничего не работает ошибка синтексиса на 11 строке