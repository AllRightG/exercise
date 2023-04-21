class car: #Создание класса
#атрибуты класса
	name = "Volga"
	make ="Lada"
	model="2007"

#методы класса
	def start(self):
		print("start")

	def stop(self):
		print("stop")

car_1 = car()
car_1.start()
x = car_1.name
print(x)
