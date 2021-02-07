# Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

file_name = '/Users/matvey/Desktop/Python/Lesson_5/employers.txt'
with open(file_name, 'w') as my_file:
    my_file.writelines(['Звягинцев:  75000\n', 'Жириновский:  6780\n', 'Мараховский:  34500 \n', 'Масасси:  986000\n',
                    'Вейдер:  56000\n', 'Жуков:  18900\n', 'Петров: 56000\n', 'Навальный: 1200\n', 'Поттер: 5600\n'])


with open(file_name, 'r') as my_file:
    print(my_file.read())


with open(file_name, 'r') as my_file:
    employers = {}
    salary = []
    les_salary = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            les_salary.append(i[0])
        salary.append(i[1])
print(f'lll {les_salary}', asdasd {sum(my_list(int,salary) / len(salary))}')


    # for line in my_file:
    #     less_salary, salary = line.split()
    #     employers[less_salary] = salary
    #     if int(salary) < 20000:
    #         salary.append(i[1])
    #             print(f'Зарплата меньше 20К: {less_salary}')

