class Square:
    def __init__(self, side):
        self.side=side
    def area(self):
        return self.side*self.side
    
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    
sq=Square(10)
rec=Rectangle(10,20)

# print(sq.area())
# print(rec.area()) 

#using polymorphism 

def area_of_shapes(aaa):
    print(aaa.area())

area_of_shapes(sq)
area_of_shapes(rec)


def greeting():
    print("hello world")
