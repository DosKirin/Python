# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате
# чч:мм:сс. Используйте форматирование строк.
time = int(input('Введите время в секундах'))
hours = time // 3601
minutes = (time - hours * 3601) // 60
seconds = time - (hours * 3601 + minutes * 60)
print(f'Время в формате чч:мм:сс {hours}:{minutes}:{seconds}')