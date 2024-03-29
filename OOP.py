'''
ООП:

Класс - шаблон для начала объекта, некий чертеж для создания объектов
Объект - сущность которое обладает поведением и состояние класса, реализация какого-либо класса
Свойства - переменные внутри класса которые его описывают
Функции - методы класса
Переменные внутри класса это СВОЙСТВА
Функции внутри класса это МЕТОДЫ
Self - общепринятное имя для ссылки на объект, в контексте которого вызывается метод
Методы объекта класса не вызываются без объекта, ибо передается ссылка на текущий объект в метод-
-и записывается в self
Ссылка - то, чем мы обращаемся к объекту (обстрактно), на текущий объект

def set_param(self, color):   Создание динамического метода объекта класса
self.color = color

Конструктор (Инициализатор) - медот при создании класса, всегда так (__init__)
Статический метод (@staticmethod) - простая функция внутри класса, ничего не передается, для вызова
объекты не нужны, обращение напрямую к классу

Классовый метод (@classmethod) - передается ссылка на класс!!!

Концепции ООП:
Обстракция - оставить (выделить) главное и отбросить второстепенное, все по делу
Инкапсуляция - принцип, в сути которого скрыть сложность програмного компонента за его интерфейсом, доступ к данным ВНЕ класса закрыт
Наследование - возможность создать другой класс за счет старого, с учетом добавления чего-то нового, более совершенная версия класса
Полиморфизм - поддержка нескольких реализаций на основе общего интерфейса?
'''

# #Создание класса Table
# class Table:
# #Создаем атрибуты класса, объекты.
#     material = "wood"
#     color = "brown"

# #Создаем методы класса, функции
#     def function(self):
#          print('Any text')

# fun = Table()
# fun.function()
# x = fun.material
# print(x)

"""
class Color:
     red = 0
     green = 0
     blue = 0

     def __init__(self, r,g,b):
        red = r
        green = g
        blue = b

     def toHex(self):
          return '#%02x%02x%02x' % (red, green, blue)

class ColorAlpha(Color):
  alpha = 1

  def __init__(self,r,g,b,a):
    red = r
    green = g
    blue = b
    alpha = a

gray = Color(80, 80, 80) #серый цвет

red = ColorAlpha(255, 0,0,.5) #Наполовину непрозрачный красный цвет
 """

""" class tableClass:
  __color = 'Not Color'

  def __init__(self, color, mat):
    self.color = color
    self.__mat = mat

  def get_mat(self):
    return self.__mat

  def set_mat(self, mat):
    self.__mat = mat

  @staticmethod
  def testStMet(color):
    if color == 'red':
      print('Red')
    else:
      print('No Red')

  @classmethod
  def testClsMet(cls):
    tmp = cls('metal')
    return tmp

redT = tableClass('red', 'wood')
#print(redT.__mat)
print(retT.color) """

#Практические задачи:

#1:
'''
Необходимо создать класс person, хранящий информацию о человеке.
Атрибуты класса person:
name – имя(str)
age – возраст(int)
number – номер(str)
address – адрес проживания(str)

Создайте конструктор
'''
'''
#Входим в тело класса person
class Person:

#Свойства созданы, передаем в инициализатор, и назначаем эти свойства опеределенным переменным
  def __init__(self, name, age = None, number=None, adress=None):
#Динамические поля
    self.name = name
    self.ad = adress
    self.nu = number
    self.a = age

pers = Person('a')
'''
#2:

#m = [[1, 2 ,3][4, 5, 6]]
#Колво строк - кол-во списков
#Колво стобцоб - кол-во элементов в списке
'''
class Matrix:
  def __init__(self, data): #Передаем self (ссылку на текущий объект)  и data (тобиш наш список, матрица)
    columns = len(data[0]) #Берем размер списка первого и записываем в переменную columns и сравниваем другие списки с этим
    correct = all(map(lambda i: len(i) == columns, data)) #И используем all и map
# map берет поочередно элемент из списка. Берет первый список, lambda функция записывает в переменную i, и проверяют, равен ли размер переданного списка размеру заданного (первого)
#В переменную correct записывается истина или ложь, если истина идем в блок if
    if correct:
      self.rows = len(data) #В количество строк записываем количество списков
      self.columns = len(data[0]) #В количество столбцов записываем кличество элементов
      self.a = data #И сохранеяем переданный список общий, дату он сохраняется, и передается в переменную a

#Перегрузка __str__

Оператор __str__ вызывается с целью преобразовать наш объект в тип данных str (то есть текст)
Данный метод логично возвращает строку. Последняя строка кода сделает все
что нужно для реализации __str__ в одну строку

  def __str__(self):
    res='' #Создаем строку res кода будет по итогу записан ответ
    for row in self.a: #Пробегаемся по переданному списку, записан в переменную a, получаем элементы списка (вложенные списки)
      res+=' '.join(map(str, row)) + '\n' #передаем список в map и он берет каждый элемент списка, применяет к ним функцию str, а join объединяет элементы в строку. В конце символ переноса строки, чтобы видеть матрицу
    return res[:-1] #Ну и возврат ответа, до -1 символа (без символа переноса строки ('\n'))
    #return '\n'.join(map(labmda row: ' '.join(map(str, row)), self.a))

obj1 = Matrix([[1, 2, 3], [4, 5, 6]])
print((obj1))
'''
'''
class Matrix:
    def __init__(self, data):
        columns = len(data[0])
        correct = all(map(lambda i: len(i) == columns, data))
        if correct:
            self.rows = len(data)
            self.columns = len(data[0])
            self.a=data

    def __str__(self):
        res=''
        for row in self.a:
            res+=' '.join(map(str, row)) + '\n'
        return res[:-1]
        return '\n'.join(map(lambda row: ' '.join(map(str, row)), self.a))

    def __add__(self, other):
      if type(other) is Matrix and (self.rows, self.colums) == (other.rows, other.columns):
        data = []
        for row_a, row_b in zip(self.a, other.a):
          data.append(list(map(lambda a, b: a+b, row_a, row_b)))
        return Matrix(data)


obj1 = Matrix([[1, 2, 3], [4, 5, 6]])
obj2 = Matrix([[7, 8, 9], [10, 10, 10]])

obj3 = obj1 + obj2 #+ реализуется через метод __add__, реализуется у левого объекта, ссылка self записывается на него, а other на правый

print(obj3)
'''
