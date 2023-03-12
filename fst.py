'''#Вывести квадрат числа
num = int(input('Введите число: '))
print((lambda num: num**2)(num))'''

'''#Task 1. Найти сумму всех четных чисел от 1 до 15
num1 = 1
num2 = 15
result = 0
for i in (num1, num2+1):
	if i%2==0:
		result +=i
print(result)
'''
#Программа для возведения числа в любую степень
from tkinter import *

def stepen():
	st = step.get()
	num = ent.get()
	nums = int(num) ** int(st)
	lbl['text'] = f'{num} ** {st} = {nums}'

wind = Tk()
wind.geometry('500x300')
wind.resizable(0,0)
wind.title('Возведение в степень')

lbl = Label(wind,
	height=3, width=72,
	bg= 'firebrick1',
	text='Здесь будет число после возведения в степень'
)
lbl.pack(side=TOP)

btn=Button(wind,
	height=3, width=20,
	bg='darkorange', activebackground='slateblue',
	text='Возведение в степень', command=stepen
)
btn.place(x=170,y=250)

ent = Entry(
	wind,
	width=30, bg='springgreen2'
)
ent.pack()

step=Entry(wind, width=15, bg='cyan')
step.pack()

wind.mainloop()
