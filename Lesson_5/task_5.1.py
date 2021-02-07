# Создать программно файл в текстовом формате, записать в него построчно данные,
<<<<<<< HEAD
 # вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

 with open('my_file_1.txt', 'w') as my_file:
     my_text = input('enter text\n')
     while my_text:
         my_file.writelines(my_text)
         my_text = input('enter text\n')
         if not my_text:
             break
=======
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

with open('my_fil.txt', 'w') as my_file:
    my_text = input('enter text\n')
    while my_text:
        my_file.writelines(my_text)
        my_text = input('enter text\n')
        if not my_text:
            break
>>>>>>> 85740d4b76b8c018b88ce1cc5b7c863684f403ce





<<<<<<< HEAD
 with open('my_fil.txt', 'r') as my_file:
     while True:
         content = my_file.read()
         print(content)
         if not content:
             break
=======
with open('my_fil.txt', 'r') as my_file:
    while True:
        content = my_file.read()
        print(content)
        if not content:
            break
>>>>>>> 85740d4b76b8c018b88ce1cc5b7c863684f403ce
