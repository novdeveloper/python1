# создать Myint ult 2+2 = 5

class Myint(int):
        
    def __add__(self, x):
        return super().__add__(x+1)
    
    
a = Myint(2)
print(a+2)