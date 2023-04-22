# import math

# a = 2
# b = 6
# c = -7

# d = b**2 - 4*a*c
# if d > 0:
#     x1 = (-b + math.sqrt(d)) / 2*a
#     x2 = (-b - math.sqrt(d)) / 2*a
#     print(x1,x2)
# elif d == 0:
#     x = -b / 2*a
#     print(x)
# else:
#     print('Корней нет')

#import math

#print(math.ceil(2.1)) #Округление числа 2.1 до 3, округление нецелого числа до бОльшего
#print(math.fabs(-5)) #Модуль числа
#print(math.floor(6.9)) #Округление числа до целого ниже, тобиш до 6
#print(math.isfinite(5)) #Проверка, является ли число числом
#print(math.fmod(27, 6)) #Нахождение остатка от деления
#print(math.isinf(50)) #Является ли число бесконечным?
#print(math.pow(3, 3)) #Возведение первого числа в степень второго
#print(math.sqrt(1600)) #Нахождение квадратного корня

'''def test (*args):
     print(args)

test(1,2,3,4,5,6)'''

'''def count_args (*args):
    print(len(args))

count_args(1, 4, 6, 8, 9)
'''

'''def mean (*args):
    count = 0
    c = 0
    for i in args:
        if type(i)== int or type(i)==float:
            count += i
            c += 1
    print(count / c)

mean(1, 'cckck', True, 8, 9)
'''

'''import csv
with open('countries.csv', 'r') as r:
   curs = csv.reader(r)
   for i in curs:
      print(i)
'''
# # Необходимо написать код для дозаписи кортежа в файл
# (5, 'Vova', 'Korolev', 67, 543, 5434)

# with open('data.csv', 'a', newline = '') as f:
#   curs = csv.writer(f)
#   curs.writerow((5, 'Vova', 'Korolev', 67, 543, 5434))

# def plus(a,b):
#      return a+b

# print(plus(1,2))

# if __name__ == '__main__':
#     print('Run vebinars.py')
# else:
#     print('Run from another file!')
# #print(__name__)

