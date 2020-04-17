#импортируем библиотеку для красивого вывода
from pprint import pprint 

#описываем класс
class Car:
    
    def __init__(self, make, year, body):
        self.make, self.year, self.body = make, year, body
        self.key = (make, body)
    
    def __repr__(self):
        return "Car('%s', %s, '%s')" % (self.make, self.year, self.body)

#присваиваем переменные    
honda = Car("honda", 1999, "universal")
toyota = Car("toyota", 1995, "sedan")
lada = Car("lada", 2020, "sedan")
seat = Car("seat", 2002, "universal")

#описываем ключи
cars = {
        honda.key: honda,
        toyota.key: toyota,
        lada.key: lada,
        seat.key: seat,
        }
#вывод в консоль
pprint(cars)
pprint(cars[seat.key])