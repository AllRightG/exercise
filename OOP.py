#ООП:

#Класс - шаблон для начала объекта
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

class tableClass:
  __color = ''

  def __init__(self, mat):
  #self.color = color
    self.mat = mat

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

redT = tableClass.testClsMet()
print(redT.mat)
