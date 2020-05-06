class Myint():
        
    #создаём функцию, конструктор класса, без него программа не будет работать

    def __init__(self, x):
        #прибавление двойки к иксу
        self.x = x+2
        self.key = (x)
    #создаём функцию, отвечающую за строковое представление вывода

    def __repr__(self):
        return "Myint('%s')" % (self.x)



a = Myint(2)

#print(type(a))
#print(a+1)
print(a)