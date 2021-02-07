# Создать текстовый файл (не программно), сохранить
<<<<<<< HEAD
 # в нем несколько строк, выполнить подсчет количества строк,
 # количества слов в каждой строке.

 file_name = '/Users/matvey/Desktop/Python/Lesson_5/my_nonprogfile.txt'
 my_file = open(file_name, 'r')
 my_file = open(file_name, 'r')
 content = my_file.read()
 print(f'Содержимое файла: \n {content}')
 my_file = open(file_name, 'r')
 content = my_file.readlines()
 print(f'Количество строк в файле - {len(content)}')
 my_file = open(file_name, 'r')
 content = my_file.readlines()
 for i in range(len(content)):
     print(f'Окличество символов {i + 1} - ой строки {len(content[i])}')
 my_file = open(file_name, 'r')
 content = my_file.read()
 content = content.split()
 print(f'Общее количество слов - {len(content)}')
 my_file.close()
=======
# в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

file_name = '/Users/matvey/Desktop/Python/Lesson_5/my_nonprogfile.txt'
my_file = open(file_name, 'r')
my_file = open(file_name, 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file = open(file_name, 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
my_file = open(file_name, 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Окличество символов {i + 1} - ой строки {len(content[i])}')
my_file = open(file_name, 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()
>>>>>>> 85740d4b76b8c018b88ce1cc5b7c863684f403ce
