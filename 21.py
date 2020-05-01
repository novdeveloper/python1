#импортируем библиотеку для красивого вывода

from pprint import pprint 

#создаётся класс, под названием 'Car'

class Car:
    #создаём функцию, конструктор класса, без него программа не будет работат

    def __init__(self, make, year, body):
        self.make, self.year, self.body = make, year, body
        self.key = (make, body)
    #создаём функцию, отвечающую за строковое представление вывода

    def __repr__(self):
        return "Car('%s', %s, '%s')" % (self.make, self.year, self.body)
#создаём подкласс(наследование)

class Honda(Car):
    #тип двигателя установленного на автомобиле
    gasoline = "benzine"

#создаём подкласс(наследование)

class Toyota(Car):
    #тип двигателя установленного на автомобиле
    gasoline = "Бензин"

#создаём подкласс(наследование)

class Lada(Car):
    pass

#создаём подкласс(наследование)

class Seat(Car):
    pass
    
#показываем тип двигателя автомобиля, используя подкласс Honda()
honda = Honda("хонда", 1999, "универсал")
pprint(honda.gasoline)


#показываем тип двигателя автомобиля, используя подкласс Toyota()
toyota = Toyota("тойота", 1999, "седан")
toyota.gasoline = "дизель"
pprint(toyota.gasoline)


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