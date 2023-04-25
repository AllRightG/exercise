#Интеграция .csv в код
'''
Что такое CSV файлы?
CSV - comma separated values(значения, разделенные запятой)
Данный формат часто используется в анализе данных

Первая строка файла - название столбцов. Все последующие строки - данные, которые хранятся в нашем файле
'''
'''
Пример:
id,name,age,group
1,Max,13,IT
2,Anna,15,IT
3,Inna,25,ROBO

d = {
  'name' = ['Max', 'Anna', 'Inna']
  'age' = [13, 15, 25]
  'group' = ['IT', 'IT', 'ROBO']
}
'''
""" def read_csv(filename):
    data = {} #Возвращаем словарь, в котором по итогу будет ключ, и набор элементво по нему
    with open(filename, 'r') as file: #with Обрабатывает исключение в ходе работы с файлом, и сама его закрывает
        columns = tuple(file.readline().replace('\n', '').split(','))[1:] #Обращаемся к файлу, читаем первую строку, при применении replace убираем символ переноса строки на пусоту, и при помощи split разделяем элементы ,
        #print(columns)
        data = {i:[] for i in columns} #Цикл записанный в одну строку - генератор, пробегаясь по названиям столбцов получаем их, и теперь i является ключом, и у него есть список пустой
        for line in file: #Читаем файл с помощью цикла, в line записывается каждая строка, и обрабатывается она
            #1,2,India,1382345085,2973190
            line = line.split(',')[1:] #Разделяем элементы строки, чтобы не было запятых, берем от первого символа, без первого столбца
            for col, value in zip(columns, line): #Берется элемент из columns а потом из line, создается набор кортежей с помощью zip
                #print(col, value)
                value = value.replace('\n', '') #
                value = int(value) if value.isdigit() else value #Если в строке только числа - преобразуем в целые, не только числа - просто возвращаем
                data[col].append(value) #Обращаемся к списку по ключу, и добавляем
    return data

d = read_csv('countries.csv')
ind = d['name'].index('Honduras')
print(d['area'][ind]) """


"""
def print_data(data:dict):
    columns = list(data.keys())
    m=max([len(i) for i in columns])
    for col in columns:
        m = max(max(map(lambda x: len(str(x)), data[col])), m)
    for i in columns:
        print(str(i).ljust(m+1, ' '), end='')
    print()
    for i in range(len(data[list(data.keys())[0]])):
        for col in columns:
            print(str(data[col][i]).ljust(m+1, ' '), end='')

print(read_csv('countries.csv'))
 """
#Интеграция .db в код
'''
Db (Data Base) - формат файла, использующийся для храниния информаций, баз данных.
Sqlite3 - библиотека, благодаря которой можно работать с файлами .db

Для работы с файлом необходимо после импорта библиотеки создать следующие переменные:

Connection - переменная отвечающая за связь с текущим файлом .db
и
Cursor - указатель на текущее действие в нашем файле .db
'''
""" import sqlite3 as sq
connection = sq.connect('students.db')
#sq.connect('students.db')
cursor = connection.cursor()
selection = list(cursor.execute('select * from students'))

#Какой средний балл среди всех элементов?
for i in selection:
  print(i)

sum = 0
for i in selection:
  sum += i[6]
print(sum / len(selection))
 """
