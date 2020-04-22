#импортируем библиотеку для красивого вывода
from pprint import pprint 

#создаётся класс, под названием 'Car'
class Car:
    pass
#создаём подкласс(наследование)
class Honda(Car):
    pass
#создаём подкласс(наследование)
class Toyota(Car):
    pass
#создаём подкласс(наследование)
class Lada(Car):
    pass
#создаём подкласс(наследование)
class Seat(Car):
    pass
    
#создаём функцию, конструктор класса, без него программа не будет работат
def __init__(self, make, year, body):
    self.make, self.year, self.body = make, year, body
    self.key = (make, body)
#создаём функцию, отвечающую за строковое представление вывода
def __repr__(self):
    return "Car('%s', %s, '%s')" % (self.make, self.year, self.body)

#основная программа, присваиваем списки к переменным    
    honda = Car("honda", 1999, "universal")
    toyota = Car("toyota", 1995, "sedan")
    lada = Car("lada", 2020, "sedan")
    seat = Car("seat", 2002, "universal")

#описываем ключи словаря
    cars = {
            honda.key: honda,
            toyota.key: toyota,
            lada.key: lada,
            seat.key: seat,
            }
#вывод в консоль
pprint(cars)
pprint(cars[seat.key])