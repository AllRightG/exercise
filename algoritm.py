""" #Алгоритмы и их сложности
# O(1) - константная О:
a = (1, 6, 7)
a[0]
size

# O(n) - линейно растет с увеличением входных данных:
for i in range(10) #Сколько укажем, столько и операций

for i in range(10) # Когда 2 цикла подряд, не вложенных - n + n...
#O(n+n) -> o(n)
for i in range(10):
  for i in range(10): #Здесь уже o(n^2)
 """
""" #Задачи:
def task_1(a:list, sum:int) -> tuple: #Задаем типы данных, хотим получить tuple (кортеж)
  for i in range(len(a)):
    for j in range(i+1, len(a)):
      if a[i] + a[j] == sum:
        return a[i], a[j]
#O(n^2)
 """
