#ООП:

#Класс - шаблон для начала объекта, некий чертеж для создания объектов
#Объект - сущность которое обладает поведением и состояние класса, реализация какого-либо класса
#Свойства - переменные внутри класса которые его описывают
#Функции - методы класса


#Принципы ООП:
#Обстракция - оставить (выделить) главное и отбросить второстепенное, все по делу
#Инкапсуляция - принцип, в сути которого скрыть сложность програмного компонента за его интерфейсом, доступ к данным ВНЕ класса закрыт
#Наследование - возможность создать другой класс за счет старого, с учетом добавления чего-то нового, более совершенная версия класса
#Полиморфизм - поддержка нескольких реализаций на основе общего интерфейса?


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
